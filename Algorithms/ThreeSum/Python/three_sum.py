"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class ThreeSum:

    ## given a list of 3 integers, sort and return a tuple
    def __tuple_sort(self, triple: list[int]) -> tuple:
        return (0,1,2)

    def run(self, nums: list[int], target: int) -> list[list[int]]:
        print(f'nums:{nums} target:{target}')
        count = 0
        x = self.__tuple_sort([2,0,1])
        print(x)
        hits = set()
        none_found = True
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    xi = nums[i]
                    xj = nums[j]
                    xk = nums[k]
                    sum = xi + xj + xk
                    # print(f'iter:{count} -> i:{i} j:{j} k:{k} sum:{sum}')
                    if (sum == 0):
                        none_found = False
                        l = [xi, xj, xk]
                        l.sort()
                        sorted_tuples = tuple(l)
                        strTuples = f'({xi},{xj},{xk})'
                        hits.add(sorted_tuples)
                        # print(tuples)    
                    count = count + 1
        ans = []
        for i in hits:
            ans.append(list(i))  
        return sorted(ans)


