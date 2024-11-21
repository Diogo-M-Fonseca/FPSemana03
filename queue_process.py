import collections

pl = input()
words = pl.split()
queue = collections.deque(words)
print(queue)
while queue:
    word = queue.popleft()
    if "o" in word:
        print(word)