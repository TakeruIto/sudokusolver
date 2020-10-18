def file2txt(path):
    with open(path) as f:
        txt = f.read()
        return txt

def display(values, rows, cols):
    width = max([len(v) for v in values.values()]) + 1
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF':
            print('+'.join(['-'*width*3]*3))