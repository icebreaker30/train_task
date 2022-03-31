import sys
text = sys.stdin.read()
x = list(text.split())
x = set(x)
print(len(x))

