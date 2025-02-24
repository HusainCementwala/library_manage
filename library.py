from tkinter import*


class LibraryManagementSystem:
  def __init__(self, root):
    self.root = root
    self.root.title("Library Management System")
    self.root.geometry("1366x768+0+0")


    lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg="white", bd=20,relief=RIDGE, font=("helvetica",40,"bold"),padx=2,pady=6)
    lbltitle.pack(side=TOP,fill=X)


    frame = Frame(self.root,)
    



if __name__ == "__main__":
  root=Tk()
  obj=LibraryManagementSystem(root)
  root.mainloop()