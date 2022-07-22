


def part(arr,start,end):
    i = start
    j = end
    pivloc = i
    while True:
        while (arr[pivloc] < arr[j]) and (pivloc is not j):
            j = j - 1
            
            if j == i:
                return pivloc
            
            
            if j == i:
                break
            elif arr[pivloc] >= arr[j]:
                temp = arr[pivloc]
                arr[pivloc] = arr[j]
                arr[j] = temp
                pivloc = j
            
        while (arr[pivloc] > arr[i]) and (pivloc is not i):
            i = i + 1
            
            if j == i:
                return pivloc
            
        if j == i:
            break
        elif arr[pivloc] >= arr[i]:
            temp = arr[pivloc]
            arr[pivloc] = arr[i]
            arr[i] = temp
            pivloc = i
        

            
        if j == i:
            break
        
    
            
            
ar = [50,20,60,10,30,40]
part(ar,0,5)
print(ar)
        
        
    
    
