arr = [102, 434,33,45, 39, 10]

def selectionSort(arr):
    for i in range(len(arr)):
        current = arr[i] #102
        changed=False
        position = 0
        for j in range(i+1, len(arr)): #[434,33...]
            if(current>arr[j]):
                current = arr[j]
                changed = True
                position=j
        if changed:
            temp = arr[i]
            arr[i] = current
            arr[position]=temp
    return arr   

newArr = selectionSort(arr)
print(newArr)
            
         
