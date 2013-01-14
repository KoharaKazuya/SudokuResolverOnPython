import csv


# 数独の問題を記した csv ファイルを読み込む
def matrix():
    matrix = []
    with open('problem.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            matrix.append(list(map((lambda c: int(c)), row)))
    return matrix


# あるマスに入る数字を計算する
def solve_cell(matrix, x, y):
    if matrix[y][x] != 0:
        return None
    possible = [x for x in range(1, 10)]
    # 行の調査
    row = matrix[y]
    for other in row:
        if other in possible:
            possible.remove(other)
    # 列の調査
    for row in matrix:
        other = row[x]
        if other in possible:
            possible.remove(other)
    # ブロックの調査
    block_x = int(x / 3)
    block_y = int(y / 3)
    for row in matrix[block_y * 3:block_y * 3 + 3]:
        for other in row[block_x * 3:block_x * 3 + 3]:
            if other in possible:
                possible.remove(other)
    return possible[0] if len(possible) == 1 else None


def solve():
    m = matrix()
    changed = True
    while changed:
        changed = False
        for y in range(0, 9):
            for x in range(0, 9):
                s = solve_cell(m, x, y)
                if s:
                    m[y][x] = s
                    changed = True
    print(m)


solve()
