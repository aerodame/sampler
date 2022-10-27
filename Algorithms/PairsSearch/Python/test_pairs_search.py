from pairs_search import PairsSearch

def test_A():
    nums = [4, 5, 6, 8, 13, 14, 16, 18, 28, 29, 32, 37, 39, 41, 42, 46, 52, 56, 72, 73, 74, 75, 79, 80, 84, 86, 88, 89, 92, 93, 96, 97]
    sum = 42
    ans = ['(5,37)', '(13,29)', '(14,28)']
    ps = PairsSearch(nums, sum)
    assert  ps.run() == ans

def test_B():
    nums = [10, 14, 26, 38, 41, 59]
    sum = 16
    ans = [None]
    ps = PairsSearch(nums, sum)
    assert  ps.run() == ans

def test_C():
    nums = [2, 3, 11, 12, 14, 17, 18, 24, 43, 47, 55, 61]
    sum = 20
    ans = ['(2,18)', '(3,17)']
    ps = PairsSearch(nums, sum)
    assert  ps.run() == ans        