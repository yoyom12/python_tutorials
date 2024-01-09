
class solution:
    def twosum(self,arr, targt, N):
        
        rmain = 0
        for i in range(N):
            rmain = targt - arr[i]

            if(arr.find(rmain)):
                print(rmain)



ar = [1,2,3,4]
targt = 10
num = 4

obj = solution()
print(obj.twosum(ar,targt, num))