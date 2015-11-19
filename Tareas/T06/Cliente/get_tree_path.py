def get_tree_path(item):
    path = []
    while item is not None:
        path.append(str(item.text(0)))
        item = item.parent()
    return '\\'.join(reversed(path))
