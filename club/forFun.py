# Find the first 10 triangle numbers that equal square numbers.

def triangle(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

def findCommon():
    arr = []
    si = 2
    ti = 2
    s = si*si
    t = 1 + ti
    while len(arr) < 10:
        while t != s:
            if t < s:
                ti += 1
                t += ti
            if s < t:
                si += 1
                s = si*si
        # arr.append((t,ti,si))
        arr.append(t)
        ti += 1
        si += 1
        s = si*si
        t += ti
    return arr

f = findCommon()
for i in f:
    print(i)
