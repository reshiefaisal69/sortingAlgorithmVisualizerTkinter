import time


def merge_sort(data, drawData, timeTick):
    mer_sort_algo(data, 0, len(data)-1, drawData, timeTick)


def mer_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        mer_sort_algo(data, left, middle, drawData, timeTick)
        mer_sort_algo(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    lpart = data[left: middle+1]
    rpart = data[middle+1: right+1]

    leIdx = reIdx = 0

    for dataIdx in range(left, right+1):
        if leIdx < len(lpart) and reIdx < len(rpart):
            if lpart[leIdx] <= rpart[reIdx]:
                data[dataIdx] = lpart[leIdx]
                leIdx += 1
            else:
                data[dataIdx] = rpart[reIdx]
                reIdx += 1
        elif leIdx < len(lpart):
            data[dataIdx] = lpart[leIdx]
            leIdx += 1
        else:
            data[dataIdx] = rpart[reIdx]
            reIdx += 1
    drawData(data, ["green" if x >= left and x <=
             right else "purple" for x in range(len(data))])
    time.sleep(timeTick)


def getColorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("Blue")
        else:
            colorArray.append("purple")
    return colorArray
