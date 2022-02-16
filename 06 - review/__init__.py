T = int(input())
for i in range(0, T):
    S = str(input())
    even_char = ''
    odd_char = ''

    for j in range(0, len(S)):
        if j % 2 == 0:
            even_char += S[j]
        else:
            odd_char += S[j]

    print('{} {}'.format(even_char, odd_char))
