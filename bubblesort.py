import time


def bubble_sort(data, drawData, timeTick):
    temp = data
    for _ in range(len(data)-1):
        if sorted(temp) == data:
            break
        else:
            for j in range(len(data)-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j +
                         1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
