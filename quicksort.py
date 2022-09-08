import time


def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(
                len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    # swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, timeTick):
    """
        this funtions takes five arguments
        data-> which is the dataset
        head-> the element a the begining of the Pivot
        tail-> the element at the of the pivot
        place-> which is the a array of the elements last individul digits to be sorted
        drawData-> the function that draws the bar graph and visualizes the data
        timeTick-> the time delay for each operation

        this funtion sorts the data using quick sort alogorithm
    """
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray
