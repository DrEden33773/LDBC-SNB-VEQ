from prelude import *
from datetime import datetime


def date_str_to_timestamp(date_str: str) -> int:
    return int(datetime.strptime(date_str, "%Y-%m-%d").timestamp())


explicit_place_labels = (
    {"China", "India"}
    .union({"Tunisia", "Cuba", "France"})
    .union({"Belgium", "Greece", "Chile"})
)

explicit_tagclass_labels = {
    "NascarDriver",
    "Thing",
    "Politician",
}.union({"Saint", "President", "Song"})

raw_date_labels = {"2010-01-07", "2010-01-10", "2010-01-26"}
raw_end_date_labels = {"2012-11-11", "2012-11-09", "2012-11-03"}

explicit_date_labels = set(map(date_str_to_timestamp, raw_date_labels))
explicit_end_date_labels = set(map(date_str_to_timestamp, raw_end_date_labels))

explicit_personId_labels = {
    "98214",
    "4886",
    "60769",
}
