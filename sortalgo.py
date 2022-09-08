# sorting algorithm visualizer

from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from mergesort import merge_sort
from quicksort import quick_sort
from selectionsort import selection_sort
from insertionsort import insertion_sort
from countsort import count_sort
from radixsort import radix_sort

# iniliazing tkinter to form a basic black window
root = Tk()
root.title("Sorting Algorith Visualisation")
root.maxsize(900, 600)
root.config(bg='black')

#varaibles and functions
selected_alg = StringVar()
data = []


def drawData(data, colourArray):
    """
        this function takes a random dataset, normalises it and drwas it on the canvas.
    """
    canvas.delete('all')
    c_height = 380
    c_width = 900
    x_width = c_width / (len(data)+4)
    offset = 30
    spacing = 10
    normaliseData = [i / max(data) for i in data]

    for i, height in enumerate(normaliseData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 360

        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colourArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

        root.update_idletasks()


def Generate():
    """
        this function generats a random data set and passes it as agruement to the drawdata function.
    """
    global data

    minVal = int(minScale.get())
    maxVal = int(maxScale.get())
    size = int(sizeScale.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal))

    # ['red''red'],........pasing this array
    drawData(data, ['red' for x in range(len(data))])


def Startalgo():
    """
        Get the results chosen from user and Starts relevent algorithm for sorting process
    """
    global data
    if algMenu.get() == "Bubble Sort":
        bubble_sort(data, drawData, speedScale.get())
    elif algMenu.get() == "Merge Sort":
        merge_sort(data, drawData, speedScale.get())
    elif algMenu.get() == "Quick Sort":
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    elif algMenu.get() == "Insertion Sort":
        insertion_sort(data, drawData, speedScale.get())
    elif algMenu.get() == "Selection Sort":
        selection_sort(data, drawData, speedScale.get())
    elif algMenu.get() == "Count Sort":
        count_sort(data, drawData, speedScale.get())
    elif algMenu.get() == "Radix Sort":
        radix_sort(data, drawData, speedScale.get())
    drawData(data, ['green' for x in range(len(data))])

# creating the ui frame/base format


ui_frame = Frame(root, width=900, height=200, bg='grey')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

# creating the cavas to draw

canvas = Canvas(root, width=900, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# creating a user interface
# Row 0
Label(ui_frame, text='Algorithm', bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(ui_frame, textvariable=selected_alg, values=[
                       'Count Sort', 'Radix Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Bubble Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(ui_frame, from_=0.1, to=3.0, length=200, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Speed[s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(ui_frame, text='Start The Sorting!', command=Startalgo,
       bg='red').grid(row=0, column=4, padx=5, pady=5)


# Row 1
minScale = Scale(ui_frame, from_=1, to=10000, length=200, digits=2,
                 resolution=0.2, orient=HORIZONTAL, label="Select min value")
minScale.grid(row=1, column=0, padx=5, pady=5)

maxScale = Scale(ui_frame, from_=10, to=10000, length=200, digits=2,
                 resolution=0.2, orient=HORIZONTAL, label="Select max value")
maxScale.grid(row=1, column=1, padx=5, pady=5)

sizeScale = Scale(ui_frame, from_=4, to=30, length=200, digits=2,
                  resolution=0.2, orient=HORIZONTAL, label="Select size of dataset")
sizeScale.grid(row=1, column=2, padx=5, pady=5)

Button(ui_frame, text='Generate new data set', command=Generate,
       bg='blue').grid(row=0, column=3, padx=5, pady=5)


root.mainloop()
