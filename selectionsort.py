import time

def selection_sort(data, drawData, timeTick):
    """
        This function takes three arguements a dataset, 
        a drawData function and a time for execution of each interval 
        and sorts the data using slection sort
    """
    for i in range(len(data)):
        x = i
        for j in range(i+1, len(data)):
            if data[x] > data[j]:
                x = j 
            drawData(data, ['silver' if j == i or j == i + 1 else 'red' for i in range(len(data))])
            time.sleep(timeTick) 
        data[i], data[x] = data[x], data[i]
        
