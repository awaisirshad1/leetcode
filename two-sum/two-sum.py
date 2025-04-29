
    
from typing import List


def brute_force(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        temp = target - nums[i]
        for j in range(len(nums) - 1, i, -1):
            if temp - nums[j] == 0:
                return [i,j]
                
def optimized_solution(self, nums: List[int], target: int) -> List[int]:
    hm = {} # define empty hashmap
    for i in range(len(nums)):
        curr = nums[i] # current element
        comp = target - curr # complement of curr
        if comp in hm:
            return [hm[comp], i]
        hm[curr] = i
    return []


    