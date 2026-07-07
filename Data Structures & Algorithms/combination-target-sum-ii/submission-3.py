class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(idx, target, res, buff):
            if target == 0:
                # res.add(tuple(buff[:]))
                res.append(buff[:])
                return
            if target < 0 or idx >= len(candidates):
                return
            
            # else:
                # for i in range(idx, len(candidates)):
                    # if i > idx and candidates[i] == candidates[i - 1]:
                        # continue
            buff.append(candidates[idx])
            solve(idx + 1, target - candidates[idx], res, buff)
            buff.pop()
                # if target - candidates[i] < 0:
                #     break
            # skip duplicates for this candidates[idx]
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx+=1
            solve(idx + 1, target, res, buff)

        res,buff,idx=[],[], 0
        candidates.sort()
        solve(idx, target, res, buff)
        # temp = [list(t) for t in res]
        # return temp
        return res