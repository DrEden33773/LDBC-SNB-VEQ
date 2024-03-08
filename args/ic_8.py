from envs import *
from .tools import *

ic_8_original_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    IC_8_DG,
    "-qg",
]

ic_8_optimized_args_starting = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    IC_8_DG_OPTIMIZED,
    "-qg",
]
