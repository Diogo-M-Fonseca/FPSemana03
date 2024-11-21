import collections

pl = input()
ppl= pl.split()
num = list(map(int, ppl))
stack = collections.deque(num)
print(stack)
while stack:
    num = stack.pop()
    print(num ** 2)

    