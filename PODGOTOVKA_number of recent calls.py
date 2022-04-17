class RecentCounter:

    def __init__(self):
        self.p = collections.deque()

    def ping(self, t):
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)

# What is from collections import deque in Python?
# Python's collections module provides a class called deque that's specially designed to provide
# fast and memory-efficient ways to append and pop item from both ends of the underlying data structure
# popleft() removes an element from the left side of the deque and returns the value