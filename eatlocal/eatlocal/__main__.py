from .eatlocal import extract_bite, submit_bite, download_bite
from .cli import get_args
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from os import devnull


@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, "w") as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


def main():
    args = get_args()
    if args.extract:
        extract_bite(args.extract)
    elif args.submit:
        with suppress_stdout_stderr():
            submit_bite(args.submit)
    elif args.download:
        download_bite(args.download)


if __name__ == "__main__":
    main()
