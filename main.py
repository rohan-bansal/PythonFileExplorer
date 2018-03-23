import tkinter as tk
import os, platform, webbrowser


# INITIALIZATIONS
window = tk.Tk()
window.geometry('800x600')
window.title('File Explorer')
bl = []
placeY = 20
currentdir = 'Desktop'
SBseparator = tk.Frame(window, height = 580, width = 1, bg = "black")
FP = tk.Label(window, text = '')
Addfiles = tk.Button(window, text = 'New File', command = lambda: create_file(currentdir))
contentLabel = tk.Label(window)
path = os.path.dirname(os.path.abspath(__file__))
desk_path = path + '/Desktop'
doc_path = path + '/Documents'
pic_path = path + '/Pictures'
mus_path = path + '/Music'
trash_path = path + '/Trash'
fileselect = tk.Listbox(window, width = 75, height = 33, bg = window.cget('bg'))

indexlist = {
    'Desktop': 0,
    'Documents': 1,
    'Pictures': 2,
    'Music': 3,
    'Trash': 4 }

index_list = ['Desktop','Documents','Pictures','Music','Trash']
path_list = [desk_path, doc_path, pic_path, mus_path, trash_path]
for x in range(5):
    if index_list[x] not in os.listdir(path):
        os.mkdir(path_list[x])
    else:
        pass

contentLabel.place(x = 150, y = 80)
FP.place(x = 150, y = 20)
SBseparator.place(x = 100, y = 10)
Addfiles.place(x = 700, y = 10)
fileselect.place(x = 140, y = 80)

# FILE DISPLAY
def direction(type_):
    FilePath(type_)
    DisplayFiles(type_)
    open_file()

def FilePath(name):
    global FP
    global currentdir
    FP.config(text = name)
    currentdir = name

def DisplayFiles(which):
    fileselect.delete(0, 'end')
    for item in files[indexlist[which]][1:]:
        fileselect.insert('end', item)

def open_file():
    #selection = fileselect.curselection()
    pass

files = []

# SIDEBAR
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

for f in range(5):
    files[indexlist[index_list[f]]].extend(os.listdir(path_list[f]))

# CREATING FILES
def create_file(currentd):
    def addftoClass(entrycontent, currentdirectory):
        global currentdir
        global indexlist
        try:
            Desktop.add_file(indexlist[currentdir], entrycontent.get())  
            os.mknod(path + '/%s/%s' % (currentdirectory, entrycontent.get()))
            filenameD.destroy()
            filenameDE.destroy()
        except:
            pass
    filenameD = tk.Entry(window)
    filenameDE = tk.Button(window, text = 'OK', command = lambda: addftoClass(filenameD, currentd))
    filenameD.place(x = 620, y = 50)
    filenameDE.place(x = 575, y = 46)

v = tk.StringVar()
v.set('')

window.mainloop()
