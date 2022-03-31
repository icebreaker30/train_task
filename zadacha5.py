n = int(input())
all_pos = set(range(1, n+1))
while True:
    beatrice = input().split()
    if beatrice[0] == 'HELP':
        break
    beatrice = set(map(int, beatrice))
    august = input()
    if august == 'YES':
        all_pos &= beatrice
    else:
        all_pos -= beatrice
print(*sorted(all_pos))
