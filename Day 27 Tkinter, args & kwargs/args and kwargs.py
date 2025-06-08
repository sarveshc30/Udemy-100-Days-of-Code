def add(*args):
    op = 0
    for i in args:
        op += i
    return op

print(add(1,2,3,4,5))
