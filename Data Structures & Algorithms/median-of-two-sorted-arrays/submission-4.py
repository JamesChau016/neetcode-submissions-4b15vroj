class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            temp=nums1
            nums1=nums2
            nums2=temp

      
        m=len(nums1)
        n=len(nums2)
        half=(m+n+1)//2


        l=0
        r=m
        while l<=r:
            i=(l+r)//2
            j=half-i


            left1= nums1[i-1] if i!=0 else -math.inf
            right1= nums1[i] if i<m else math.inf
            left2= nums2[j-1] if j!=0 else -math.inf
            right2= nums2[j] if j<n else math.inf
            

            if left1>right2:
                r=i-1
            elif left2>right1: 
                l=i+1
            else:
                break
        
        if (m+n) %2!=0:
            res= max(left1,left2)
        else:
            res= (max(left1,left2)+min(right1,right2))/2

        return res


