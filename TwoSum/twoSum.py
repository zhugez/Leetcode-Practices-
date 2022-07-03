# def numberst(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return i,j

# class Solution(object):
#     def twoSum(self,nums,target):
#         visit = dict()
#         for k,v in enumerate(nums):
#             if target-v in visit:
#                 return [visit[target-v],k]
#             visit[v]=k

class Solution(object):
    def twoSum(self,nums,target):
        visit = dict()
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in visit:
                return [visit[needed],i]
            # visit.setdefault(nums[i],i)
            visit[nums[i]]=i
target = 10
nums = [1,2,4,5,6,7,8]
s = Solution()
print(s.twoSum(nums, target))