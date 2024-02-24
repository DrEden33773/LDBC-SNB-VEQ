import os

DATA_PREFIX = "./data"
OUT_PREFIX = "./out"
LOG_PREFIX = "./log"
RAW_DATA_PREFIX = f"{DATA_PREFIX}/raw"
INDEX_EDGES_PREFIX = f"{DATA_PREFIX}/index"
ORIGINAL_QUERY_PREFIX = f"{OUT_PREFIX}/original"
OPTIMIZED_QUERY_PREFIX = f"{OUT_PREFIX}/optimized"
ORIGINAL_LOG_PREFIX = f"{LOG_PREFIX}/original"
OPTIMIZED_LOG_PREFIX = f"{LOG_PREFIX}/optimized"

for e in [
    INDEX_EDGES_PREFIX,
    RAW_DATA_PREFIX,
]:
    if not os.path.exists(e):
        os.makedirs(e)

""" BI 11 """

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

BI_11_DG = f"{BI_11_ORIGINAL_Q_PRE}/data_graph.txt"
BI_11_CHINA_QG = f"{BI_11_ORIGINAL_Q_PRE}/china_query_graph.txt"
BI_11_INDIA_QG = f"{BI_11_ORIGINAL_Q_PRE}/india_query_graph.txt"

BI_11_DG_OPTIMIZED = f"{BI_11_OPTIMIZED_Q_PRE}/data_graph.txt"
BI_11_CHINA_QG_OPTIMIZED = f"{BI_11_OPTIMIZED_Q_PRE}/china_query_graph.txt"
BI_11_INDIA_QG_OPTIMIZED = f"{BI_11_OPTIMIZED_Q_PRE}/india_query_graph.txt"

BI_11_ORIGINAL_CHINA_RES = f"{BI_11_ORIGINAL_L_PRE}/china_match_result.txt"
BI_11_ORIGINAL_INDIA_RES = f"{BI_11_ORIGINAL_L_PRE}/india_match_result.txt"

BI_11_OPTIMIZED_CHINA_RES = f"{BI_11_OPTIMIZED_L_PRE}/china_match_result.txt"
BI_11_OPTIMIZED_INDIA_RES = f"{BI_11_OPTIMIZED_L_PRE}/india_match_result.txt"

""" BI 10 """

# DG
BI_10_DG = BI_11_DG
BI_10_DG_OPTIMIZED = BI_11_DG_OPTIMIZED

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
    BI_10_ORIGINAL_L_PRE,
]:
    if not os.path.exists(e):
        os.makedirs(e)
