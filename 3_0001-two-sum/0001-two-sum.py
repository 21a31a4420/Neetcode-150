class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i in range(len(nums)):
            e=target-nums[i]
            if e in l:
                return[i,l[e]]
            l[nums[i]]=i
        return []