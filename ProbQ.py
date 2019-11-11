#from time import time


def op(x):
    if x % 2 == 0:
        return x//2
    else:
        return x+1


a_str, b_str = input().split(' ')

a = int(a_str)
b = int(b_str)

i = 0

'''
if a < b:
    i = b - a
else:
    while a != b:
        a = op(a)
        i += 1
'''

#t_i = time()
while a != b:
    if a > b:
        a = op(a)
        i += 1
    else:
        i += b - a
        break
#t_f = time()

print(i)
#print("time: {}".format(t_f-t_i))