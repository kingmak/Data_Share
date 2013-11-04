import os, sys, Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()
Title = 'Please Browse to The File You Wish to Add'
Startdir = os.path.join(os.path.expanduser('~'), 'Desktop')
AddFile = str(tkFileDialog.askopenfilename(initialdir = Startdir, title = Title))

if AddFile == '':
    os.startfile(os.path.join(os.getcwd(), 'Index.pyw'))
    sys.exit('')
    
File = open(os.path.join(os.getcwd(), 'FilePaths.txt'), 'a')
File.write(AddFile + '\n')
File.close()

os.startfile(os.path.join(os.getcwd(), 'Index.pyw'))
sys.exit('')
