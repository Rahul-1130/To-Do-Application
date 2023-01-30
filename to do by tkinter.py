import tkinter
from tkinter import *

#create root window
root=Tk()

#Root window title and dimension
root.title("To-do application")
root.geometry("400x650+400+100")


task_list=[]

def deleteTask():
    global task_list
    
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w')as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")


        listbox.delete(ANCHOR)

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(0, task)

def openTaskfile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)


    except:
        file=open('tasklist.txt','w')
        file.close()

#to put icon image for title name
Image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False,Image_icon)

#create top bar function at top side
TopImage=PhotoImage(file="Image/topbar.png")
Label(root,image=TopImage).pack()

#to create dockimage
dockImage=PhotoImage(file="Image/dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=340,y=25)

#to create notepad image
noteImage=PhotoImage(file="Image/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=30,y=20)


#to Put "ALL TASK" text in topbar
heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

#to create a frame 
frame=Frame(root,width=400,height=50,bg="yellow")
frame.place(x=0,y=180)

#to create frame for enter task
task=StringVar()
task_entry=Entry(frame,width=20,font="arial 20",bd=1)
task_entry.place(x=10,y=7)
task_entry.focus()

#to create Add Task
button=Button(frame,text="Add",font="arial 20 bold", width=6 ,bg ="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=00)

# to create listbox frame
frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH , padx=2)

#to make scrollbar for up and down
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete button
Delete_icon=PhotoImage(file="Image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=15)

openTaskfile()

root.mainloop()
