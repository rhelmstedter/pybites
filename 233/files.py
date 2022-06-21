from datetime import datetime
import os
from pathlib import Path, PosixPath
from zipfile import ZipFile
from time import ctime

TMP = Path(os.getenv("TMP", "/tmp"))
LOG_DIR = TMP / "logs"
ZIP_FILE = "logs.zip"


def _rename_log(log):
    date = datetime.strptime(ctime(os.path.getctime(log)), "%c")
    log_num = os.path.basename(log).split(".")[0]
    return f"{log_num}_{date:%Y-%m-%d}.log"


def zip_last_n_files(
    directory: PosixPath = LOG_DIR, zip_file: str = ZIP_FILE, n: int = 3
):
    with ZipFile(directory / zip_file, "w") as zip:
        for log in sorted(
            os.listdir(directory),
            key=lambda log: (os.path.getctime(directory / log)),
        )[-n:]:
            new_name = _rename_log(directory / log)
            zip.write(directory / log, new_name)
