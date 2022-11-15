import time

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        result=[]
        d_nums=[]
        i=0
        for x in nums:
            d_nums.append({i:x,'is_excluded':(True if x >= target else False)})
            i+=1

        # d_nums[:]=

        return result

if __name__=='__main__':
    start_time=time.time()
    two_sum=Solution()
    result= two_sum.twoSum([2,11,15,7],9)
    end_time=time.time()
    print((start_time-end_time))
    print(result)