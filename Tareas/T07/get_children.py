def get_children(item, dict={}):
    num_children = item.childCount()
    for n in range(num_children):
        # Es un archivo.
        if item.child(n).childCount() == 0 \
                and item.child(n).text(0).count(".") > 0:

            path = []
            while item is not None:
                path.append(str(item.text(0)))
                item = item.parent()
            path = '/' + '/'.join(reversed(path))

            dict.update({"file": path})

        # Es una carpeta con elementos.
        elif item.child(n).childCount() != 0:
            dict = get_children(item.child(n), dict)

        # Es una carpeta vacia.
        else:
            path = []
            while item is not None:
                path.append(str(item.text(0)))
                item = item.parent()
            path = '/' + '/'.join(reversed(path))
            dict.update({"folder": (path,[])}

    return dict

