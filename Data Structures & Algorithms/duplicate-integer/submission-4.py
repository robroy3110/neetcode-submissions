class Solution:
     def hasDuplicate(self, nums: List[int]) -> bool:
        backup = set(())
        for n in nums:
            if n in backup:
                return True
            backup.add(n)
        return False
        