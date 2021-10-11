# img_viewer.py

import PySimpleGUI as sg
from sympy import *

rows = 3
cols = 3

def buildLayout(rows,cols):

    colWidth = 200
    colHeight = 300

    file_list_column = [    [
            sg.Text("Select Matrix Calculation", font = '20')
        ],
        [
            sg.Text("Rows: "), sg.In(size = (3,0)), sg.Text("Columns: "), sg.In(size = (3,0))
        ],
        [sg.OK()]
    ]
    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [sg.Text("Fill in the matrix")]
    ]


    for _ in range(rows):
        temp = []
        for _ in range(cols):
            temp.append(sg.InputText(size = (3,0)))
        image_viewer_column.append(list(temp))

    image_viewer_column.append([sg.Button("SOLVE",size=(25, 1), pad=(0, 3))])
    count = 0
    for _ in range(rows):
        temp = []
        for _ in range(cols):
            temp.append(sg.InputText(size = (3,0), key = str(count)))
            count += 1
        image_viewer_column.append(list(temp))

    return [
        [
            sg.Column(file_list_column, size = (colWidth,colHeight)),
            sg.VSeperator(),
            sg.Column(image_viewer_column, element_justification='c', size = (colWidth,colHeight)),
        ]
    ]

def solve(rows,cols,values):
    print(values)
    matrix = []
    temp = []
    for i in range(rows * cols):
        temp.append(int(values[i + 3]))
        if len(temp) == cols:
            matrix.append(list(temp))
            temp = []
    convertedMat = Matrix(matrix)
    convertedMat = convertedMat.rref()


    for i in range(len(list(convertedMat[0]))):
        window[str(i)].update(list(convertedMat[0])[i])

# First the window layout in 2 columns
sg.theme("DarkAmber")

window = sg.Window("Garrett's Linear Algebra Calculator",buildLayout(3,3))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "SOLVE":
        solve(rows,cols,values)
    elif event == "OK":

        window.close()
        window = sg.Window("Garrett's Linear Algebra Calculator",buildLayout(int(values[0]),int(values[1])))
        rows = int(values[0])
        cols = int(values[1])
    print(values)
