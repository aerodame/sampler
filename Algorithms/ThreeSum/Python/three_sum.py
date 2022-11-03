"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class ThreeSum:
    def run(self, nums: list[int], target: int) -> list[list[int]]:
        print(f'nums:{nums} target:{target}')
        count = 0
        hits = []
        none_found = True
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    # print(f'iter:{count} -> i:{i} j:{j} k:{k} sum:{sum}')
                    if (sum == 0):
                        none_found = False
                        triples = [nums[i],nums[j],nums[k]]
                        strTriples = f'({nums[i]},{nums[j]},{nums[k]})'
                        hits.append(triples)
                        # print(triples)    
                    count = count + 1
        return hits

        


