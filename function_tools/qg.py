import os


def qg_labels_builder(
    common_prefix: list[str],
):
    pass


def qg_emitter(
    qg_path: str,
    labels: list[str],
    edges: list[tuple[int, int]],
):
    if not os.path.exists(qg_path):
        with open(qg_path, "w") as f:
            f.write("#0\n")
            f.write(f"{len(labels)}\n")
            [f.write(f"{label}\n") for label in labels]
            f.write(f"{len(edges)}\n")
            [f.write(f"{src} {dst}\n") for src, dst in edges]
