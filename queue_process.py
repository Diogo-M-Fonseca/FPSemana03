import collections

pl = input()
words = pl.split()
queue = collections.deque()
for i in words:
    queue.appendleft(i)
print(queue)

for word in words:
    if "o" in word:
        print(word)