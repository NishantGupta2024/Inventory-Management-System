from tkinter import*
from PIL import Image,ImageTk
from Employee import EmployeeClass
from Supplier import SupplierClass
from Category import CategoryClass
from Product import ProductClass
from Sales import SalesClass
from billing import BillClass
import os;
import time
import sqlite3
from tkinter import messagebox

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("INVENTORY MANAGEMENT SYSTEM ")
        self.root.config(bg="white")
        
        #Title
        self.icon_title=PhotoImage(file="Images/cart.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #Button Logout    
        btn_logout=Button(self.root,text="Log Out",font=("times new roman",18,"bold"),bg="yellow",cursor="hand2")
        btn_logout.place(x=1180,y=15,width=150,height=35)
        
        # clock
        self.lbl_clock=Label(self.root,text="Date : DD-MM-YYYY   \t\t   Welcome to Inventory Management System  \t\t  Time : HH:MM:SS ",font=("imes new roman",18),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # Left Menu
        self.Menulogo = Image.open("Images/menu_im.png")
        self.Menulogo = self.Menulogo.resize((200, 200))
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)

        Left_Menu = Frame(self.root, bd=2, relief=RIDGE)
        Left_Menu.place(x=5, y=102, width=200, height=565)

        menu_label = Label(Left_Menu, image=self.Menulogo)
        menu_label.pack()

        lbl_menu=Label(Left_Menu,text="Menu",font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X)
        self.icon_side=PhotoImage(file="Images/side.png")
        Btn_Employee=Button(Left_Menu,text="Employee",command=self.Employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_Supplier=Button(Left_Menu,text="Supplier",command=self.Supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_Category=Button(Left_Menu,text="Category",command=self.Category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_Product=Button(Left_Menu,text="Product",command=self.Product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_Sales=Button(Left_Menu,text="Sales",command=self.Sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_Exit=Button(Left_Menu,text="Exit",command=self.billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        # Content

        self.lbl_emp=Label(self.root,text="Total Employee\n[ 0 ]",bg="#33bbf9",bd=5,fg="white",font=("Arail Black",20,"bold"))
        self.lbl_emp.place(x=300,y=120,height=150,width=300)
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bg="#ff5722",bd=5,fg="white",font=("Arail Black",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bg="#009688",bd=5,fg="white",font=("Arail Black",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bg="#607d8b",bd=5,fg="white",font=("Arail Black",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bg="#ffc107",bd=5,fg="white",font=("Arail Black",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        lbl_Footer=Label(self.root,text="  IMS - Inventory Management System \n For any queries contact here - 756XXXXXXX ",font=("imes new roman",10),bg="#4d636d",fg="white").pack(side="bottom",fill=X)
        self.update_content()
        self.update_date_time()
        
        
    def Employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=EmployeeClass(self.new_win)
    def Supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)    
    def Category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win) 
    def Product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)  
    def Sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesClass(self.new_win) 
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)     
    def update_content(self):
        con=sqlite3.connect(database=r"ims.db")    
        cur=con.cursor() 
        
        # Employee data
        try:
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_emp.config(text=f'Total Employees\n[{str(len(employee))}]')
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
        
        # supplier data        
        try:
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
    
        # category data
        try:
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Categories\n[{str(len(category))}]')
        
            bill=len(os.listdir('bill'))    
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')    
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
        
        try:
            cur.execute("select * from Product")
            Product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[{str(len(Product))}]')
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
       
            
      
    def update_date_time(self):
        time_ = time.strftime("%H:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Date : {str(date_)}  \t\t   Welcome to Inventory Management System  \t\t  Time : {str(time_)} ")    
        self.lbl_clock.after(200,self.update_date_time)       
            
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()