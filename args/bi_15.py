from envs import *
from .tools import *

bi_15_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_15_DG,
    "-qg",
]

bi_15_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_15_DG_OPTIMIZED,
    "-qg",
]
