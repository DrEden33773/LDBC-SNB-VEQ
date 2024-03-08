from envs import *
from .tools import *

is_2_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    IS_2_DG,
    "-qg",
]

is_2_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    IS_2_DG_OPTIMIZED,
    "-qg",
]
