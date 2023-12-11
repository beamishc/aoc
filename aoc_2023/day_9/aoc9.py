from icecream import ic
import numpy as np

def day_9_1(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')
        end_results = 0
        for line in lines:
            seqs = [[int(x) for x in line.split()]]
            while not all(v == 0 for v in seqs[-1]):
                seqs.append(list(np.diff(seqs[-1])))
            rev = seqs[::-1]
            for i, s in enumerate(seqs[::-1]):
                if i == 0:
                     s.append(0)
                else:
                    s.append(s[-1] + seqs[::-1][i-1][-1])
                if i == len(seqs)-1:
                    end_results += s[-1]
        ic(end_results)
            # ic(seqs)

ic(day_9_1('day_9/input.txt'))

def day_9_2(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')
        start_results = 0
        for line in lines:
            seqs = [[int(x) for x in line.split()]]
            while not all(v == 0 for v in seqs[-1]):
                seqs.append(list(np.diff(seqs[-1])))
            rev = seqs[::-1]
            for i, s in enumerate(rev):
                if i == 0:
                    rev[i] = [0] + s + [0]
                else:
                    rev[i] = [s[0] - rev[i-1][0]] + s + [s[-1] + rev[i-1][-1]]
                    # ic(rev[i])
                if i == len(seqs)-1:
                    start_results += rev[i][0]
            # ic(seqs)
        ic(start_results)

ic(day_9_2('day_9/input.txt'))
