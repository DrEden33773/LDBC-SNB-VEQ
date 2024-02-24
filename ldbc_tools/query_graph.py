import os


def replace(
    template: list[str],
    indices: list[int],
    replacements: list[str],
) -> list[str]:
    assert len(indices) == len(replacements)
    for i in indices:
        assert 0 <= i < len(template)

    res = template.copy()
    for i, r in zip(indices, replacements):
        res[i] = r

    return res


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
