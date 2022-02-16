import sys

n = int(sys.stdin.readline().strip())

phonebook = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split(' ')
    phonebook[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    if query in phonebook:
        print(query+'='+phonebook[query])
    else:
        print('Not found')
    query = sys.stdin.readline().strip()
