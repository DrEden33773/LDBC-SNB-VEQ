from envs import *
from .tools import *

bi_3_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_3_DG,
    "-qg",
]

bi_3_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_3_DG_OPTIMIZED,
    "-qg",
]
