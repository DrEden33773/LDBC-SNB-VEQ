from prelude import *
from polars import DataFrame
from ldbc_tools.data_graph import *


vertices = dict[str, DataFrame]()
raw_edges = dict[tuple[str, str, str], DataFrame]()
switch_namespace = dict[str, dict[int, int]]()
vertex_num, edge_num = 0, 0

labels = dict[int, str]()
label_set = set[str]()
edges = set[tuple[int, int]]()

index_edges = dict[str, DataFrame]()
index_edge_num = 0


def load_vertices_edges():
    """Load `vertices/edges`"""

    for file in glob.glob(f"{RAW_DATA_PREFIX}/*.csv"):
        df_name = os.path.basename(file).split(".")[0]
        if "_" in df_name:
            src, relationship, dst = df_name.split("_")
            raw_edges[(src, relationship, dst)] = pl.read_csv(file)
        else:
            vertices[df_name] = pl.read_csv(file)

    global vertex_num, edge_num
    vertex_num = sum(len(df) for df in vertices.values())
    edge_num = sum(len(df) for df in raw_edges.values())


def rearrange_id():
    """Re-arrange all `:ID($AnyNamespace)`"""

    def init_switch_namespace():
        """Initialize `switch_namespace`"""
        for df in vertices.values():
            base_label = get_namespace(df.columns[0])
            switch_namespace[base_label] = dict()

    init_switch_namespace()
    curr_global_id = 0
    with tqdm(desc="Mapping `origin_id` to `uni_id`", total=vertex_num) as bar:
        for df in vertices.values():
            base_label = get_namespace(df.columns[0])
            map = switch_namespace[base_label]
            for row in df.rows():
                map[int(row[0])] = curr_global_id
                curr_global_id += 1
                bar.update(1)


def build_uid_label_map():
    """Build map of `vertex.uid -> label`"""

    def place_op(df: DataFrame):
        namespace = get_namespace(df.columns[0])
        map = switch_namespace[namespace]
        slice = df.select(
            [
                pl.col(df.columns[0]),
                pl.col("name"),
                pl.col(":TYPE"),
            ]
        )
        for oid, name, ty in slice.rows():
            oid, name, label = int(oid), str(name), str(ty)
            uid = map[oid]
            if name in explicit_place_labels:
                label = BaseLabel.Country + name
            labels[uid] = label
            label_set.add(label)
            bar.update(1)

    def person_op(df: DataFrame):
        namespace = get_namespace(df.columns[0])
        map = switch_namespace[namespace]
        slice = df.select(
            [
                pl.col(df.columns[0]),
                pl.col(":LABEL"),
            ]
        )
        for x, y in slice.rows():
            personId = int(x)
            generalLabel = str(y)
            uid = map[personId]
            label = (
                generalLabel
                if not personId in explicit_personId_labels
                else BaseLabel.PersonId + str(personId)
            )
            labels[uid] = label
            label_set.add(label)
            bar.update(1)

    def tagclass_op(df: DataFrame):
        namespace = get_namespace(df.columns[0])
        map = switch_namespace[namespace]
        slice = df.select(
            [
                pl.col(df.columns[0]),
                pl.col(df.columns[1]),
                pl.col(":LABEL"),
            ]
        )
        for oid, tagclass_name, label in slice.rows():
            uid = map[int(oid)]
            label = (
                str(label)
                if not str(tagclass_name) in explicit_tagclass_labels
                else BaseLabel.TagClass + str(tagclass_name)
            )
            labels[uid] = label
            label_set.add(label)
            bar.update(1)

    def forum_op(df: DataFrame):
        namespace = get_namespace(df.columns[0])
        map = switch_namespace[namespace]
        slice = df.select(
            [
                pl.col(df.columns[0]),
                pl.col(df.columns[2]),
                pl.col(":LABEL"),
            ]
        )
        for oid, creationDate, label in slice.rows():
            uid = map[int(oid)]
            labels[uid] = (
                str(label)
                if not int(creationDate) in explicit_date_labels
                else BaseLabel.Date + str(creationDate)
            )
            label_set.add(str(label))
            bar.update(1)

    def normal_op(df: DataFrame):
        namespace = get_namespace(df.columns[0])
        map = switch_namespace[namespace]
        slice = df.select(
            [
                pl.col(df.columns[0]),
                pl.col(":TYPE" if ":TYPE" in df.columns else ":LABEL"),
            ]
        )
        for oid, label in slice.rows():
            uid = map[int(oid)]
            labels[uid] = str(label)
            label_set.add(str(label))
            bar.update(1)

    def vertex_op(df_name: str, df: DataFrame):
        match df_name:
            case "place":
                place_op(df)
            case "person":
                person_op(df)
            case "tagclass":
                tagclass_op(df)
            case "forum":
                forum_op(df)
            case _:
                normal_op(df)

    with tqdm(desc="Build map of `vertex.uni_id -> label`", total=vertex_num) as bar:
        for df_name, df in vertices.items():
            vertex_op(df_name, df)


def build_origin_edges():
    """Build edges in format: `(src_id, dst_id)`"""
    with tqdm(desc="Build edges in format: `(src_id, dst_id)`", total=edge_num) as bar:
        for df_name, df in raw_edges.items():
            src_namespace = get_namespace(df.columns[0])
            dst_namespace = get_namespace(df.columns[1])
            src_map = switch_namespace[src_namespace]
            dst_map = switch_namespace[dst_namespace]
            slice = df.select(
                [
                    pl.col(df.columns[0]),
                    pl.col(df.columns[1]),
                ]
            )
            for src_id, dst_id in slice.rows():
                src_uni_id = src_map[int(src_id)]
                dst_uni_id = dst_map[int(dst_id)]
                edges.add((src_uni_id, dst_uni_id))
                bar.update(1)


def emit_original_data_graph():
    """Write into `data_graph.txt`"""
    if not os.path.exists(COMMON_DG):
        with open(COMMON_DG, "w") as f:
            f.write("#0\n")
            f.write(f"{len(labels)}\n")
            with tqdm(
                desc=f"Writing `labels` into `{COMMON_DG}`", total=len(labels)
            ) as bar:
                for i in range(len(labels)):
                    f.write(f"{labels[i]}\n")
                    bar.update(1)
            f.write(f"{len(edges)}\n")
            with tqdm(
                desc=f"Writing `edges` into `{COMMON_DG}`", total=len(edges)
            ) as bar:
                for src, dst in edges:
                    f.write(f"{src} {dst}\n")
                    bar.update(1)
    else:
        print(f"File `{COMMON_DG}` already exists")


def build_original_dg(
    original_dg_filepath: str, optimized_dg_filepath: str, overwrite: bool = False
):
    """Build `original data graph`"""
    if (
        not overwrite
        and os.path.exists(optimized_dg_filepath)
        and os.path.exists(original_dg_filepath)
    ):
        print(
            f"File `{optimized_dg_filepath}` & `{original_dg_filepath}` already exists"
        )
        return
    load_vertices_edges()
    rearrange_id()
    build_uid_label_map()
    build_origin_edges()
    emit_original_data_graph()


def load_specified_index_edge(index_csv_filenames: list[str]):
    """Load specified `index edge`"""
    for filename in index_csv_filenames:
        file = f"{INDEX_EDGES_PREFIX}/{filename}.csv"
        df_name = os.path.basename(file).split(".")[0]
        index_edges[df_name] = pl.read_csv(file)
    global index_edge_num
    index_edge_num = sum(len(df) for df in index_edges.values())


def append_index_edges():
    """Append `index edge` into `edges`"""
    with tqdm(desc="Adding `index edge` into `edges`", total=index_edge_num) as bar:
        for df in index_edges.values():
            src_namespace = get_namespace(df.columns[0])
            dst_namespace = get_namespace(df.columns[1])
            src_map = switch_namespace[src_namespace]
            dst_map = switch_namespace[dst_namespace]
            slice = df.select(
                [
                    pl.col(df.columns[0]),
                    pl.col(df.columns[1]),
                ]
            )
            for src_id, dst_id in slice.rows():
                src_uni_id = src_map[int(src_id)]
                dst_uni_id = dst_map[int(dst_id)]
                edges.add((src_uni_id, dst_uni_id))
                bar.update(1)


def emit_optimized_data_graph(dg_filepath: str):
    """Write into `data_graph.txt`"""
    if not os.path.exists(dg_filepath):
        with open(dg_filepath, "w") as f:
            f.write("#0\n")
            f.write(f"{len(labels)}\n")
            with tqdm(
                desc=f"Writing `labels` into `{dg_filepath}`", total=len(labels)
            ) as bar:
                for i in range(len(labels)):
                    f.write(f"{labels[i]}\n")
                    bar.update(1)
            f.write(f"{len(edges)}\n")
            with tqdm(
                desc=f"Writing `edges` into `{dg_filepath}`", total=len(edges)
            ) as bar:
                for src, dst in edges:
                    f.write(f"{src} {dst}\n")
                    bar.update(1)
    else:
        print(f"File `{dg_filepath}` already exists")


def build_optimized_dg(optimized_dg_filepath: str, index_csv_filenames: list[str]):
    """Build `optimized data graph`"""
    if os.path.exists(optimized_dg_filepath):
        print(f"File `{optimized_dg_filepath}` already exists")
        return
    load_specified_index_edge(index_csv_filenames)
    append_index_edges()
    emit_optimized_data_graph(optimized_dg_filepath)
