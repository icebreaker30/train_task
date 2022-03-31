n = int(input())
events = []
for i in range(n):
    tinc, duration = map(int, input().split())
    events.append((tinc, 1))
    events.append((tinc+duration, -1))
events.sort()
online = 0
max_now = 0

for i in range(len(events)):
    if events[i][1] == 1:
        online += 1
    else:
        online -= 1
    max_now = max(max_now, online)
print(max_now)


