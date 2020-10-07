def file2txt(path):
    with open(path) as f:
        txt = f.read()
        return txt
