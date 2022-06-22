import re

test = "this is some text. does it work? we don't know! good luck."


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = re.split(r'([.?!])', text)
    capped = []
    for s in sentences:
        if s.startswith(' '):
            capped.append(' ' + s.strip().capitalize())
        else:
            capped.append(s.capitalize())
    return ''.join(capped)
