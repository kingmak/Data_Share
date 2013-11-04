from collections import OrderedDict
import os, sys, linecache, Tkinter, tkSimpleDialog, tkMessageBox

FilePaths = []
InputData = []
InputDataSorted = ''

def AlertBox(Title, Message):
    window = Tkinter.Tk()
    window.withdraw()
    tkMessageBox.showinfo(title = Title, message = Message)
    window.destroy()

def StoreFilePaths():
    File = os.path.join(os.getcwd(), 'FilePaths.txt')
    count = 1
    OpenFile = open(File)
    LenFile = len(OpenFile.readlines())
    while count <= LenFile:
        FilePaths.append(linecache.getline(File, count).strip())
        count += 1

StoreFilePaths()
FilePaths = filter(None, FilePaths)

def ReadStoreInputData():
    count = 0
    while count < len(FilePaths):
        line = 1
        File = FilePaths[count]
        OpenFile = open(File)
        LenFile = len(OpenFile.readlines())
        while line <= LenFile:
            InputData.append(linecache.getline(File, line))
            line += 1
        count += 1
        
ReadStoreInputData()
InputDataSorted = list (OrderedDict.fromkeys(InputData))
InputDataSorted = filter(None, InputDataSorted)

def WriteStoredInputData():
    count = 0
    while count < len(FilePaths):
        i = 0
        File = open(FilePaths[count], 'w')
        while i < len(InputDataSorted):
            File.write(InputDataSorted[i])
            i += 1
        File.close()    
        count += 1

WriteStoredInputData()        
AlertBox('Finished', 'All Data was Copied to Their Respective File Locations')
sys.exit('')
