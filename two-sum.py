class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        for x in nums:
            is_found=False
            if x<target:
                for y in nums:
                    if y<target:
                        if x+y==target:
                            result.append(nums.index(x))
                            result.append(nums.index(y))
                            is_found=True
                            break
            if is_found:
                break
        return result

if __name__=='__main__':
    two_sum=Solution()
    nums=[10,6,4,2,11,55,7,3,5,1,35]
    target=9
    result= two_sum.twoSum(nums,target)
    print(result)