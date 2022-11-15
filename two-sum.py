class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        idx_x=0
        for x in nums:            
            is_found=False
            if x<target:
                idx_y=0
                for y in nums:
                    if y<target and idx_x!=idx_y:
                        if x+y==target:
                            result.append(idx_x)
                            result.append(idx_y)
                            is_found=True
                            break
                    idx_y+=1
            idx_x+=1
            if is_found:
                break
        return result

if __name__=='__main__':
    two_sum=Solution()
    nums=[2,7,11,15]
    target=9
    result= two_sum.twoSum(nums,target)
    print(result)