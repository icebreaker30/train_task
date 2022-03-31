n = int(input())  # количество школьников
si = {input() for _ in range(int(input()))}  # языки первого школьника
s_union = si.copy()
s_intersec = si.copy()
for _ in range(1, n):
    si = {input() for _ in range(int(input()))}  # языки каждого школьника
    s_union = s_union | si
    s_intersec = s_intersec & si
print(len(s_intersec))  # знают все школьники
for lang in s_intersec:  # список таких языков
    print(lang)
print(len(s_union))  # знает хотя бы один
for lang in s_union:  # список таких языков
    print(lang)
