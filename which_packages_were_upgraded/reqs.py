def _parse_req(reqs: str) -> tuple[str, list[int]]:
    """
    >>> _parse_req("chardet==3.0.4")
    ('chardet', [3, 0, 4])
    """
    lib, version = reqs.split("==")
    return lib, [int(v) for v in version.split(".")]


def changed_dependencies(old_reqs: str, new_reqs: str) -> list[str]:
    """Compare old vs new requirement multiline strings
    and return a list of dependencies that have been upgraded
    (have a newer version)
    """
    upgraded_libs = []
    for line_old, line_new in zip(
        old_reqs.strip().splitlines(), new_reqs.strip().splitlines()
    ):
        library_name, old_version = _parse_req(line_old)
        _, new_version = _parse_req(line_new)
        for old_v, new_v in zip(old_version, new_version):
            if old_v == new_v:
                continue
            elif old_v > new_v:
                break
            elif old_v < new_v:
                upgraded_libs.append(library_name)
                break
    return upgraded_libs
