import re
import pandas as pd

df = pd.read_fwf('pcrfif.txt')
(rows, column) = df.shape


def rFind(gotcha):
    rlist = []
    for r in range(0, rows):
        if isinstance(df.values[r, 0], str):
            ds = df.values[r, 0]
            m1 = re.search(gotcha, ds)
            if m1:
                found = m1.group(0)
                rlist.append(r)
    return rlist
