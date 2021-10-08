# img_viewer.py

import PySimpleGUI as sg


def buildLayout(rows,cols):
    matrix = []

    for _ in range(rows):
        temp = []
        for _ in range(cols):
            temp.append(sg.InputText(size = (3,0)))
        matrix.append(list(temp))

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
        [sg.Text("Fill in the matrix")],
        [sg.Button("Click this Trash", size=(25, 1), pad=(0, 0))]
    ]


    for i in matrix:
        image_viewer_column.append(i)

    return [
        [
            sg.Column(file_list_column, size = (colWidth,colHeight)),
            sg.VSeperator(),
            sg.Column(image_viewer_column, element_justification='l', size = (colWidth,colHeight)),
        ]
    ]
# First the window layout in 2 columns
sg.theme("DarkAmber")

window = sg.Window("Garrett's Linear Algebra Calculator",buildLayout(3,3))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Click this Trash":
        print("really bruh")
    elif event == "OK":


        window.close()
        window = sg.Window("Garrett's Linear Algebra Calculator",buildLayout(int(values[0]),int(values[1])))
    print(values)
