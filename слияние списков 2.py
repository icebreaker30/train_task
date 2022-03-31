from heapq import merge
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(list(merge(list1, list2)))