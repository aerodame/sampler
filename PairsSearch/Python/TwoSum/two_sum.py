class TwoSum:
    def run(self, nums: list[int], target: int) -> list[int]:
        print(f'nums:{nums} target:{target}')
        stride = 0
        count = 0
        while(stride < len(nums)-1):
            stride = stride + 1
            for i in range(len(nums)-stride):
                count = count + 1
                j = i+stride
                if (j < len(nums)):
                    sum = nums[i] + nums[j]
                    print(f'iter:{count} -> i:{i} j:{j} s:{stride}\t a[{i}] a[{j}] sum:{sum}')
                    if (sum) == target:
                        return [i, j]
        return [None, None]


