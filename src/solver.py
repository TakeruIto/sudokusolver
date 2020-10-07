class Solver:
    def __init__(self, txt):
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols = self.digits

        self.squares = self.cross(self.rows, self.cols)
        self.unitlist = ([self.cross(self.rows, c) for c in self.cols] +
                    [self.cross(r, self.cols) for r in self.rows] +
                    [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        self.units = dict((s, [u for u in self.unitlist if s in u])
                    for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], []))-set([s]))
                    for s in self.squares)

        self.board = self.txt2dict(txt)
        print(self.board)

    def cross(self, A, B):
        return [a+b for a in A for b in B]

    def txt2dict(self, txt):
        chars = [c for c in txt if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))