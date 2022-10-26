## Two Sum

## Algorithm
### Python3 Code
```python3
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        stride = 0
        while(stride < len(nums)-1):
            stride = stride + 1
            for i in range(len(nums)-stride):
                j = i+stride
                if (j < len(nums)):
                    sum = nums[i] + nums[j]
                    if (sum) == target:
                        return [i, j]
        return [None, None]
```
### LeetCode Results
```
Runtime: 160 ms, faster than 34.63% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 95.96% of Python3 online submissions for Two Sum.
```