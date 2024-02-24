from tools import *
from envs import *

original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_10_DG,
    "-qg",
]

optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_10_DG_OPTIMIZED,
    "-qg",
]
