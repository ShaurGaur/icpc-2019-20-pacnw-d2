n_str, m_str = input().split(' ')

n = int(n_str)
m = int(m_str)

badwords = []
leet_plates = []
plates = []

for i in range(n):
    badwords.append(input())

for j in range(m):
    leet_plates.append(input())


leetcodes = ['O', 'L', 'Z', 'E', '4', 'S', 'B', 'T', 'B', '9']
digits = "0123456789"


# Unleetspeak the plates
for p in leet_plates:
    unleeted = ""
    for char in p:
        if char in digits:
            unleeted += leetcodes[int(char)]
        else:
            unleeted += char
    plates.append(unleeted)

for plate in plates:
    invalid = False
    for badword in badwords:
        if badword in plate:
            invalid = True
            print("INVALID")
            break
    if not invalid:
        print("VALID")