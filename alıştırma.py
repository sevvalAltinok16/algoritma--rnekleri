n=10
def sumten(n):
    if n<1:
        return 0
    return n +sumten(n-1)

print(sumten(10))