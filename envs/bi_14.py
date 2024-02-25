from .base import *
import os

""" BI 14 """

BI_14_DG = COMMON_DG
BI_14_DG_OPTIMIZED = COMMON_DG_OPTIMIZED

BI_14_DIRNAME = "BI_14"
BI_14_ORIGINAL_Q_PRE = f"{ORIGINAL_QUERY_PREFIX}/{BI_14_DIRNAME}"
BI_14_OPTIMIZED_Q_PRE = f"{OPTIMIZED_QUERY_PREFIX}/{BI_14_DIRNAME}"
BI_14_ORIGINAL_L_PRE = f"{ORIGINAL_LOG_PREFIX}/{BI_14_DIRNAME}"
BI_14_OPTIMIZED_L_PRE = f"{OPTIMIZED_LOG_PREFIX}/{BI_14_DIRNAME}"

for e in [
    BI_14_ORIGINAL_Q_PRE,
    BI_14_OPTIMIZED_Q_PRE,
    BI_14_ORIGINAL_L_PRE,
    BI_14_OPTIMIZED_L_PRE,
]:
    if not os.path.exists(e):
        os.makedirs(e)
