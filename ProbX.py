word = input().replace(' ','').replace(',','').replace('.','').upper()
counts = {word[0]:1}

for i in range(len(word) - 1):
    if word[i+1] not in counts.keys():
        counts[word[i+1]] = 1
    elif word[i+1] in counts.keys():
        for j in counts.keys():
            if word[i+1] == j:
                counts[j] = counts[j] + 1

raw_counts = [v for v in counts.values()]
sorted_counts = sorted(raw_counts)

fibonacci = {0: 1, 1: 2, 2: 3, 3: 5, 4: 8, 5: 13}
weights = []
for i in range(min(len(sorted_counts),6)):
    for j in range(fibonacci[i]):
        weights.append(2 * i + 1)

sum = 3 * (len(word) - 1)
for i in range(len(sorted_counts)):
    j = sorted_counts[len(sorted_counts) - 1 - i] * weights[i]
    sum += j

print(sum)