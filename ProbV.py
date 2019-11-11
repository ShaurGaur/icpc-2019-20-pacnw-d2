



alpha = input()
word = input()

mistakes = []

for a in alpha:
    for i in range(len(word)+1):
        q = list(word)
        q.insert(i, a)
        r = ''.join(q)
        if r not in mistakes:
            mistakes.append(r)

for j in range(len(word)):
    q = word[:j]+word[j+1:]
    if q not in mistakes:
        mistakes.append(q)

for i in range(len(word)):
    for a in alpha:
        if word[i] == a:
            continue
        x = list(word)
        x[i] = a
        q = ''.join(x)
        if q not in mistakes:
            mistakes.append(q)

mistakes.sort()

for mistake in mistakes:
    print(mistake)

