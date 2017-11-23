a = [1, 3, 5, 6, 9]
from collections import deque
def sum(item):
    head, *tail = item
    return head + sum(tail) if tail else head
print(sum(a))

conect = deque(maxlen=3)
for i in a:
    if i < 9:
        conect.appendleft(i)
print(conect.popleft())
print(conect)