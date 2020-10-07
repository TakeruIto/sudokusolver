import sys
from utils import file2txt
from solver import Solver

def parseargs():
    path = sys.argv[1]
    return path

def solve():
    path = parseargs()
    txt = file2txt(path)
    solver = Solver(txt)

if __name__ == "__main__":
    solve()
