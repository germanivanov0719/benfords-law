import sys

with open(sys.argv[1], encoding='utf-8') as f:
    s = f.read()
    d = {}
    for p in range(101):
        d[p] = s.count(f' {p}%')

print(d)
print()
print(*(i[1] for i in d.items()))

