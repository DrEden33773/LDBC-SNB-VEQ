from .base import *
import os

""" BI 3 """

BI_3_DG = COMMON_DG

BI_3_DIRNAME = "BI_3"
BI_3_ORIGINAL_Q_PRE = f"{ORIGINAL_QUERY_PREFIX}/{BI_3_DIRNAME}"
BI_3_OPTIMIZED_Q_PRE = f"{OPTIMIZED_QUERY_PREFIX}/{BI_3_DIRNAME}"
BI_3_ORIGINAL_L_PRE = f"{ORIGINAL_LOG_PREFIX}/{BI_3_DIRNAME}"
BI_3_OPTIMIZED_L_PRE = f"{OPTIMIZED_LOG_PREFIX}/{BI_3_DIRNAME}"

BI_3_DG_OPTIMIZED = f"{BI_3_OPTIMIZED_Q_PRE}/data_graph.txt"

for e in [
    BI_3_ORIGINAL_Q_PRE,
    BI_3_OPTIMIZED_Q_PRE,
    BI_3_ORIGINAL_L_PRE,
    BI_3_OPTIMIZED_L_PRE,
]:
    if not os.path.exists(e):
        os.makedirs(e)
