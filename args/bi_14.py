from envs import *
from .tools import *

bi_14_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_14_DG,
    "-qg",
]

bi_14_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_14_DG_OPTIMIZED,
    "-qg",
]
