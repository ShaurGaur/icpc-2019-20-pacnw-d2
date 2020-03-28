#from time import time

class Board:
    def __init__(self, n):
        self.rows = []
        self.size = n

    def load_row(self, row):
        self.rows.append(row)

    def get_col(self, n):
        col = ""
        for row in self.rows:
            col += row[n]
        return col


def is_balanced(squares):
    n_w = 0
    n_b = 0
    for sq in squares:
        if sq == 'W':
            n_w += 1
        elif sq == 'B':
            n_b += 1
    return n_w == n_b


def has_cons(squares):
    last = ''
    last2 = ''
    for sq in squares:
        if sq == last and sq == last2:
            return True
        last2 = last
        last = sq
    return False


# ---- MAIN ----

n = int(input())
board = Board(n)



for i in range(n):
    board.load_row(input())

#t_i = time()

for j in range(n):
    col = board.get_col(j)
    row = board.rows[j]
    if has_cons(col):
        print(0)
        #print("time {}".format(time() - t_i))
        exit()
    if has_cons(row):
        print(0)
        #print("time {}".format(time() - t_i))
        exit()
    if not is_balanced(col):
        print(0)
        #print("time {}".format(time() - t_i))
        exit()
    if not is_balanced(row):
        print(0)
        #print("time {}".format(time() - t_i))
        exit()

#t_f = time()

#print("time {}".format(time()-t_i))
print(1)