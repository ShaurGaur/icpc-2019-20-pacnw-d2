


# D2: Team1 (Oregon State) ... team452


def smallest(l):
    r = 0
    for j in l:
        if j < r:
            r = j
    return r

def biggest(l):
    r = 0
    for j in l:
        if j > r:
            r = j
    return r

def to_dom(inds):
    return (smallest(inds), biggest(inds))

def in_dom(inie, outie):
    return outie[0] <= inie[0] and inie[1] <= outie[1]

def is_counted(inds):
    return inds.issubset(closed_subs)



rainbows = {'': 1}
closed_subs = list()

def is_rainbow(s):
    return len(set(s)) == len(s)


def n_rainbows(s, inds):
    try:
        return rainbows[s]
    except KeyError:
        if is_rainbow(s):
            rainbows[s] = 2**len(s)
            closed_subs.append(inds)
            return 2**len(s)
        else:
            x = 0
            for i in range(len(s)):
                next_inds = inds.difference({i})
                if not is_counted(next_inds):
                    closed_subs.append(next_inds)
                    x += n_rainbows(s[:i] + s[i+1:], next_inds)
            rainbows[s] = x
            return x


word = input()
print(n_rainbows(word, set(range(len(word)))))


