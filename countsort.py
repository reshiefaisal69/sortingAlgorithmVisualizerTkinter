import time


def count_sort(data, drawData, timeTick):
    max_element = int(max(data))
    min_element = int(min(data))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual and elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(data))]

    # Store count of each character
    for i in range(0, len(data)):
        count_arr[data[i] - min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual and position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
        # drawData(data, ['silver' if x == i or x == i + 1 else 'red' for x in range(len(data))])
        # time.sleep(timeTick)

    # Builds the output dataset array
    for i in range(len(data) - 1, -1, -1):
        output_arr[count_arr[data[i] - min_element] - 1] = data[i]
        count_arr[data[i] - min_element] -= 1

    # Copys the sorted dataset in output_arr to data
    for i in range(0, len(data)):
        data[i] = output_arr[i]
        drawData(data, ['purple' if x == i or x == i +
                 1 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
