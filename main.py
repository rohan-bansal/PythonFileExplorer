import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
window.title('File Explorer')
bl = []
placeY = 20
currentdir = ''
SBseparator = tk.Frame(window, height = 580, width = 1, bg = "black")
FP = tk.Label(window, text = '')
Addfiles = tk.Button(window, text = 'New File', command = lambda: create_file())
contentLabel = tk.Label(window)

contentLabel.place(x = 150, y = 80)
FP.place(x = 150, y = 20)
SBseparator.place(x = 100, y = 10)
Addfiles.place(x = 700, y = 10)

def direction(type_):
    FilePath(type_)
    DisplayFiles(type_)

def FilePath(name):
    global FP
    global currentdir
    FP.config(text = name)
    currentdir = name

def DisplayFiles(which):
    contentLabel.config(text = '\n\n'.join(files[indexlist[which]][1:]))

def OpenFilePath(type__):
    pass


files = []

class SideBar():
    def __init__(self, name):
        global window
        global bl
        global files
        self.name = name
        self.bl = bl
        self.bl.append(self.name)
          
    def create_folder(self, index):
        global placeY
        self.bl[index] = tk.Button(window, text = self.name, command = lambda: direction(self.name))
        self.bl[index].config(height = 3, width = 6)
        self.bl[index].place(x = 10, y = placeY)
        placeY += 70
    
    def add_file(self, folderIndex, filename):
        files[folderIndex].append(filename)
        print(files)
    
    def create_file_list(self):
        files.append(['Desktop'])
        files.append(['Documents'])
        files.append(['Pictures'])
        files.append(['Music'])
        files.append(['Trash'])
        print(files)



Desktop = SideBar('Desktop')
Documents = SideBar('Documents')
Pictures = SideBar('Pictures')
Music = SideBar('Music')
Trash = SideBar('Trash')

Desktop.create_file_list()
Desktop.create_folder(0)
Documents.create_folder(1)
Pictures.create_folder(2)
Music.create_folder(3)
Trash.create_folder(4)

def create_file():

    global indexlist
    global currentdir 

    def addftoClass(entrycontent):
        global currentdir
        global indexlist
        try:
            Desktop.add_file(indexlist[currentdir], entrycontent.get())  
            newfile = open(entrycontent.get(), 'w')
            filenameD.destroy()
            filenameDE.destroy()
        except:
            pass

    filenameD = tk.Entry(window)
    filenameDE = tk.Button(window, text = 'OK', command = lambda: addftoClass(filenameD))
    filenameD.place(x = 620, y = 50)
    filenameDE.place(x = 575, y = 46)

indexlist = {
    'Desktop': 0,
    'Documents': 1,
    'Pictures': 2,
    'Music': 3,
    'Trash': 4 }

window.mainloop()
