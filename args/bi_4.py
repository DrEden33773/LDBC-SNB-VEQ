from envs import *
from .tools import *

bi_4_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_4_DG,
    "-qg",
]

bi_4_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_4_DG_OPTIMIZED,
    "-qg",
]
