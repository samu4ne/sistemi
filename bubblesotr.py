
arr= [9,2,5,4,8,6,7,1] #faccio un vettore
n = len(arr) #assegno ad n la dimensione di arr
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

print(arr)
