class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans=[]
        arr=[(position[i],speed[i]) for i in range(len(speed))]
        arr.sort(reverse=True, key= lambda x: x[0])

        ans.append((target-arr[0][0])/arr[0][1])

        for i in range(1,len(arr)):
            time=(target-arr[i][0])/arr[i][1]
            if time<=ans[-1]:
                continue
            else:
                ans.append(time)


        return len(ans)