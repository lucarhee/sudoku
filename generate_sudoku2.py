base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c):
    return (base * (r % base) + r // base + c)%side
    # 이 식은 뭔가?

# randomize rows, columns and numbers (of valid base pattern)
from random import sample

def shuffle(s):
    return sample(s, len(s))

rBase = range(base)
rows  = [ g * base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g * base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))
# rows, cols, nums 다 셔플로 된 임의의 리스트.

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
# patterns()가 어떤 의미인지 모르겠다.

for line in board: print(line)

[6, 2, 5, 8, 4, 3, 7, 9, 1]
[7, 9, 1, 2, 6, 5, 4, 8, 3]
[4, 8, 3, 9, 7, 1, 6, 2, 5]
[8, 1, 4, 5, 9, 7, 2, 3, 6]
[2, 3, 6, 1, 8, 4, 9, 5, 7]
[9, 5, 7, 3, 2, 6, 8, 1, 4]
[5, 6, 9, 4, 3, 2, 1, 7, 8]
[3, 4, 2, 7, 1, 8, 5, 6, 9]
[1, 7, 8, 6, 5, 9, 3, 4, 2]
