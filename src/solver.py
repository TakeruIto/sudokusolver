import utils

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

        self.values = dict((s, self.digits) for s in self.squares)
        self.board = self.txt2dict(txt)

    def cross(self, A, B):
        return [a+b for a in A for b in B]

    def txt2dict(self, txt):
        chars = [c for c in txt if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def solve(self):
        for s,d in self.board.items():
            if d in self.digits and not self._assign(s, d):
                break

        utils.display(self.values, self.rows, self.cols)

    def _assign(self, s, d):
        values_ = self.values[s].replace(d, '')
        return all(self._eliminate(s, d_) for d_ in values_)

    def _eliminate(self, s, d):
        if d not in self.values[s]:
            return True
        self.values[s] = self.values[s].replace(d, '')

        if len(self.values[s])==0:
            return False
        elif len(self.values[s])==1:
            d_ = self.values[s]
            if not all(self._eliminate(s_, d_) for s_ in self.peers[s]):
                return False
        
        for u in self.units[s]:
            dplaces = [s for s in u if d in self.values[s]]
            if len(dplaces )==0:
                return False
            elif len(dplaces)==1:
                if not self._assign(dplaces[0], d):
                    return False

        return True
