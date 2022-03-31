b ={}
while True:
    c = int(input())
    if c != 0:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    else:
        break
max_key = 0
for key, item in b.items():
    if key > max_key:
        max_key = key
        max_value = item
print(max_value)
