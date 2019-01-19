
map = dict()
map[1000] = 'M'
map[900] = 'CM'
map[90] = 'XC'
map[9] = 'IX'
map[400] = 'CD'
map[40] = 'XL'
map[4] = 'IV'
map[500] = 'D'
map[100] = 'C'
map[50] = 'L'
map[10] = 'X'
map[5] = 'V'
map[1] = 'I'


def solve(n):
    i = 1000
    arr = []
    res = 0

    while i != 0:
        div = int(n // i)
        if div == 9 or div == 4:
            arr = arr + [map[div*i]]
            res = n - div*i
            i = i // 10
        if 9 > div >= 5:
            arr = arr + [map[5*i]]
            res = n - 5*i
        if div < 4:
            arr = arr + [map[i]] * div
            res = n - div * i
            i = i // 10

        n = res


    print(''.join(arr))

def solve1(data):
    A = ['....']
    B = ['....']
    C = ['....']
    D = ['....']

    return D[data/1000]+C[data%1000/100]+B[data%100/10]+A[data%10]


if __name__ == "__main__":
    solve(2)
