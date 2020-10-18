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
        self.values = self._search(self._solve(self.values))

        utils.display(self.values, self.rows, self.cols)

    def _solve(self, values):
        for s, d in self.board.items():
            if d in self.digits and not self._assign(values, s, d):
                return False
        return values

    def _search(self, values):
        if not values:
            return False
        if all(len(values[s])==1 for s in self.squares):
            return values
        tmp = dict((s, len(values[s])) for s in self.squares if len(values[s])>1)
        s = min(tmp, key=tmp.get)
        # n, s = ((len(values[s]), s) for s in self.squares if len(values[s])>1)
        return self._some(self._search(self._assign(values.copy(), s, d)) for d in values[s])

    def _assign(self, values, s, d):
        values_ = values[s].replace(d, '')
        if all(self._eliminate(values, s, d_) for d_ in values_):
            return values
        return False

    def _eliminate(self, values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')

        if len(values[s])==0:
            return False
        elif len(values[s])==1:
            d_ = values[s]
            if not all(self._eliminate(values, s_, d_) for s_ in self.peers[s]):
                return False
        
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces )==0:
                return False
            elif len(dplaces)==1:
                if not self._assign(values, dplaces[0], d):
                    return False

        return values

    def _some(self, seq):
        for e in seq:
            if e: 
                return e
        return False
