class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         In_set=set()
         for number in nums:
            if number in In_set:
                return True
            In_set.add(number)
         return False
    