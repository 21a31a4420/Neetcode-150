class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            t=numbers[l]+numbers[r]
            if target == t:
                return [l+1,r+1]
            elif target>t:
                l+=1
            else:
                r-=1
            