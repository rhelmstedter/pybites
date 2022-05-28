import json
import re

DELIMITERS = r",|;|\|"

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    lines = [line.strip("\n") for line in members.strip().split("\n")]
    fieldnames = re.split(DELIMITERS, lines[0])
    data = []
    for line in lines[1:]:
        attributes = re.split(DELIMITERS, line)
        person = {fieldnames[i]: attributes[i] for i in range(4)}
        data.append(person)
    return json.dumps(data)


if __name__ == "__main__":
    print(convert_to_json(members))
