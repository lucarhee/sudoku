#  수도쿠를 만드는 방법은
#  http://parkjuwan.dothome.co.kr/wordpress/2019/04/19/make-simple-sudoku/
#  을 참고하였다.


# TODO: 컴퓨터가 풀게 한다.
# TODO: 사람이 풀 수 있게 만들어 본다.
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

def turnClockwise(s):
    # TODO: 45도 회전을 구현해야 한다.
    # XXX: 행렬 변환으로 가능한가?
    # XXX: 아니면 i, j로 해야 하나?
    for i in range(9):
        for j in range(9):
            s[i][j] = s[j][i]
    return s

# TODO: 아래의 4개 변환을 구현한다.
# TODO: 각종 조합을 자동으로 한다.
def randomize(s):
    """
    * h=horizontal(0), v=vertical(1)
    * 가로, 세로 모두 (0,1,2) (3,4,5) (6,7,8) 내에서는 한 줄 전체를 바꿔줄 수 있다. -- exchange_lines(m, n, rows=0, hv=0)
    * 가로, 세로 모두 (0,1,2) (3,4,5) (6,7,8)의 세 묶음 전체를 바꿔줄 수 있다. -- exchange_3lines(m, n, hv=0)
    * 같은 숫자끼리 바꿔줄 수 있다. -- exchange(m, n)
    * 시계 방향으로 돌려줄 수 있다. -- clockwise()
    """
    pass


# TODO: 빈칸을 만들어 문제를 낸다.
def generateSudoku(s):
    """
    몇몇 빈칸을 생성하여 문제를 만든다.
    """
    pass


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

if __name__ == '__main__':
    s = initSudoku()
    printSudoku(s)
    print()
    printSudoku(turnClockwise(s))
