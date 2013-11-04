import os, sys, Tkinter, tkMessageBox

Widget = Tkinter.Tk()
textA = ('**********************************************\n' +
           '            Delete File Path        \n' +
           '**********************************************')
textB = ('**********************************************\n' +
           '         Add New File Path     \n' +
           '**********************************************')
textC = ('**********************************************\n' +            
           '             Copy Data            \n' +
           '**********************************************')
textD = ('**********************************************\n' +            
           '                Quit                 \n' +
           '**********************************************')
textE = ('**********************************************\n' +            
           '          Created by KingMaK        \n' +
           '**********************************************')

def DelFilePaths():
   os.startfile(os.path.join(os.getcwd(), 'Del File.pyw'))
   sys.exit('')

def EditFilePaths():
   os.startfile(os.path.join(os.getcwd(), 'Add File.pyw'))
   sys.exit('')

def DataDistribute():
   os.startfile(os.path.join(os.getcwd(), 'Data Distribution.pyw'))
   sys.exit('')

def Quit():
   sys.exit('')

def Author():
   os.system('start https://github.com/kingmak')
   
DelFilePath =  Tkinter.Button(Widget, text = textA, command = DelFilePaths)
AddFilePath = Tkinter.Button(Widget, text = textB, command = EditFilePaths)
DataDistribute = Tkinter.Button(Widget, text = textC, command = DataDistribute)
Quit = Tkinter.Button(Widget, text = textD, command = Quit)
Author = Tkinter.Button(Widget, text = textE,  command = Author)

DelFilePath.pack()
AddFilePath.pack()
DataDistribute.pack()
Quit.pack()
Author.pack()

def centerWidget(w = 288, h = 375):  
    ws = Widget.winfo_screenwidth()
    hs = Widget.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    Widget.geometry('%dx%d+%d+%d' % (w, h, x, y))

centerWidget()
Widget.title('Distribute Data')
Widget.mainloop()
