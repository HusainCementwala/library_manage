import datetime


def SelectBook(self,event=""):
      value = str(self.listBox.get(self.listBox.curselection()))
      x = value 
      if(x=="Python Crash Course"):
        self.bookid_var.set("BK1D5454")
        self.booktitle_var.set("Python Crash Course")
        self.author_var.set("Paul Bailey")

        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
        self.datedue_var.set(d3.strftime("%Y-%m-%d"))
        self.daysonbook_var.set(15)
        self.latereturnfine_var.set("Rs.50")
        self.dateoverdue_var.set("NA")
        self.finalprice_var.set("Rs.788")


      elif(x=="Automate the Boring Stuff with Python"):
        self.bookid_var.set("BK1D6263")
        self.booktitle_var.set("Automate the Boring Stuff with Python")
        self.author_var.set("Nash Mokrey")

        d1=datetime.datetime.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
        self.datedue_var.set(d3.strftime("%Y-%m-%d"))
        self.daysonbook_var.set(15)
        self.latereturnfine_var.set("Rs.50")
        self.dateoverdue_var.set("NA")
        self.finalprice_var.set("Rs.300")

      elif(x == "Learning Python"):
        self.bookid_var.set("BK1A1234")
        self.booktitle_var.set("Learning Python")
        self.author_var.set("Mark Lutz")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=15)
        d3 = d1 + d2
        self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
        self.datedue_var.set(d3.strftime("%Y-%m-%d"))
        self.daysonbook_var.set(15)
        self.latereturnfine_var.set("Rs.50")
        self.dateoverdue_var.set("NA")
        self.finalprice_var.set("Rs.850")
      
      elif(x == "Fluent Python"):
        self.bookid_var.set("BK1B5678")
        self.booktitle_var.set("Fluent Python")
        self.author_var.set("Luciano Ramalho")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=15)
        d3 = d1 + d2
        self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
        self.datedue_var.set(d3.strftime("%Y-%m-%d"))
        self.daysonbook_var.set(15)
        self.latereturnfine_var.set("Rs.50")
        self.dateoverdue_var.set("NA")
        self.finalprice_var.set("Rs.950")

      elif(x == "Effective Python"):
          self.bookid_var.set("BK1C9876")
          self.booktitle_var.set("Effective Python")
          self.author_var.set("Brett Slatkin")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.700")

      elif(x == "Python Cookbook"):
          self.bookid_var.set("BK1D3456")
          self.booktitle_var.set("Python Cookbook")
          self.author_var.set("David Beazley")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.1200")

      elif(x == "Think Python"):
          self.bookid_var.set("BK1E2233")
          self.booktitle_var.set("Think Python")
          self.author_var.set("Allen B. Downey")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.500")

      elif(x == "Python Tricks"):
          self.bookid_var.set("BK1F7890")
          self.booktitle_var.set("Python Tricks")
          self.author_var.set("Dan Bader")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.650")

      elif(x == "Serious Python"):
          self.bookid_var.set("BK1G4321")
          self.booktitle_var.set("Serious Python")
          self.author_var.set("Julien Danjou")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.750")

      elif(x == "Introduction to Machine Learning with Python"):
          self.bookid_var.set("BK1H5643")
          self.booktitle_var.set("Introduction to Machine Learning with Python")
          self.author_var.set("Andreas C. Müller")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.1100")

      elif(x == "Clean Code"):
          self.bookid_var.set("BK1I8765")
          self.booktitle_var.set("Clean Code")
          self.author_var.set("Robert C. Martin")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.950")

      elif(x == "The Pragmatic Programmer"):
          self.bookid_var.set("BK1J0987")
          self.booktitle_var.set("The Pragmatic Programmer")
          self.author_var.set("Andy Hunt")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.1000")

      elif(x == "Design Patterns: Elements of Reusable Object-Oriented Software"):
        self.bookid_var.set("BK1K1234")
        self.booktitle_var.set("Design Patterns: Elements of Reusable Object-Oriented Software")
        self.author_var.set("Erich Gamma")
        d1 = datetime.datetime.today()
        d2 = datetime.timedelta(days=15)
        d3 = d1 + d2
        self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
        self.datedue_var.set(d3.strftime("%Y-%m-%d"))
        self.daysonbook_var.set(15)
        self.latereturnfine_var.set("Rs.50")
        self.dateoverdue_var.set("NA")
        self.finalprice_var.set("Rs.1400")

      elif(x == "Code Complete"):
          self.bookid_var.set("BK1L5678")
          self.booktitle_var.set("Code Complete")
          self.author_var.set("Steve McConnell")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.1300")

      elif(x == "You Don't Know JS"):
          self.bookid_var.set("BK1M9876")
          self.booktitle_var.set("You Don't Know JS")
          self.author_var.set("Kyle Simpson")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.600")

      elif(x == "Eloquent JavaScript"):
          self.bookid_var.set("BK1N3456")
          self.booktitle_var.set("Eloquent JavaScript")
          self.author_var.set("Marijn Haverbeke")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.750")

      elif(x == "Grokking Algorithms"):
          self.bookid_var.set("BK1O2233")
          self.booktitle_var.set("Grokking Algorithms")
          self.author_var.set("Aditya Y. Bhargava")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.900")

      elif(x == "Structure and Interpretation of Computer Programs"):
          self.bookid_var.set("BK1P7890")
          self.booktitle_var.set("Structure and Interpretation of Computer Programs")
          self.author_var.set("Harold Abelson")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.1150")

      elif(x == "The Art of Computer Programming"):
          self.bookid_var.set("BK1Q4321")
          self.booktitle_var.set("The Art of Computer Programming")
          self.author_var.set("Donald Knuth")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.5000")

      elif(x == "Refactoring: Improving the Design of Existing Code"):
          self.bookid_var.set("BK1R5643")
          self.booktitle_var.set("Refactoring: Improving the Design of Existing Code")
          self.author_var.set("Martin Fowler")
          d1 = datetime.datetime.today()
          d2 = datetime.timedelta(days=15)
          d3 = d1 + d2
          self.dateborrowed_var.set(d1.strftime("%Y-%m-%d"))
          self.datedue_var.set(d3.strftime("%Y-%m-%d"))
          self.daysonbook_var.set(15)
          self.latereturnfine_var.set("Rs.50")
          self.dateoverdue_var.set("NA")
          self.finalprice_var.set("Rs.1250")