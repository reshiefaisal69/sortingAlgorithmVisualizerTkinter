import time
# Using counting sort to sort the elements in the basis of significant places
def countingSort(data, place,drawData, timeTick):
    """
        this funtions takes four arguments
        data-> which is the dataset
        place-> which is the a array of the elements last individul digits to be sorted
        drawData-> the function that draws the bar graph and visualizes the data
        timeTick-> the time delay for each operation
        
        this function returns the sorted element using the counting sort algorithm
    """
    size = len(data)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = data[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = data[i] // place
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        data[i] = output[i]
        drawData(data, ['purple' if x == i or x == i + 1 else 'red' for x in range(len(data))])
        time.sleep(timeTick)


# Main function to implement radix sort
def radix_sort(data, drawData, timeTick):
    """
        this funtions takes three arguments
        data-> which is the dataset
        drawData-> the function that draws the bar graph and visualizes the data
        timeTick-> the time delay for each operation

        this function find the last digit of the elements of the data and pass them to the count sort funtion to be sorted.
    """
    # Get maximum element
    max_element = max(data)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(data, place, drawData, timeTick)
        place *= 10