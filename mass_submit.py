import json
import sys
from dataclasses import dataclass
from os import environ
from pathlib import Path

from dotenv import dotenv_values
from playwright.sync_api import Page, sync_playwright
from rich.traceback import install

from console import console
from constants import (
    BITE_URL,
    LOCAL_BITES_DB,
    LOGIN_URL,
    PROFILE_URL,
    TIMEOUT_LENGTH,
    ConsoleStyle,
)

install(show_locals=True)


@dataclass
class Bite:
    """Dataclass for a PyBites bite.

    Attributes:
        title: The title of the bite.
        slug: The slug of the bite.
        platform_content: The content of the bite downloaded from the platform.

    """

    title: str = None
    slug: str = None
    platform_content: str = None

    @property
    def url(self) -> str:
        return BITE_URL.format(bite_slug=self.slug)

    def bite_slug_to_dir(self, pybites_repo: Path) -> Path:
        return Path(pybites_repo).resolve() / self.slug

    def fetch_local_code(self, config: dict) -> None:
        bite_dir = self.bite_slug_to_dir(config["PYBITES_REPO"])
        if not bite_dir.is_dir():
            console.print(
                f":warning: Unable to find bite {self.title} locally.",
                style=ConsoleStyle.WARNING.value,
            )
            console.print(
                "Please make sure that your local pybites directory is correct and bite has been downloaded.",
                style=ConsoleStyle.SUGGESTION.value,
            )
            self.local_code = None
        else:
            python_file = [
                file
                for file in list(bite_dir.glob("*.py"))
                if not file.name.startswith("test_")
            ][0]

            with open(python_file) as file:
                self.local_code = file.read()


def load_config(env_path: Path) -> dict[str, str]:
    """Load configuration from .env file.

    Args:
        env_path: Path to .env file.

    Returns:
        dict: Configuration variables.

    """
    config = {"PYBITES_USERNAME": "", "PYBITES_PASSWORD": "", "PYBITES_REPO": ""}
    if not env_path.exists():
        console.print(
            ":warning: Could not find or read .eatlocal/.env in your home directory.",
            style=ConsoleStyle.WARNING.value,
        )
        console.print(
            "Please run [underline]eatlocal init[/underline] first.",
            style=ConsoleStyle.SUGGESTION.value,
        )
        sys.exit()
    config.update(dotenv_values(dotenv_path=env_path))
    return config


def login(browser, username: str, password: str) -> Page:
    """Login to the PyBites platform.

    Args:
        browser: Playwright browser object.
        username: PyBites username.
        password: PyBites password.

    Returns:
        An authenticated page object for the PyBites platform.

    """
    page: Page = browser.new_page()
    # only shorten for debugging, some bites need in e2e test need longer
    page.set_default_timeout(TIMEOUT_LENGTH)
    page.goto(LOGIN_URL)

    page.click("#login-link")
    page.fill('input[name="login"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    return page


def fetch_local_bites(config: dict) -> Bite:
    """Choose a local bite to submit.

    Args:
        config: Dictionary containing the user's PyBites credentials.

    Returns:
        A Bite object.

    """
    with open(LOCAL_BITES_DB, "r") as local_bites:
        bites = json.load(local_bites)
    return bites


def submit_bite(
    bite: str,
    config: dict,
    page: Page,
) -> None:
    """Submit the bite to the PyBites platform.

    Args:
        bite: The name of the bite to submit.
        config: Dictionary containing the user's PyBites credentials.

    Returns:
        None

    """
    bite.fetch_local_code(config)
    if bite.local_code is None:
        console.print(
            ":warning: Unable to find local code for bite.",
            style=ConsoleStyle.WARNING.value,
        )
        return

    page.goto(bite.url)
    page.wait_for_url(bite.url)
    page.evaluate(
        f"""document.querySelector('.CodeMirror').CodeMirror.setValue({
            repr(bite.local_code)})"""
    )
    page.click("#validate-button")
    page.wait_for_selector("#feedback", state="visible")
    page.wait_for_function(
        "document.querySelector('#feedback').innerText.includes('test session starts')"
    )

    validate_result = page.text_content("#feedback")
    if "Congrats, you passed this Bite" in validate_result:
        console.print(f"{bite.title} and passed!", style=ConsoleStyle.SUCCESS.value)
    else:
        console.print(
            f":warning: {bite.title} did not pass the tests.",
            style=ConsoleStyle.WARNING.value,
        )
    return page


if __name__ == "__main__":
    env_path = Path(environ["HOME"]) / ".eatlocal" / ".env"
    config = load_config(env_path)
    bites = fetch_local_bites(config)
    with sync_playwright() as p:
        with p.chromium.launch() as browser:
            page = login(
                browser,
                config["PYBITES_USERNAME"],
                config["PYBITES_PASSWORD"],
            )
            if page.url != PROFILE_URL:
                console.print(
                    ":warning: Unable to login to PyBites.",
                    style=ConsoleStyle.WARNING.value,
                )
                console.print(
                    "Ensure your credentials are valid.",
                    style=ConsoleStyle.SUGGESTION.value,
                )
            for bite in bites.items():
                bite = Bite(*bite)
                page = submit_bite(bite, config, page)
