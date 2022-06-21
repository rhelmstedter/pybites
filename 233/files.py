from datetime import datetime
from os import chdir, listdir, getenv
from os.path import basename, getctime
from pathlib import Path, PosixPath
from time import ctime
from zipfile import ZipFile

TMP = Path(getenv("TMP", "/tmp"))
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def _rename_log(log):
    date = datetime.strptime(ctime(getctime(log)), "%c")
    log_num = basename(log).split(".")[0]
    return f"{log_num}_{date:%Y-%m-%d}.log"


def zip_last_n_files(
    directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3
):
    chdir(directory)
    with ZipFile(zip_file, "w") as zip:
        for log in sorted(listdir(), key=lambda log: getctime(log))[-n:]:
            zip.write(log, _rename_log(log))
