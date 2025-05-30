class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        nums.sort()

        for index , val in enumerate(nums):
            if index>0 and val==nums[index-1]:
                continue
            left= (index+1)
            right=(len(nums)-1)
            while left< right:
                currentSum = val+ nums[left]+ nums[right]
                if currentSum >0:
                    right -= 1
                elif currentSum< 0:
                    left +=1
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left +=1

                    while (left<right) and (nums[left]==nums[left-1]):
                        left +=1

        return triplets        

        