from envs import *
from .tools import *

bi_19_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_19_DG,
    "-qg",
]

bi_19_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_19_DG_OPTIMIZED,
    "-qg",
]
