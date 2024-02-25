""" BI 11 """

from .base import *
import os

BI_11_ORIGINAL_Q_PRE = f"{ORIGINAL_QUERY_PREFIX}/BI_11"
BI_11_OPTIMIZED_Q_PRE = f"{OPTIMIZED_QUERY_PREFIX}/BI_11"
BI_11_ORIGINAL_L_PRE = f"{ORIGINAL_LOG_PREFIX}/BI_11"
BI_11_OPTIMIZED_L_PRE = f"{OPTIMIZED_LOG_PREFIX}/BI_11"

for e in [
    BI_11_ORIGINAL_Q_PRE,
    BI_11_OPTIMIZED_Q_PRE,
    BI_11_ORIGINAL_L_PRE,
    BI_11_OPTIMIZED_L_PRE,
]:
    if not os.path.exists(e):
        os.makedirs(e)

BI_11_DG = COMMON_DG
BI_11_CHINA_QG = f"{BI_11_ORIGINAL_Q_PRE}/china_query_graph.txt"
BI_11_INDIA_QG = f"{BI_11_ORIGINAL_Q_PRE}/india_query_graph.txt"

BI_11_DG_OPTIMIZED = COMMON_DG_OPTIMIZED
BI_11_CHINA_QG_OPTIMIZED = f"{BI_11_OPTIMIZED_Q_PRE}/china_query_graph.txt"
BI_11_INDIA_QG_OPTIMIZED = f"{BI_11_OPTIMIZED_Q_PRE}/india_query_graph.txt"

BI_11_ORIGINAL_CHINA_RES = f"{BI_11_ORIGINAL_L_PRE}/china_match_result.txt"
BI_11_ORIGINAL_INDIA_RES = f"{BI_11_ORIGINAL_L_PRE}/india_match_result.txt"

BI_11_OPTIMIZED_CHINA_RES = f"{BI_11_OPTIMIZED_L_PRE}/china_match_result.txt"
BI_11_OPTIMIZED_INDIA_RES = f"{BI_11_OPTIMIZED_L_PRE}/india_match_result.txt"
