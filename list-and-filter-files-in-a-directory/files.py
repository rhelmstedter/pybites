import os
from os import listdir
from os.path import getsize

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    return [
        file
        for file in listdir(dirname)
        if (getsize(os.path.join(dirname, file)) / ONE_KB) >= size_in_kb
    ]
