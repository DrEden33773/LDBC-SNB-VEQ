from envs import *
from .tools import *

bi_10_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_10_DG,
    "-qg",
]

bi_10_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_10_DG_OPTIMIZED,
    "-qg",
]
