import re


def strip_comments(code):
    code = re.sub(
        r'''(?:\s*#\s.*|\s\s#\s.*|\s*"""[\s\S]*?""")(\n)''',
        r"\1",
        code,
        flags=re.MULTILINE,
    )
    return code
