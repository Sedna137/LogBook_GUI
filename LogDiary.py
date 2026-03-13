from tkinter import *
import time
import os

'''
Digital logbook
- This user interface allows one to write notes and logs.
- Entries will be saved, including a time stamp.
- Separate sections for independent tasks as well as additional notes included.

Author Jeena A. V.
Created in 2019
Updated on 11.03.2026
written in Python 3.14.2
'''

class LogDiary():
    
    def __init__(self, root):

        logs = self.SaveLogs()
        self.logsFrame = Frame(root)
        self.logsFrame.pack(side=TOP)
        self.frame=Frame(root, borderwidth=1, relief=SOLID)
        self.frame.pack(side=TOP)

        self.Q1Label = Label(self.logsFrame, text="Task1 question ")
        self.Q1Label.grid(row=0, column=0, sticky=E)
        self.Q1 =Text(self.logsFrame, height=3)
        self.Q1.insert(1.0, logs[0])
        self.Q1.bind("<Tab>", focus_next_window)
        self.Q1.grid(row=0, column=1)

        self.Q2Label = Label(self.logsFrame, text="Task 2 question")
        self.Q2Label.grid(row=1, column=0, sticky=E)
        self.Q2 = Text(self.logsFrame, height=3)
        self.Q2.insert(1.0, logs[1])
        self.Q2.bind("<Tab>", focus_next_window)
        self.Q2.grid(row=1, column=1)


        self.textArea = Text(self.frame, height = 20)
        self.textArea.grid(row=1, column=0)
        self.textArea.bind("<Tab>", focus_next_window)
        self.textArea.insert(1.0,"Location: ") # In case, location of the entry of log is important
        self.button = Button(self.frame, text="Save all", command = self.onSubmit) # saves task 1, 2, and notes
        self.button.grid(row=2, column=0, sticky = E)
        self.button = Button(self.frame, text="Save notes", command = self.SaveNotes) # saves only notes. Useful for multiple entries for same set of tasks
        self.button.grid(row=2, column=0, sticky = W)

    def SaveNotes(self):
        f.write("\n*****************************************************\n"+timestamp+"\n") # Adding paragraph break
        f.write(self.textArea.get(1.0, END))
        f.close()
        root.destroy()

    def onSubmit(self):
        f.write("\n*****************************************************\n"+timestamp+"\n") # Adding paragraph break
        f.write("#1 Starting Sentence for task 1:\n"+self.Q1.get(1.0, END)+'\n') # optional
        f.write("#2 Starting Sentence for task 2:\n"+self.Q2.get(1.0, END)+'\n') # optional
        f.write("Additional notes:\n" + self.textArea.get(1.0, END))
        f.close()
        root.destroy()

    def SaveLogs(self):
        global timestamp, ROOT_DIR, f
        timestamp = time.strftime("%d.%m.%Y, %H:%M", time.localtime()) # Case I. All entries are into same file.
        #timestamp = time.strftime("%Y-%m-%d_%H-%M", time.gmtime())  # case II. To save each entry as new file
        ROOT_DIR = r"D:/" # change to your desired root directory
        f = open( "D:/LogsGoHere.txt", 'a+') # Case I. generates 'LogsGoHere.txt' and writes entries.
        #f = open( ROOT_DIR +timestamp + ".txt", 'a+') # case II. Use this if logs must be saved each time in individual file


        retVal = [f.readline().replace("\n", "T"), f.readline().replace("\n", "F")]
        return retVal

    
def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")
        
root = Tk()
app = LogDiary(root)
root.wm_title("LogDiary")
root.mainloop()

