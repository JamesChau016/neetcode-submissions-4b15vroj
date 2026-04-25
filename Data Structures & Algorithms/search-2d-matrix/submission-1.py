class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        row=0
        while row<n and not matrix[row][0]<=target<=matrix[row][m-1]:
            row+=1
        
        l=0
        r=m-1
        while row<n and l<=r:
            mid=(l+r)//2
            if matrix[row][mid]<target:
                l=mid+1
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                return True



        return False