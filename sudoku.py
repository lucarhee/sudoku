#  https://blog.0xf.kr/2020/05/02/%EC%8A%A4%EB%8F%84%EC%BF%A0-%EC%88%98%ED%95%99-1/
#  수도쿠의 경우의 수는? 6,670,903,752,021,072,936,960
#  수도쿠는 최소 17개의 힌트가 있어야 유일한 해답을 갖는다.
#  위의 것을 줄이는 방법까지 잘 설명되어 있다. 읽어보면 재미있다.
#  경우의 수를 구하는 데 몇 백년 ... 몇 천년 단위다... ㅋㅋㅋㅋ


#  수도쿠를 만드는 것을 정말 단순하게 봤는데
#  수도쿠 문제를 만드는 것부터
#  푸는 알고리즘을 만드는 것까지
#  (wikipedia 수도쿠 푸는 방법 번역하기 - https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)
#  쉬운게 없네.



#  수도쿠를 만드는 방법은
#  http://parkjuwan.dothome.co.kr/wordpress/2019/04/19/make-simple-sudoku/
#  을 참고하였다.


# TODO: 컴퓨터가 풀게 한다.
# TODO: 사람이 풀 수 있게 만들어 본다. (ncurses)
# TODO: 옵션을 달 수 있도록 만든다.

import random


def initSudoku():
    """
    수도쿠 기본형을 만든다.
    """
    sudoku = []

    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(0)
        sudoku.append(temp)

    """
    수도쿠 만드는 방법
    1. 한 줄의 배열을 채운다.
    2. 바로 위 칸의 수가 7이상일 경우 6을 뺀 값을, 아닐 경우 3을 더한 값을 넣는다.
    3. 3번째 줄까지 채워간다.
    4. 나머지 줄은 그 줄의 위로 3번째 줄에서 그 값이 9이면 1을 입력하고, 아니면 +1 값을 넣는다.

    이렇게 만들어진 수도쿠를 여러 방법으로 편집할 수 있다.
    TODO: 아래 3 경우는 구현하지 않음
    * 가로, 세로 모두 (0,1,2) (3,4,5) (6,7,8) 내에서는 한 줄 전체를 바꿔줄 수 있다.
    * 가로, 세로 모두 (0,1,2) (3,4,5) (6,7,8)의 세 묶음 전체를 바꿔줄 수 있다.
    * 같은 숫자끼리 바꿔줄 수 있다.
    """

    numbers = [n for n in range(1, 10)]

    for i in range(9):
        for j in range(9):
            if i == 0:
                sudoku[0][j] = numbers[j]
            elif i < 3:
                if sudoku[i-1][j] >= 7:
                    sudoku[i][j] = sudoku[i-1][j] - 6
                else:
                    sudoku[i][j] = sudoku[i-1][j] + 3
            else:
                if sudoku[i-3][j] == 9:
                    sudoku[i][j] = 1
                else:
                    sudoku[i][j] = sudoku[i-3][j] + 1

    return sudoku


def getColumns(s, reverse=True):
    columns = []
    for i in range(9):
        column = []
        for j in range(9):
            column.append(s[j][i])
        if reverse:
            column.reverse()
        columns.append(column)
    return columns


def turnClockwise(s):
    times = random.randint(0, 3)
    for n in range(times):
        s = getColumns(s)

    print(f"{times}번 회전했어요.....")
    return s


def exchange(s):
    """두 숫자를 서로 바꿔 준다"""

    times = random.randint(0, 100)
    for n in range(times):
        numbers = [n for n in range(1, 10)]
        m = random.choice(numbers)
        numbers.remove(m)
        n = random.choice(numbers)

        for i in range(9):
            for j in range(9):
                if s[i][j] == m:
                    s[i][j] = n
                elif s[i][j] == n:
                    s[i][j] = m
        print(f"{m}와 {n}을 서로 바꿨습니다....")
    print(f"{times}번 숫자의 위치를 바꿨어요.....")
    return s


def exchangeColumns(s):
    """세로 뭉치(3줄)을 서로 바꾼다
    0, 1
    0, 2
    1, 2
    3가지 경우의 수 밖에 없다
    """
    cases = ((0, 1), (0, 2), (1, 2))
    m, n = random.choice(cases)

    s = getColumns(s, reverse=False)

    cols0 = s[:3]
    cols1 = s[3:6]
    cols2 = s[6:]

    s = [cols0, cols1, cols2]

    s[m], s[n] = s[n], s[m]

    temp = s
    s = []
    for i in range(3):
        s.extend(temp[i])

    s = getColumns(s, reverse=False)
    print(f"{m}번째 세로줄 뭉치와 {n}번째 세로줄 뭉치를 바꿨어요....")

    return s


def exchangeRows(s):
    """가로 뭉치(3줄)을 서로 바꾼다"""
    cases = ((0, 1), (0, 2), (1, 2))
    m, n = random.choice(cases)

    rows0 = s[:3]
    rows1 = s[3:6]
    rows2 = s[6:]

    s = [rows0, rows1, rows2]

    s[m], s[n] = s[n], s[m]

    temp = s
    s = []
    for i in range(3):
        s.extend(temp[i])

    print(f"{m}번째 가로줄 뭉치와 {n}번째 가로줄 뭉치를 바꿨어요....")

    return s


def exchangeColumnLines(s):
    """같은 줄 뭉치 안의 세로 줄을 서로 바꾼다"""

    numbers = (0, 3, 6)
    cases = ((0, 1), (0, 2), (1, 2))
    cols = random.choice(numbers)
    m, n = random.choice(cases)

    s = getColumns(s, reverse=False)
    s[m+cols], s[n+cols] = s[n+cols], s[m+cols]
    s = getColumns(s, reverse=False)

    print(f"{m+cols}번째 줄과 {n+cols}번째 줄을 바꿨어요....")
    return s


def exchangeRowLines(s):
    """같은 줄 뭉치 안의 가로 줄을 서로 바꾼다"""

    numbers = (0, 3, 6)
    cases = ((0, 1), (0, 2), (1, 2))
    rows = random.choice(numbers) # 바꿀 줄 뭉치
    m, n = random.choice(cases)

    s[m+rows], s[n+rows] = s[n+rows], s[m+rows]

    print(f"{m+rows}번째 줄과 {n+rows}번째 줄을 바꿨어요....")
    return s

def randomize(s):
    """
    * h=horizontal(0), v=vertical(1)
    * 가로, 세로 모두 (0,1,2) (3,4,5) (6,7,8) 내에서는 한 줄 전체를 바꿔줄 수 있다. -- exchange_lines(m, n, rows=0, hv=0)
    * 가로, 세로 모두 (0,1,2) (3,4,5) (6,7,8)의 세 묶음 전체를 바꿔줄 수 있다. -- exchange_3lines(m, n, hv=0)
    * 같은 숫자끼리 바꿔줄 수 있다. -- exchange(m, n)
    * 시계 방향으로 돌려줄 수 있다. -- turnClosewise()
    """

    s = turnClockwise(s)
    s = exchange(s)
    s = exchangeRows(s)
    s = exchangeColumns(s)
    s = exchangeRowLines(s)
    s = exchangeColumnLines(s)

    return s


# TODO: 빈칸을 만들어 문제를 낸다.
def generateSudoku(s):
    """
    몇몇 빈칸을 생성하여 문제를 만든다.
    17개 이상 남기는 것으로 한다.
    """

    MAX = 64
    deleted = 0
    for i in range(9):
        for j in range(9):
            D = random.choice((True, False))

            if deleted < 64:
                if D:
                    s[i][j] = '.'
                    deleted += 1
            else:
                break
    return s

def printSudoku(s):
    print(" -------" * 3)
    for i in range(9):
        print('| ', end='')
        for j in range(9):
            if j % 3 == 2:
                print(f'{s[i][j]} ', end='| ')
            else:
                print(f'{s[i][j]} ', end='')
        if i % 3 == 2:
            print()
            print(" -------" * 3)
        else:
            print('')

def solver(s):
    # 가장 윗 줄부터 채워나간다.
    # 각 칸에 올 수 있는 수의 조합을 기억한다
    # checkRow
    # checkCell
    # checkColumn
    # 이걸 반복하면 되지 않을까?




if __name__ == '__main__':
    import copy
    # make a sudoku
    s = initSudoku() # 수도쿠 기본형을 만듬
    solution = copy.deepcopy(randomize(s)) # 모두 채워진 수도쿠를 만듬
    printSudoku(solution)
    problem = copy.deepcopy(generateSudoku(solution)) # 17개 이상의 숫자만 남기고 문제를 만듬
    printSudoku(problem)
    #  if solver(problem):
        #  printSudoku(problem)
        #  # 풀이 통계를 보여줌
        #  # 걸린 시간
        #  # 문제의 난이도
        #  printSudoku(solution)
