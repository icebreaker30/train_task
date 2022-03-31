n,s = list(map(int,input().split()))
if s >= n:
    print('INF')
bar =[]
for i in range(n):
    time = int(input())
    bar.append(time)
bar.sort()
bar_set = set(bar)
if len(bar) - len(bar_set) >= s:
    print('IMPOSSIBLE')
online = 0
max_time = 0
l = 0
r = 0
for b in bar:
    online += 1
     # s - 1 пока не понятно до конца - вроде работает на тестовых данных но хз. Смысл в том, чтобы на границах было без пересечений
    if online > s - 1:
        time = bar[r] - bar[l]
        max_time = max(max_time, time)
        online -= 1
        l += 1
    r += 1

print(max_time)
