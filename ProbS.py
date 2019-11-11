#from time import time

l = int(input())

times = []
distances = []
maximum = 0

for i in range(l):
    t_str, d_str = input().split(' ')
    t = int(t_str)
    d = int(d_str)
    times.append(t)
    distances.append(d)
    if i > 0:
        s = (distances[i] - distances[i - 1]) / (times[i] - times[i - 1])
        if s > maximum:
            maximum = s

print(int(maximum))

#t_f = time()
#print("time: {}".format(t_f - t_i))