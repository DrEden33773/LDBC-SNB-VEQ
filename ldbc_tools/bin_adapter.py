from typing import Optional
import subprocess, os


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
        header = content.split(":")[0]
        processing_time = (
            float(content.split(" ")[-1])
            if header == "Processing Time (ms)"
            else float("nan")
        )
        time_table.append(processing_time)


def run_multiple_veq_m_100k(
    result_path_list: list[str],
    task_name_list: list[str],
    args_list: list[list[str]],
    time_table: Optional[list[float]] = None,
):
    assert len(result_path_list) == len(task_name_list) == len(args_list)
    n = len(result_path_list)
    for i in range(n):
        run_veq_m_100k(result_path_list[i], task_name_list[i], args_list[i], time_table)
