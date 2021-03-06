import math

def _rot(n, x, y, rx, ry):
    if (rx == 1):
        x = n - 1 - x
        y = n - 1 - y
    return y,x


class HilbertCurve:
    def __init__(self, sz):
        self.sz = sz
        self.degree = int(math.ceil(math.log(self.sz,4)))
        self.n = 2**self.degree
        all = self.n**2
        half = int(all / 2)
        quarter = int(all / 4)
        eighth = int(all / 8)
        req = quarter*int((self.sz+quarter-1)/quarter)
        sub = int(req / quarter)
        assert sub != 1
        if sub == 2:
            self.start = quarter
        else:
            self.start = half - int(sz / 2)
        self.end = self.start + self.sz
        self.height = self.n - min([y for x,y in [self._d_to_xy(i) for i in self.range()]])
        self.width = max([x for x,y in [self._d_to_xy(i) for i in self.range()]]) + 1

    def _d_to_xy(self, d):
        d += self.start
        x = y = 0
        s = 1;
        while s < self.n:
            rx = int(d / 2) & 1
            ry = (d ^ rx) & 1
            if ry == 0:
                x,y = _rot(s, x, y, rx, ry)
            else:
                y += s * ry
            x += s * rx
            s *= 2
            d >>= 2
        return x, y

    def range(self):
        return range(self.sz)

    def __getitem__(self, key):
        if not type(key) == int or key < 0 or key >= (self.end - self.start):
            raise Exception("invalid index")
        x,y = self._d_to_xy(key)
        return x, y - (self.n - self.height)

def _coords(n):
    h = HilbertCurve(n)
    return [h._d_to_xy(d) for d in range(n**2)]

def compact(n):
    assert type(n) == int and n >= 2 and n & (n - 1) == 0
    c = _coords(n)
    assert len(c) == n**2
    for x in range(int(n**2/4),n**2+1,2):
        assert (x & 1) == 0
        f = int(n**2 / 2 - x / 2)
        t = int(n**2 / 2 + x / 2)
        minx = min([e[0] for e in c[f:t]])
        miny = min([e[1] for e in c[f:t]])
        maxx = max([e[0] for e in c[f:t]])
        maxy = max([e[1] for e in c[f:t]])
        if (maxx - minx + 1) * (maxy - miny + 1) == t - f:
            print("yes",t-f,n,f,t,minx,miny,maxx,maxy)
