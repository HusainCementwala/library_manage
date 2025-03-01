from tkinter import *
from tkinter import ttk
import mysql.connector


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


    lblBookId = Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblBookId.grid(row=0,column=2,sticky=W)
    txtBookId = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtBookId.grid(row=0,column=3)


    lblBookTitle = Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblBookTitle.grid(row=1,column=2,sticky=W)
    txtBookTitle = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtBookTitle.grid(row=1,column=3)


    lblAuthor = Label(DataFrameLeft,bg="powder blue",text="Author Name",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblAuthor.grid(row=2,column=2,sticky=W)
    txtAuthor = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtAuthor.grid(row=2,column=3)


    lblDateBorrowed = Label(DataFrameLeft,bg="powder blue",text="Borrowed On:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblDateBorrowed.grid(row=3,column=2,sticky=W)
    txtDateBorrowed = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtDateBorrowed.grid(row=3,column=3)


    lblDateDue = Label(DataFrameLeft,bg="powder blue",text="Due On",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblDateDue.grid(row=4,column=2,sticky=W)
    txtDateDue = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtDateDue.grid(row=4,column=3)


    lblDaysOnBook = Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblDaysOnBook.grid(row=5,column=2,sticky=W)
    txtDaysOnBook = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtDaysOnBook.grid(row=5,column=3)


    lblLateReturnFine = Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblLateReturnFine.grid(row=6,column=2,sticky=W)
    txtLateReturnFine = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtLateReturnFine.grid(row=6,column=3)


    lblDateOverDue = Label(DataFrameLeft,bg="powder blue",text="Date Overdue:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblDateOverDue.grid(row=7,column=2,sticky=W)
    txtDateOverDue = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtDateOverDue.grid(row=7,column=3)


    lblActualPrice = Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("helvetica",12,"bold"),padx=2,pady=6)
    lblActualPrice.grid(row=8,column=2,sticky=W)
    txtActualPrice = Entry(DataFrameLeft,font=("helvetica",12,"bold"),width=29)
    txtActualPrice.grid(row=8,column=3)

#================================================DATA FRAME RIGHT========================================

    DataFrameRight = LabelFrame(frame,text="Book Details",bg="powder blue",fg="black",padx=20, bd=12,relief=RIDGE, font=("helvetica",12,"bold"))
    DataFrameRight.place(x=870,y=5,width=580,height=350)


    self.txtBox = Text(DataFrameRight,font=("helvetica",12,"bold"),width=32,height=15,padx=2,pady=6)
    self.txtBox.grid(row=0,column=2)


    listScrollBar = Scrollbar(DataFrameRight)
    listScrollBar.grid(row=0,column=1,sticky="ns")

    listBooks = ['Python Crash Course','Automate the Boring Stuff with Python','Learning Python','Fluent Python','Effective Python','Python Cookbook','Think Python','Python Tricks','Serious Python','Introduction to Machine Learning with Python','Clean Code','The Pragmatic Programmer','Design Patterns: Elements of Reusable Object-Oriented Software','Code Complete','You Dont Know JS','Eloquent JavaScript','Grokking Algorithms','Structure and Interpretation of Computer Programs','The Art of Computer Programming','Refactoring: Improving the Design of Existing Code']

    listBox = Listbox(DataFrameRight,font=("helvetica",12,"bold"),width=20,height=15)
    listBox.grid(row=0,column=0,padx=4)
    listScrollBar.config(command=listBox.yview)

    for item in listBooks:
      listBox.insert(END,item)

    #============================== BUTTON FRAMES =============================

    FrameButton = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    FrameButton.place(x=0,y=530,width=1530,height=70)


    # Define the number of buttons
    num_buttons = 6  

# Configure grid columns for equal spacing
    for i in range(num_buttons):
     FrameButton.grid_columnconfigure(i, weight=1)



    btnAddData = Button(FrameButton,text="Add Book",font=("helvetica",12,"bold"),width=18,bg="black",fg="white")
    btnAddData.grid(row=0,column=0,pady=5,padx=5)

    btnAddData = Button(FrameButton,text="Show Books",font=("helvetica",12,"bold"),width=18,bg="black",fg="white")
    btnAddData.grid(row=0,column=1,pady=5,padx=5)

    btnAddData = Button(FrameButton,text="Update Books",font=("helvetica",12,"bold"),width=18,bg="black",fg="white")
    btnAddData.grid(row=0,column=2,pady=5,padx=5)

    btnAddData = Button(FrameButton,text="Delete Book",font=("helvetica",12,"bold"),width=18,bg="black",fg="white")
    btnAddData.grid(row=0,column=3,pady=5,padx=5)

    btnAddData = Button(FrameButton,text="Reset",font=("helvetica",12,"bold"),width=18,bg="black",fg="white")
    btnAddData.grid(row=0,column=4,pady=5,padx=5)

    btnAddData = Button(FrameButton,text="Exit",font=("helvetica",12,"bold"),width=18,bg="black",fg="white")
    btnAddData.grid(row=0,column=5,pady=5,padx=5)


    #============================== INFO FRAMES  =============================

    FrameDetails = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
    FrameDetails.place(x=0,y=600,width=1530,height=195)


    Table_frame = Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
    Table_frame.place(x=0,y=2,width=1460,height=170)

    xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
    yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

    self.library_table=ttk.Treeview(Table_frame,columns=("MemberType","PRNno","Title","FirstName","Lastname","Address1","Address2","PostID","Mobile","BookID","BookTitle","Author","DateBorrowed","DateDue","Days","LateReturnFine","DateOverdue","FinalPrice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

    xscroll.pack(side=BOTTOM,fill=X)
    yscroll.pack(side=RIGHT,fill=Y)

    xscroll.config(command=self.library_table.xview)
    yscroll.config(command=self.library_table.yview)


    self.library_table.heading("MemberType",text="Member Type")
    self.library_table.heading("PRNno",text="PRN No.")
    self.library_table.heading("Title",text="Title")
    self.library_table.heading("FirstName",text="First Name")
    self.library_table.heading("Lastname",text="Last Name")
    self.library_table.heading("Address1",text="Address1")
    self.library_table.heading("Address2",text="Address2")
    self.library_table.heading("PostID",text="Post ID")
    self.library_table.heading("Mobile",text="Mobile Number")
    self.library_table.heading("BookID",text="Book ID")
    self.library_table.heading("BookTitle",text="Book Title")
    self.library_table.heading("Author",text="Author")
    self.library_table.heading("DateBorrowed",text="Date of Borrowed")
    self.library_table.heading("DateDue",text="Date Due")
    self.library_table.heading("Days",text="DaysOnBook")
    self.library_table.heading("LateReturnFine",text="LateReturnFine")
    self.library_table.heading("DateOverdue",text="DateOverDue")
    self.library_table.heading("FinalPrice",text="Final Price")


    columns = ["MemberType","PRNno","Title","FirstName","Lastname","Address1","Address2","PostID","Mobile","BookID","BookTitle","Author",        "DateBorrowed","DateDue","Days","LateReturnFine","DateOverdue","FinalPrice"]
    for col in columns:
     self.library_table.column(col, width=100)


    self.library_table["show"]="headings"
    self.library_table.pack(fill=BOTH,expand=1)




    



if __name__ == "__main__":
  root=Tk()
  obj=LibraryManagementSystem(root)
  root.mainloop()