m1 = input()
m2 = input()
m3 = input()
m4 = input()
m5 = input()
matrix = [m1.split(' '), m2.split(' '), m3.split(' '), m4.split(' ') ,m5.split(' ')]
def print_hi(matrix):
    row = 0
    col = 0
    i = 0
    centerRow = 2
    centerCol = 2
    total = 0

    for row, x in enumerate(matrix):
        try:
            i = x.index('1')
            if i > centerCol:
                cr = i -centerCol
                total += cr
            if i < centerCol:
                cr = centerCol - i
                total += cr
            if row > centerRow:
                cc = row -centerRow
                total += cc
            if row < centerRow:
                cc = centerRow - row
                total += cc
            print(total)
        except:
            pass
if __name__ == '__main__':
    print_hi(matrix)

