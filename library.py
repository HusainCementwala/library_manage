from tkinter import *
from tkinter import ttk


class LibraryManagementSystem:
  def __init__(self, root):
    self.root = root
    self.root.title("Library Management System")
    self.root.geometry("1366x768+0+0")


    lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg="white", bd=20,relief=RIDGE, font=("helvetica",40,"bold"),padx=2,pady=6)
    lbltitle.pack(side=TOP,fill=X)


    frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    frame.place(x=0,y=130,width=1530,height=400)
    
   #==============================DATA FRAME LEFT=============================
    DataFrameLeft = LabelFrame(frame,text="Library Membership Info",bg="powder blue",fg="black", bd=12,relief=RIDGE, font=("helvetica",12,"bold"))
    DataFrameLeft.place(x=0,y=5,width=900,height=350)


    lblMember = Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblMember.grid(row=0,column=0,sticky=W)

    comMember = ttk.Combobox(DataFrameLeft,font=("helvetica",12,"bold"),width=27,state="readonly")
    comMember["value"]=("Admin Staff","Student","Lecturer")
    comMember.grid(row=0,column=1)



    lblPRN_No = Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblPRN_No.grid(row=1,column=0,sticky=W)
    txtPRN_NO = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtPRN_NO.grid(row=1,column=1)


    lblTitle = Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblTitle.grid(row=2,column=0,sticky=W)
    txtTitle = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtTitle.grid(row=2,column=1)


    lblFirstName = Label(DataFrameLeft,bg="powder blue",text="First Name:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblFirstName.grid(row=3,column=0,sticky=W)
    txtFirstName = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtFirstName.grid(row=3,column=1) 


    lblLastName = Label(DataFrameLeft,bg="powder blue",text="Last Name:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblLastName.grid(row=4,column=0,sticky=W)
    txtLastName = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtLastName.grid(row=4,column=1)



    lblAddress1 = Label(DataFrameLeft,bg="powder blue",text="Address 1:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblAddress1.grid(row=5,column=0,sticky=W)
    txtAddress1 = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtAddress1.grid(row=5,column=1)


    lblAddress2 = Label(DataFrameLeft,bg="powder blue",text="Address 2:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblAddress2.grid(row=6,column=0,sticky=W)
    txtAddress2 = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtAddress2.grid(row=6,column=1)

    
    lblPRN_No = Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblPRN_No.grid(row=7,column=0,sticky=W)
    txtPRN_NO = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtPRN_NO.grid(row=7,column=1)


    lblPRN_No = Label(DataFrameLeft,bg="powder blue",text="Mobile",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblPRN_No.grid(row=8,column=0,sticky=W)
    txtPRN_NO = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtPRN_NO.grid(row=8,column=1)


   


   





    DataFrameRight = LabelFrame(frame,text="Book Details",bg="powder blue",fg="black", bd=12,relief=RIDGE, font=("helvetica",12,"bold"))
    DataFrameRight.place(x=910,y=5,width=540,height=350)

    #==============================BUTTON FRAMES=============================

    FrameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    FrameButton.place(x=0,y=530,width=1530,height=70)


    #==============================INFO FRAMES=============================

    FrameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    FrameDetails.place(x=0,y=600,width=1530,height=195)


    



if __name__ == "__main__":
  root=Tk()
  obj=LibraryManagementSystem(root)
  root.mainloop()