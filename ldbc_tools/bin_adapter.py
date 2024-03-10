from typing import Optional
import subprocess, os
import time as Time


def run_veq_m_100k(
    result_path: str,
    task_name: str,
    args: list[str],
    time_table: Optional[list[float]] = None,
    outer_elapsed_time_table: Optional[list[float]] = None,
):
    if os.path.exists(result_path):
        print(f"File `{result_path}` already exists")
        with open(result_path, "r") as f:
            non_empty_lines = [line for line in f if line.strip() != ""]
            last_line = non_empty_lines[-1].strip()
            penultimate_line = non_empty_lines[-2].strip()
            print(f"    lines[-2] ~> {penultimate_line}")
            print(f"    lines[-1] ~> {last_line}")
            last_header = last_line.split(":")[0]
            penultimate_header = penultimate_line.split(":")[0]
            time = (
                float(penultimate_line.split(" ")[-1])
                if penultimate_header == "Processing Time (ms)"
                else float("nan")
            )
            outer_elapsed_time = float(last_line.split(" ")[-1])
            if not time_table is None:
                time_table.append(time)
            if not outer_elapsed_time_table is None:
                outer_elapsed_time_table.append(outer_elapsed_time)
        print()
        return

    content = ""
    with open(result_path, "w") as f:
        print(f">>> Running: {task_name}...")
        start_time_ns = Time.perf_counter_ns()
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
        end_time_ns = Time.perf_counter_ns()
        elapsed_time_ms = (end_time_ns - start_time_ns) / 1_000_000
        f.write(f"Outer Elapsed Time (ms): {elapsed_time_ms}\n")
        print(f"<<< Done! (Outer Elapsed Time: {elapsed_time_ms} ms)")

    if not time_table is None:
        last_header = content.split(":")[0]
        processing_time = (
            float(content.split(" ")[-1])
            if last_header == "Processing Time (ms)"
            else float("nan")
        )
        if last_header != "Processing Time (ms)":
            print(
                f"--- Warning: No `Processing Time (ms)` detected in `task({task_name})` (`Outer Elapsed Time` is NOT accurate). ---"
            )
            print(
                f'--- ^^^^^^^^ `time_table` will be filled with `float("NaN")` only for marking. ---'
            )
        time_table.append(processing_time)
    if not outer_elapsed_time_table is None:
        outer_elapsed_time_table.append(elapsed_time_ms)


def run_multiple_veq_m_100k(
    result_path_list: list[str],
    task_name_list: list[str],
    args_list: list[list[str]],
    time_table: Optional[list[float]] = None,
    outer_elapsed_time_table: Optional[list[float]] = None,
):
    assert len(result_path_list) == len(task_name_list) == len(args_list)
    n = len(result_path_list)
    for i in range(n):
        run_veq_m_100k(
            result_path_list[i],
            task_name_list[i],
            args_list[i],
            time_table,
            outer_elapsed_time_table,
        )
