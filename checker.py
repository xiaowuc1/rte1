from dmoj.result import CheckerResult
from dmoj.executors import executors

import subprocess
from collections import defaultdict
from re import split as resplit

import math

def getNorm(n, y, L):
    rhs = []
    for _ in range(n):
        rhs.append(0.0)
    for i in range(n):
        # Ly component
        for j in L[i]:
            rhs[i] += y[j] * L[i][j]
    ret = 0.0
    for i in range(n):
        ret += y[i] * rhs[i]
    return math.sqrt(ret)

def getL(judge_input):
    # from the raw input
    n = int(judge_input[1].split()[0])
    m = int(judge_input[1].split()[2])
    wMat = []
    for _ in range(n):
        wMat.append(dict())
    for i in range(2, m+2):
        data = judge_input[i].split()
        u = int(data[0]) - 1
        v = int(data[1]) - 1
        w = float(data[2])
        wMat[u][v] = w
        wMat[v][u] = w
    L = []
    for _ in range(n):
        L.append(dict())
    for i in range(n):
        wDeg = 0.0
        for j in wMat[i]:
            wDeg += wMat[i][j]
            L[i][j] = -wMat[i][j]
        L[i][i] = wDeg
    return L

def check(process_output, judge_output, judge_input, point_value, execution_time, **kwargs):
    try:
        process_lines = process_output.decode("utf-8").split("\n")[:-1]
        judge_lines = judge_output.decode("utf-8").split("\n")[1:-1]
        judge_input = judge_input.decode("utf-8").split("\n")

        id = judge_input[0]
        n = int(judge_input[1].split()[0])

        assert n == len(process_lines), "wrong number of lines {}".format(len(process_lines))

        barx = [float(x) for x in judge_lines]
        try:
            x = [float(z) for z in process_lines]
        except:
            assert False, "illegal output"
        for y in x:
            assert not math.isnan(y), "nan detected"

        assert len(barx) == n, "barx has wrong length {}".format(len(barx))
        assert len(x) == n, "x has wrong length {}".format(len(x))

        L = getL(judge_input)
        xDiff = [x[i] - barx[i] for i in range(n)]

        xDiffNorm = getNorm(n, xDiff, L)
        xNorm = getNorm(n, barx, L)
        if xDiffNorm > 0.1 * xNorm:
            return CheckerResult(False, 0, "norm out of range: xNorm = {}, xDiffNorm = {}, ratio = {}".format(xNorm, xDiffNorm, xDiffNorm / xNorm))
        bestTime = 10.
        ratio = bestTime / execution_time
        return CheckerResult(True, point_value * ratio**2, "norm in range: xNorm = {}, xDiffNorm = {}, ratio = {}".format(xNorm, xDiffNorm, xDiffNorm / xNorm))
    except Exception as e:
        return CheckerResult(False, 0, "{}".format(e))
