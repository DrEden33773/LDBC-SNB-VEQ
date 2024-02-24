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

COMMON_DG = f"{ORIGINAL_QUERY_PREFIX}/data_graph.txt"
COMMON_DG_OPTIMIZED = f"{OPTIMIZED_QUERY_PREFIX}/data_graph.txt"
