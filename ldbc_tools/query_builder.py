from dataclasses import dataclass
from typing import Callable, Self
from ldbc_tools.bin_adapter import run_multiple_veq_m_100k
from ldbc_tools.query_graph import QGMetaRecord, qg_emitter, replace


@dataclass
class QueryBuilder:
    edges: list[tuple[int, int]]
    labels: list[str]
    raw_task_names: list[list[str]]
    QG_PRE: str
    LOG_PRE: str
    args_starting: list[str]
    kwargs: dict[str, QGMetaRecord]

    replace_indices = list[int]()
    replace_wrapper: Callable[[list[str]], list[str]] = lambda x: x

    def __repr__(self) -> str:
        return f"""QueryBuilder {{
    edges: {self.edges},
    labels: {self.labels},
    raw_task_names: {self.raw_task_names},
    QG_PRE: {self.QG_PRE},
    LOG_PRE: {self.LOG_PRE},
    args_starting: {self.args_starting},
    replace_indices: {self.replace_indices},
    replace_wrapper: {self.replace_wrapper},
    kwargs: {self.kwargs:},
}}"""

    def with_replace_indices(self, replace_indices: list[int]) -> Self:
        self.replace_indices = replace_indices
        return self

    def with_replace_wrapper(
        self, replace_wrapper: Callable[[list[str]], list[str]]
    ) -> Self:
        self.replace_wrapper = replace_wrapper
        return self

    def kwargs_unite_with(self, kwargs: dict[str, QGMetaRecord]) -> Self:
        self.kwargs.update(kwargs)
        return self

    def __build_qg(self):
        for qg_name, meta_record in self.kwargs.items():
            qg_path = f"{self.QG_PRE}/{qg_name}.txt"
            labels = meta_record.labels
            edges = meta_record.edges
            qg_emitter(qg_path, labels, edges)

    def __build_task_names(self):
        self.task_names = [
            ",".join(raw_task_name) for raw_task_name in self.raw_task_names
        ]

    def __build_args(self):
        self.args_list = [
            self.args_starting + [f"{self.QG_PRE}/{task_name}.txt"]
            for task_name in self.task_names
        ]

    def __build_kwargs(self):
        for task_name, raw_task_name in zip(self.task_names, self.raw_task_names):
            labels = self.labels
            if self.replace_indices:
                labels = replace(
                    self.labels,
                    self.replace_indices,
                    self.replace_wrapper(raw_task_name),
                )
            self.kwargs[task_name] = QGMetaRecord(labels, self.edges)

    def build(self) -> Self:
        self.__build_task_names()
        self.__build_kwargs()
        self.__build_qg()
        self.__build_args()
        return self

    def run(self) -> list[float]:
        time_table = list[float]()
        result_path_list = [
            f"{self.LOG_PRE}/{task_name}.txt" for task_name in self.task_names
        ]
        run_multiple_veq_m_100k(
            result_path_list,
            self.task_names,
            self.args_list,
            time_table,
        )
        return time_table

    def run_with_elapsed_time_table_ret(self) -> tuple[list[float], list[float]]:
        time_table = list[float]()
        outer_elapsed_time_table = list[float]()
        result_path_list = [
            f"{self.LOG_PRE}/{task_name}.txt" for task_name in self.task_names
        ]
        run_multiple_veq_m_100k(
            result_path_list,
            self.task_names,
            self.args_list,
            time_table,
            outer_elapsed_time_table,
        )
        return time_table, outer_elapsed_time_table
