---
name: GUI Update request
about: Suggest to contribute the GUI portion of any tool whose .py file is already present in the repo, but not included in the UI.
title: ''
labels: ''
assignees: ''

---

#### Feature Request:
There is no User Interface available on ENCODN for the tool PQR.

#### Solution required:
1. Create a button in the **ENCODN/ENCODN/BUTTONS/FRAME1BUTTON.py** file with the name PQR (check from dcode.fr if it is a dropdown or normal button)
2. The command of the button should call the **ENCODN/ENCODN/TOOLS/ABC/..../PQR/PQR-FRAME.py** file to display the frame of PQR inside Frame2.
3. Create your GUI console inside PQR-FRAME.py keeping the color codes and the theme in mind. 
4. Create any extra buttons you need in **ENCODN/ENCODN/BUTTONS/CUSTOMBUTTONS1.py** and import them accordingly.

#### Additional Info:
The file should be stored in the **ENCODN/ENCODN/TOOLS/ABC/DEF/** directory only, the filename, function name should be as specified above (case sensitive). Please import various buttons and frames from their directories as and when required.

#### Any questions/confusions? (if no, leave blank)
