from csv import DictReader
from collections import Counter
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = "bite_output_log.txt"
DATA = os.path.join(TMP, LOGS)
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
if not os.path.isfile(DATA):
    urlretrieve(f"{S3}/{LOGS}", DATA)


class BiteStats:
    def __init__(self, data=DATA):
        self.rows = []
        with open(data) as data:
            rows = DictReader(data)
            self.rows = [row for row in rows]

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len({row["bite"] for row in self.rows})

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len({
            row["bite"]
            for row in self.rows
            if row["completed"] == "True"
        })

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len({row["user"] for row in self.rows})

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
        one or more Bites"""
        return len({
            row["user"]
            for row in self.rows
            if row["completed"] == "True"
        })

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
        (= in most rows)"""
        bite_counts = Counter()
        for row in self.rows:
            bite_counts[row["bite"]] += 1
        return bite_counts.most_common()[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        user_counts = Counter()
        for row in self.rows:
            if row["completed"] == "True":
                user_counts[row["user"]] += 1
        return user_counts.most_common()[0][0]
