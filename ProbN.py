#from time import time

r_str, c_str, a_str, b_str = input().split(' ')
r = int(r_str)
c = int(c_str)
a = int(a_str)
b = int(b_str)

a_is = []
b_is = []

for i in range(a):
    a_i = int(input())
    a_is.append(a_i)

for i in range(b):
    b_i = int(input())
    b_is.append(b_i)

#t_i = time()
for r in range(a):
    for i in range(a_is[r]):
        for c in range(b):
            for j in range(b_is[c]):
                if (r + c) % 2 == 0:
                    print('B',end='')
                else:
                    print('W',end='')
        print()

#t_f = time()
#print("time: {}".format(t_f - t_i))
