class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        if not matrix or not matrix[0]:
            return False
        
        l=0
        r=(n*m)-1
        while l<=r:
            mid= (l+r)//2
            midValue= matrix[mid//m][mid%m]
            if midValue<target:
                l=mid+1
            elif midValue>target:
                r=mid-1
            else:
                return True

        return False