n = int(input())
max_pos = set(range(1, n+1))
while True:
    beat = list(input().split())
    if beat[0] == "HELP":
        break
    else:
        avg = input()
        beat = set(map(int,beat))
        if avg =='YES':
            max_pos &= beat
        elif avg =='NO':
            max_pos =max_pos - beat
print(*max_pos)
