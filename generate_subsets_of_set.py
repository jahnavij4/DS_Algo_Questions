class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.out=[]
        def sub(index,partial_sol):
            if index==len(nums):
                self.out.append(partial_sol)
                return 
            # Include
            partial_sol.append(nums[index])
            sub(index+1,partial_sol[:])
            partial_sol.pop()
            # Exclude
            sub(index+1,partial_sol[:])
        sub(0,[])
        return self.out
