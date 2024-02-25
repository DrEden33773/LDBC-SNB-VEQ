from envs import *
from .tools import *

bi_13_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_13_DG,
    "-qg",
]

bi_13_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_13_DG_OPTIMIZED,
    "-qg",
]
