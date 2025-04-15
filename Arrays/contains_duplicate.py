class Solutions:
    def hasDuplicate(self, nums: list[int]) -> bool:
        dset = set(nums)
        return len(dset) != len(nums)
    

sol = Solutions()
print(sol.hasDuplicate([])) 