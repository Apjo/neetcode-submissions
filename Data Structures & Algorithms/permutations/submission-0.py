class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(idx, buff, res):
            if idx == len(nums):
                print(f"reach eol at nums, adding buff={buff} to res!")
                res.append(nums[:])
                return
            #add element at idx
            # then for each of the remaining elements, perform swap amongst them
            # each swap will generate a new seq of elements of nums
            # add this finally to res upon reaching the end
            # repeat for each element in nums
            for i in range(idx, len(nums)):
                print(f"perform swap at i={i}, idx={idx}")
                nums[i], nums[idx] = nums[idx], nums[i]
                # if nums[i] in buff:
                    # print(f"nums[i]={nums[i]} in buff")
                    # continue
                # print(f"adding {nums[i]} to buff!")
                # buff.append(nums[i])
                print(f"recurse with idx={idx+1}")
                solve(idx+1, buff, res)
                
                # if buff:
                #     print(f"pop from buff")
                #     buff.pop()
                print(f"perform swap at i={i}, idx={idx}")
                nums[i], nums[idx] = nums[idx], nums[i]


        res,buff,idx=[],[],0
        solve(idx, buff, res)
        return res