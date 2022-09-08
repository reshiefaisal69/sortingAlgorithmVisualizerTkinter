import time


def insertion_sort(data, drawData, timeTick):

    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['green' if i == j or i == j +
                     1 else 'red' for i in range(len(data))])
            time.sleep(timeTick)
        data[j + 1] = key
