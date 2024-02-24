from tools import *
from envs import *

original_china_match_args = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_11_DG,
    "-qg",
    BI_11_CHINA_QG,
]
original_india_match_args = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_11_DG,
    "-qg",
    BI_11_INDIA_QG,
]

optimized_china_match_args = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_11_DG_OPTIMIZED,
    "-qg",
    BI_11_CHINA_QG_OPTIMIZED,
]
optimized_india_match_args = wsl_if_on_windows + [
    "./VEQ_M_100k",
    "-dg",
    BI_11_DG_OPTIMIZED,
    "-qg",
    BI_11_INDIA_QG_OPTIMIZED,
]
