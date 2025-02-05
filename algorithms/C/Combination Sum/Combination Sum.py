class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        path = []
        answer = []
        def dp(idx, total):
            if total == target:
                answer.append(path[:])
                return
            if total > target:
                return
            
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                dp(i, total + candidates[i])
                path.pop()
        
        dp(0, 0)
        return answer

