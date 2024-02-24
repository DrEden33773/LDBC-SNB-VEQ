from enum import StrEnum
import re


class BaseLabel(StrEnum):
    def __repr__(self) -> str:
        return self.value

    def __add__(self, other: str) -> str:
        return f"{self.value}({other})"

    Country = "country"
    Date = "date"
    EndDate = "endDate"
    TagClass = "tagClass"
    PersonId = "personId"


class MsgType(StrEnum):
    Comment = "comment"
    Post = "post"


def get_inner_namespace(col_name: str) -> str:
    match = re.search("\((.*?)\)", col_name)
    return "" if match is None else match.group(1)


def get_namespace(col_name: str) -> str:
    inner_namespace = get_inner_namespace(col_name)
    if inner_namespace in ["Country", "Continent", "City"]:
        return "Placeid"
    if inner_namespace in ["University", "Company"]:
        return "Organisationid"
    return inner_namespace


test_res = get_namespace(":ID(Forumid)") == "Forumid"
assert test_res
