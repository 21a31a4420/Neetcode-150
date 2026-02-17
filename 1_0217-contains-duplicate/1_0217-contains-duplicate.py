class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        l=set(nums)
        m=len(l)
        return m!=n
