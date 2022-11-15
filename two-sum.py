from datetime import datetime

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        result=[]
        d_nums={}
        i=0
        for x in nums:
            if (x < target):
                d_nums[i]=x
            i+=1

        half_of_target=round(target/2)
        
        arr_right={}
        arr_left={}

        for index in d_nums:
            if d_nums[index]>half_of_target:
                arr_right[index]=d_nums[index]
            else:
                arr_left[index]=d_nums[index]
                
        is_found=False
        for r in arr_right:
            for l in arr_left:
                if (target-arr_right[r])==arr_left[l]:
                    result.append(l)
                    result.append(r)
                    is_found=True
                    break
            if is_found:
                break

        return result

if __name__=='__main__':
    start_time=datetime.now()
    two_sum=Solution()
    result= two_sum.twoSum([2,7,11,15],9)
    end_time=datetime.now()
    print(result)
    elapsed_time=end_time-start_time
    print('Execution time is '+str(elapsed_time)+' seconds')