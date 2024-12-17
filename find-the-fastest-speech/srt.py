from datetime import timedelta
from typing import List


def _calc_diff(time_stamps: str) -> int:
    start, end = time_stamps.split(" --> ")
    hours, minutes, seconds = start.split(":")
    start = timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds.split(",")[0]))
    hours, minutes, seconds = end.split(":")
    end= timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds.split(",")[0]))
    return (end - start).total_seconds()


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    sections_with_ratios = []
    for section in text.strip().split("\n\n"):
        num, time_stamps, caption = [line.strip() for line in section.split("\n") if line]
        diff = _calc_diff(time_stamps)
        ratio = diff / len(caption)
        sections_with_ratios.append((int(num), ratio))

    return [s[0] for s in sorted(sections_with_ratios, key=lambda x: x[1])]




if __name__ == "__main__":
    get_srt_section_ids("1\n00:00:00,000 --> 00:00:01,000\nlet's code\n\n2\n00:00:00,000 --> 00:00:03,000\ncode")
