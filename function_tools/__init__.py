""" Function Tools """

import subprocess
from typing import Iterable, Optional
from enum import StrEnum
import re, os


class BaseLabel(StrEnum):
    def __repr__(self) -> str:
        return self.value

    def __add__(self, other: str) -> str:
        return f"{self.value}({other})"

    Country = "country"
    Date = "date"
    EndDate = "endDate"
    TagClass = "tagClass"


def run_veq_m_100k(
    result_path: str,
    task_name: str,
    args: list[str],
    time_table: Optional[list[float]] = None,
):
    if os.path.exists(result_path):
        print(f"File `{result_path}` already exists")
        with open(result_path, "r") as f:
            non_empty_lines = [line for line in f if line.strip() != ""]
            last_line = non_empty_lines[-1]
            print(f"    last_line ~> {last_line}")
            time = float(last_line.split(" ")[-1])
            if not time_table is None:
                time_table.append(time)
        return

    content = ""
    with open(result_path, "w") as f:
        print(f">>> Running: {task_name}...")
        with subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as p:
            if p.stdout:
                for line in iter(p.stdout.readline, b""):
                    content = line.decode("utf-8")
                    print("    " + content, end="")
                    f.write(content)
            else:
                print("    <No output>")
                f.write("<No output>")
        print("<<< Done!")
    if not time_table is None:
        processing_time = float(content.split(" ")[-1])
        time_table.append(processing_time)


def run_multiple_veq_m_100k(
    result_path_list: list[str],
    task_name_list: list[str],
    args_list: list[list[str]],
    time_table_list: Optional[list[list[float]]] = None,
):
    assert len(result_path_list) == len(task_name_list) == len(args_list)
    if not time_table_list is None:
        assert len(result_path_list) == len(time_table_list)
    n = len(result_path_list)
    for i in range(n):
        run_veq_m_100k(
            result_path_list[i],
            task_name_list[i],
            args_list[i],
            time_table_list[i] if not time_table_list is None else None,
        )


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


def query_graph_emitter(
    qg_path: str,
    labels: list[str],
    edges: list[tuple[int, int]],
):
    if not os.path.exists(qg_path):
        with open(qg_path, "w") as f:
            f.write("#0\n")
            f.write(f"{len(labels)}\n")
            [f.write(f"{label}\n") for label in labels]
            f.write(f"{len(edges)}\n")
            [f.write(f"{src} {dst}\n") for src, dst in edges]


test_res = get_namespace(":ID(Forumid)") == "Forumid"
assert test_res
