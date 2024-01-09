

class solution:
    
    def subarrayString(self,arr, Num, s):
        

        x=0
        sum=0
        for i in range(Num):
            sum += arr[i]
            
            if sum>=s:
                while (x>i and sum >s):
                    sum-=arr[x]
                    x+=1
                if sum==1:
                    return [x+1,i+1]
            

arr = {1,2,3,7,5}
Num = 5
s = 12
obj = solution()
print(obj.subarrayString(arr,Num,s))