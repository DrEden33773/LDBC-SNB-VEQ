from .base import *
import os

""" BI 10 """

# DG
BI_10_DG = COMMON_DG
BI_10_DG_OPTIMIZED = COMMON_DG_OPTIMIZED

# China QG
SHORT_CHINA_POST_QG = "short_china_post_query_graph.txt"
SHORT_CHINA_COMMENT_QG = "short_china_comment_query_graph.txt"
LONG_CHINA_POST_QG = "long_china_post_query_graph.txt"
LONG_CHINA_COMMENT_QG = "long_china_comment_query_graph.txt"

# India QG
SHORT_INDIA_POST_QG = "short_india_post_query_graph.txt"
SHORT_INDIA_COMMENT_QG = "short_india_comment_query_graph.txt"
LONG_INDIA_POST_QG = "long_india_post_query_graph.txt"
LONG_INDIA_COMMENT_QG = "long_india_comment_query_graph.txt"

# China Log(Result)
SHORT_CHINA_POST_RES = "short_china_post_result.txt"
SHORT_CHINA_COMMENT_RES = "short_china_comment_result.txt"
LONG_CHINA_POST_RES = "long_china_post_result.txt"
LONG_CHINA_COMMENT_RES = "long_china_comment_result.txt"

# India Log(Result)
SHORT_INDIA_POST_RES = "short_india_post_result.txt"
SHORT_INDIA_COMMENT_RES = "short_india_comment_result.txt"
LONG_INDIA_POST_RES = "long_india_post_result.txt"
LONG_INDIA_COMMENT_RES = "long_india_comment_result.txt"

# Dirname
BI_10_DIRNAME = "BI_10"
BI_10_ORIGINAL_Q_PRE = f"{ORIGINAL_QUERY_PREFIX}/{BI_10_DIRNAME}"
BI_10_OPTIMIZED_Q_PRE = f"{OPTIMIZED_QUERY_PREFIX}/{BI_10_DIRNAME}"
BI_10_ORIGINAL_L_PRE = f"{ORIGINAL_LOG_PREFIX}/{BI_10_DIRNAME}"
BI_10_OPTIMIZED_L_PRE = f"{OPTIMIZED_LOG_PREFIX}/{BI_10_DIRNAME}"

for e in [
    BI_10_ORIGINAL_Q_PRE,
    BI_10_OPTIMIZED_Q_PRE,
    BI_10_ORIGINAL_L_PRE,
    BI_10_OPTIMIZED_L_PRE,
]:
    if not os.path.exists(e):
        os.makedirs(e)
