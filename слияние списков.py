list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))


def merge(A, B):
    i = 0
    j = 0
    list3 = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            list3.append(A[i])
            i += 1
        else:
            list3.append(B[j])
            j += 1
    list3 += A[i:]
    list3 += B[j:]
    return list3


print(*merge(list1, list2))
