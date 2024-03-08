from envs import *
from .tools import *

ic_12_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    IC_12_DG,
    "-qg",
]

ic_12_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    IC_12_DG_OPTIMIZED,
    "-qg",
]
