from envs import *
from .tools import *

bi_9_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_9_DG,
    "-qg",
]

bi_9_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_9_DG_OPTIMIZED,
    "-qg",
]
