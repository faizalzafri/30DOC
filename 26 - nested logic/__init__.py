returns = list(map(int, input().strip().split(" ")))
rd, rm, ry = returns
dues = list(map(int, input().strip().split(" ")))
dd, dm, dy = dues

fine = 0

if ry > dy:
    fine = 10000
elif ry == dy:
    if rm > dm:
        fine = 500 * (rm - dm)
    elif rm == dm and rd > dd:
        fine = 15 * (rd - dd)

print(fine)
