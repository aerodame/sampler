from three_sum import ThreeSum

s = ThreeSum()
test_array = [-47, -46, -38, -37, -33, -16, -13, -11, -4, -2, 2, 7, 17, 26, 33, 35, 39, 43, 46, 47]
target_sum = 0
ans = s.run(test_array, target_sum)
print(ans)