from tkinter import*
class BillApp:
   def __init__(self, root):

      self.root = root
      self.root.geometry("1350x700+0+0")
      self.root.title("Dharsh Super Market")
      bg_color = "#4d0000"
      title = Label(self.root, text = " Dharsh Super Market", bd = 12 , bg = bg_color, relief = GROOVE, fg = "#e6e600", font = ("Helvetica" , 35 , "bold") , pady = 2 ).pack(fill = X)

      F1 = LabelFrame(self.root, text = "Customer Details", font = ("hervetica", 15 , "italic"), fg = "#e6e600", bg = bg_color)
      F1.place(x = 0, y = 80, relwidth = 1)

      cname_lbl = Label(F1, text = "Customer Name", bg = "#4d0000", font = ("Helvetica", 18, "normal")).grid(row = 0, column = 0, padX = 20, padY = 5)


root = Tk()
obj = BillApp(root)
root.mainloop()

