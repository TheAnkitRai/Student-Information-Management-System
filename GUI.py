# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 03:15:36 2020

@author: Aniket Rai
"""


from tkinter import *
from tkinter import StringVar , Label , ttk , scrolledtext , filedialog,simpledialog , messagebox
from main_module import *
from PIL import Image, ImageTk



# TO verify New Student entries -----------------------------------------------------------------
def verifier():
    a=b=c=d=e=f=g=h=i=j=0
    txt.delete(1.0,END)
    if not qaa.get() or qaa.get() == "SELECT":
        txt.insert(INSERT," \n\n------------------------------>>\n\nSelect Session Properly \n")
        a=1
    if not qbb.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not qcc.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not qdd.get() or qdd.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not qee.get() or qee.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not qff.get() or qff.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    if not qgg.get() :
        txt.insert(INSERT,"Type Father Name \n")
        g=1
    if not qhh.get() :
        txt.insert(INSERT,"Type Mother Name \n")
        h=1
    if not qii.get() or qii.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not qjj.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 :
        return 1
    else:
        return 0

# To verify Update Student entries-------------------------------------------------------
def verifier1():
    a=b=c=d=e=f=g=h=i=j=k=0
    txt.delete(1.0,END)
    if not roll1.get():
        txt.insert(INSERT," \n\n------------------------------>>\n\nType Roll No.. \n")
        a=1
    if not aa1.get() or aa1.get() == "SELECT":
        txt.insert(INSERT,"Select Session Properly \n")
        k=1
    if not bb1.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not cc1.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd1.get() or dd1.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee1.get() or ee1.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff1.get() or ff1.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    if not gg1.get() :
        txt.insert(INSERT,"Type Father Name \n")
        g=1
    if not hh1.get() :
        txt.insert(INSERT,"Type Mother Name \n")
        h=1
    if not ii1.get() or ii1.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj1.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 :
        return 1
    else:
        return 0


def add_student() :      # Add student records into existing or new file...
    if verifier() == 0 :
        student = {"session" : qaa.get() , "first_name" :qbb.get() , "last_name" : qcc.get() , "class" : qdd.get() ,  "section" : qee.get() , "gender" : qff.get() , "father" : qgg.get() , "mother" : qhh.get(),
                   "mobile" : qii.get(),"address" : qjj.get()}

        return_data = student_create(student)       # Calling function from "main_module"  
        txt.delete(1.0,END)
        
        for key, value in return_data.items() :     # Display recorded data/entries
            roll=str(key)
            txt.insert(INSERT,"\n------------------------------>>\n")
            txt.insert(INSERT,"Your Details -->>"+"\n\nRoll No. : "+roll+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+
                       "\nClass : "+return_data[key]["class"]+"\nFather : "+return_data[key]["father"]+"\nMother : "+return_data[key]["mother"]+"\nMobile : "+return_data[key]["mobile"]+
                       "\nAddress :"+return_data[key]["address"],"\n")
 
        qaa.delete(0,END)          # Clearing entries from the entry box after saving it.......
        qbb.delete(0,END)
        qcc.delete(0,END)
        qdd.delete(0,END)
        qee.delete(0,END)
        qff.delete(0,END)
        qgg.delete(0,END)
        qhh.delete(0,END)
        qii.delete(0,END)
        qjj.delete(0,END)


def view_student() :        # View all existing sudent records
    return_data = student_list()
    txt.delete(1.0,END)
    txt.insert(INSERT,"\n Roll No.,\t\tStudent Name,\t\t Class ,\t\t Section,\t\t Father Name ,\t\t\t Mobile ,\t\t\t Address \n")
    for key, value in return_data.items() :
        if return_data[key] == "This Record is Deleted from System" :
            continue
        else :
            roll=str(key)
            txt.insert(INSERT,"\n"+roll+",\t\t"+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+",\t\t"+return_data[key]["class"]+",\t\t"+return_data[key]["section"]+",\t\t"+return_data[key]
                       ["father"]+",\t\t\t"+return_data[key]["mobile"]+",\t\t\t"+return_data[key]["address"],"\n")
            


def update_student() :        # Update an existing student record...
    if verifier1() == 0 :
        rollNo = roll1.get()
        student = {"session" : aa1.get() , "first_name" : bb1.get() , "last_name" : cc1.get() , "class" : dd1.get() ,  "section" : ee1.get() , "gender" : ff1.get() , "father" : gg1.get() , "mother" : hh1.get(),
                   "mobile" : ii1.get(),"address" : jj1.get()}
        return_data = student_update(rollNo,student)
        txt.delete(1.0,END)
        
        for key, value in return_data.items() :
            if key == rollNo :
                rollNo=str(key)
                txt.insert(INSERT,"\n------------------------------>>\n")
                txt.insert(INSERT,"Updated Details -->>"+"\n\nRoll No. : "+rollNo+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+
                           "\nFather : "+return_data[key]["father"]+"\nMother : "+return_data[key]["mother"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")
                
        aa1.delete(0,END)         # Clearing entries from the entry box after updating it......
        bb1.delete(0,END)
        cc1.delete(0,END)
        dd1.delete(0,END)
        ee1.delete(0,END)
        ff1.delete(0,END)
        gg1.delete(0,END)
        hh1.delete(0,END)
        ii1.delete(0,END)
        jj1.delete(0,END)                

                
        
def delete_student() :         # Delete an existing student record by giving student's roll no...
    messagebox.showwarning("Warning","Are you sure to delete ?")         # Display a message box for confirmation to delete..
    data = student_delete(entry_delete.get())
    txt.delete(1.0,END)
    txt.insert(INSERT,data)
    
    
def saveFile() :              # Save the existing records as a spreadsheet..
    f = filedialog.asksaveasfile(mode='w',defaultextension='.csv')          # Pop-up for saving the file in 'csv' format...
    if f!= None:
        data = txt.get('1.0',END)
    try:
        f.write(data)
        txt.delete(1.0,END)
        txt.insert(INSERT,"Spreadsheet Saved Successfully !")
    except:
        messagebox.showerror(title="Aww Snap!!",message="Something went wrong.\nUnable to save file!")        # Pop_up message when file has not been saved....



def classwise() :        # Display class wise students' records
    return_data = student_list()
    txt.delete(1.0,END)
    if combo_class.get() in ("NURSERY","LKG","UKG",'1', '2', '3', '4', '5','6','7','8','9','10','11','12') :
        for key, value in return_data.items() :
            if return_data[key] == "This Record is Deleted from System" :
                continue
            else :
                roll=str(key)
                if combo_class.get() == return_data[key]["class"]:
                    txt.insert(INSERT,"\n"+roll+",\t"+return_data[key]["first_name"]+"\t"+return_data[key]["last_name"]+",\t"+return_data[key]["class"]+",\t"+return_data[key]["section"]+",\t"+return_data[key]["gender"]+",\t"+return_data[key]["father"]+",\t"+return_data[key]["mother"]+",\t"+return_data[key]["mobile"]+",\t"+return_data[key]["address"],"\n")
                    
                    
                    
if __name__=="__main__":
    root=Tk()          # Object for tkinter window
    root.state("zoomed")          # Open window in full screen mode
    root.title("Student Information Management System")      # Title of the main tkinter window
    root.configure(bg="khaki")        # Set main tkinter window bg color 
    root.resizable(0,0)              # Set tkinter window non-resizable
    
    
    # Display school logo image ----------------------------------------------------------------------------
    img1=Image.open("junior1.png")          
    img2=ImageTk.PhotoImage(img1)
    lbl1=Label(root,bg="khaki",image=img2)
    lbl1.image=img2
    
    lbl1.place(x=450,y=0)       # Position school logo Image
    
    
    # Text Variable Type for "ADD STUDENT" fields --------------------------------
    sess = StringVar()
    fn = StringVar()
    ln = StringVar()
    cl = StringVar()
    sect = StringVar()
    gen = StringVar()
    fa_name= StringVar()
    mo_name = StringVar()
    mob = StringVar()
    ad = StringVar()
    
    # Text Variable Type for "UPDATE STUDENT" fields --------------------------------
    roll1 = StringVar()
    sess1 = StringVar()
    fn1 = StringVar()
    ln1 = StringVar()
    cl1 = StringVar()
    sect1 = StringVar()
    gen1 = StringVar()
    fa_name1= StringVar()
    mo_name1 = StringVar()
    mob1 = StringVar()
    ad1 = StringVar()
    
    # Text Varibles Type for "DELETE STUDENT" field----------------------------------
    roll_delete = StringVar()
    

    # "Add Student" Window ======================================================
    def add_st():
        root=Tk()            # "ADD STUDENT" Tkinter window  object
        w=360                # Window width
        h=452                # Window height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title("ADD NEW STUDENT ")
        root.configure(bg="black")
        root.resizable(0,0)
        
        heading=Label(root,bg="black",text="NEW STUDENT",font=("Arial Rounded MT Bold",22),foreground ="white")
        label_a=Label(root,bg="black",text="Session :",font=("Arial bold",12),width=11,fg="white")
        label_b=Label(root,bg="black",text="First Name :",font=("Arial bold",12),width=11,fg='white')
        label_c=Label(root,bg="black",text="Last Name :",font=("Arial bold",12),width=11,fg='white')
        label_d=Label(root,bg="black",text="Class :",font=("Arial bold",12),width=11,fg="white")
        label_e=Label(root,bg="black",text="Section :",font=("Arial bold",12),width=11,fg="white")
        label_f=Label(root,bg="black",text="Gender :",font=("Arial bold",12),width=11,fg="white")
        label_g=Label(root,bg="black",text="Father Name :",font=("Arial bold",12),width=11,fg="white")
        label_h=Label(root,bg="black",text="Mother Name :",font=("Arial bold",12),width=11,fg="white")
        label_i=Label(root,bg="black",text="Mobile :",font=("Arial bold",12),width=11,fg="white")
        label_j=Label(root,bg="black",text="Address :",font=("Arial bold",12),width=11,fg="white")
        
        global qaa
        global qbb
        global qcc
        global qdd
        global qee
        global qff
        global qgg
        global qhh
        global qii
        global qjj
        
        
        qaa = ttk.Combobox(root,width=15)    # Session entry
        qaa['values']= ("SELECT","2015-16","2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23")
        qaa.current(0)   #set the selected item
        
        qbb=Entry(root,textvariable=fn,width=17,bd=4)    # first name
        
        qcc=Entry(root,textvariable=ln,width=17,bd=4)    # last name
        
        qdd = ttk.Combobox(root,width=15)    # class name
        qdd['values']= ("SELECT","NURSERY","LKG","UKG",1, 2, 3, 4, 5,6,7,8,9,10,11,12)
        qdd.current(0)  #set the selected item
        
        qee = ttk.Combobox(root,width=15)    # section name
        qee['values']= ("A","B","C","D","E")
        qee.current(0)  #set the selected item
        
        qff = ttk.Combobox(root,width=15)    # gender
        qff['values']= ("SELECT","Male","Female")
        qff.current(0)  #set the selected item
        
        qgg=Entry(root,textvariable=fa_name,width=17,bd=4)    # father name
        
        qhh=Entry(root,textvariable=mo_name,width=17,bd=4)    # mother name
        
        qii=Entry(root,textvariable=mob,width=17,bd=4)    # mobile number
        
        qjj=Entry(root,textvariable=ad,width=17,bd=4)    # address
        
        
        # Placing headings and labels-----------
        heading.place(x=65,y=0)
        label_a.place(x=15,y=51)
        label_b.place(x=15,y=78)
        label_c.place(x=15,y=110)
        label_d.place(x=15,y=142)
        label_e.place(x=15,y=169)
        label_f.place(x=15,y=196)
        label_g.place(x=15,y=224)
        label_h.place(x=15,y=256)
        label_i.place(x=15,y=288)
        label_j.place(x=15,y=320)
        
        
        # Placing entry boxes, buttons and combo boxes on "ADD STUDENT" tkinter window ----------
        qaa.place(x=200,y=51)   
        qbb.place(x=200,y=78)
        qcc.place(x=200,y=110)
        qdd.place(x=200,y=142)
        qee.place(x=200,y=169)
        qff.place(x=200,y=196)
        qgg.place(x=200,y=224)
        qhh.place(x=200,y=256)
        qii.place(x=200,y=288)
        qjj.place(x=200,y=320)
        
        
     
        b1=Button(root,text="ADD",command=lambda: add_student(),width=38,background ="deep sky blue", foreground ="purple",font=("Arial Rounded MT Bold",11),bd=5)
        b1.place(x=2,y=370)
        
        # Button to go bck to main window
        # Destroy function used to dissolve window
        b2=Button(root,text="GO TO HOME PAGE",command=lambda: root.destroy() ,width=38,background = 'deep sky blue', foreground ="red",font=("Arial Rounded MT Bold",11),bd=5)
        b2.place(x=2,y=410)
       
        root.mainloop()
        
        
        
    # "UPDATE STUDENT"  WindoW ================================================
    def update_st() :
        root=Tk()
        w=360
        h=480
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title("UPDATE STUDENT INFORMATION")
        root.configure(bg="black")
        root.resizable(0,0)
        
        heading1=Label(root,bg="black",text="UPDATE STUDENT",font=("Arial Rounded MT Bold",22),foreground ="white")
        label_roll1=Label(root,bg="black",text="Roll Number :",font=("Arial bold",12),width=11,fg='white')
        label_a1=Label(root,bg="black",text="Session :",font=("Arial bold",12),width=11,fg="white")
        label_b1=Label(root,bg="black",text="First Name :",font=("Arial bold",12),width=11,fg='white')
        label_c1=Label(root,bg="black",text="Last Name :",font=("Arial bold",12),width=11,fg='white')
        label_d1=Label(root,bg="black",text="Class :",font=("Arial bold",12),width=11,fg="white")
        label_e1=Label(root,bg="black",text="Section :",font=("Arial bold",12),width=11,fg="white")
        label_f1=Label(root,bg="black",text="Gender :",font=("Arial bold",12),width=11,fg="white")
        label_g1=Label(root,bg="black",text="Father Name :",font=("Arial bold",12),width=11,fg="white")
        label_h1=Label(root,bg="black",text="Mother Name :",font=("Arial bold",12),width=11,fg="white")
        label_i1=Label(root,bg="black",text="Mobile :",font=("Arial bold",12),width=11,fg="white")
        label_j1=Label(root,bg="black",text="Address :",font=("Arial bold",12),width=11,fg="white")
        
        global roll1
        global aa1
        global bb1
        global cc1
        global dd1
        global ee1
        global ff1
        global gg1
        global hh1
        global ii1
        global jj1
        
       
        roll1=Entry(root,textvariable=roll1,width=17,bd=4)  #roll no
                
        aa1 = ttk.Combobox(root,width=15)    # Session entry
        aa1['values']= ("SELECT","2015-16","2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23")
        aa1.current(0) #set the selected item
        
        bb1=Entry(root,textvariable=fn,width=17,bd=4)    # first name
        
        cc1=Entry(root,textvariable=ln,width=17,bd=4)    # last name
        
        dd1 = ttk.Combobox(root,width=15)    # class name
        dd1['values']= ("SELECT","NURSERY","LKG","UKG",1, 2, 3, 4, 5,6,7,8,9,10,11,12)
        dd1.current(0) #set the selected item
        
        ee1 = ttk.Combobox(root,width=15)    # section name
        ee1['values']= ("A","B","C","D","E")
        ee1.current(0) #set the selected item
        
        ff1 = ttk.Combobox(root,width=15)    # gender
        ff1['values']= ("SELECT","Male","Female")
        ff1.current(0) #set the selected item
        
        gg1=Entry(root,textvariable=fa_name,width=17,bd=4)    # father name
        
        hh1=Entry(root,textvariable=mo_name,width=17,bd=4)    # mother name
        
        ii1=Entry(root,textvariable=mob,width=17,bd=4)    # mobile
        
        jj1=Entry(root,textvariable=ad,width=17,bd=4)    # address
        
        
        # Placing Heading and Lables
        heading1.place(x=40,y=0)
        label_roll1.place(x=15,y=51)
        label_a1.place(x=15,y=83)
        label_b1.place(x=15,y=110)
        label_c1.place(x=15,y=142)
        label_d1.place(x=15,y=173)
        label_e1.place(x=15,y=200)
        label_f1.place(x=15,y=228)
        label_g1.place(x=15,y=256)
        label_h1.place(x=15,y=288)
        label_i1.place(x=15,y=320)
        label_j1.place(x=15,y=352)
        
        
        # Placing Entry boxes, buttons and Combo boxes on "UPDATE STUDENT" tkinter window
        roll1.place(x=200,y=51)   
        aa1.place(x=200,y=83)
        bb1.place(x=200,y=110)
        cc1.place(x=200,y=142)
        dd1.place(x=200,y=173)
        ee1.place(x=200,y=200)
        ff1.place(x=200,y=228)
        gg1.place(x=200,y=256)
        hh1.place(x=200,y=288)
        ii1.place(x=200,y=320)
        jj1.place(x=200,y=352)
        
     
        b3=Button(root,text="UPDATE",command=lambda :update_student(),width=38,background = 'deep sky blue', foreground ="purple",font=("Arial Rounded MT Bold",11),bd=5)
        b3.place(x=2,y=400)    
    
        b4=Button(root,text="GO TO HOME PAGE",command=lambda: root.destroy() ,width=38,background = 'deep sky blue', foreground ="red",font=("Arial Rounded MT Bold",11),bd=5)
        b4.place(x=2,y=440)
       
        root.mainloop()
        
    
    # "DELETE STUDENT" Window =================================================
    def delete_st():
        root=Tk()
        w=360
        h=332
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title("DELETE STUDENT INFORMATION")
        root.configure(bg="black")
        root.resizable(0,0)
        
        heading2=Label(root,bg="black",text="DELETE STUDENT",font=("Arial Rounded MT Bold",22),foreground ="white")
        label_delete=Label(root,bg="black",text="Roll Number :",font=("Arial bold",12),width=10,fg="white")
        
        global entry_delete
        entry_delete=Entry(root,textvariable=roll_delete,font=("Arial",12),width=17,bd=4)
        
        # Placing heading, label, entry box and buttons
        heading2.place(x=50,y=10)
        label_delete.place(x=130,y=85)
        entry_delete.place(x=100,y=122)

        b5=Button(root,text="DELETE",command=lambda: delete_student(),width=38,background = 'deep sky blue', foreground ="purple",font=("Arial Rounded MT Bold",11),bd=5)
        b5.place(x=2,y=250)
        b6=Button(root,text="GO TO HOME PAGE",command=lambda: root.destroy() ,width=38,background = 'deep sky blue', foreground ="red",font=("Arial Rounded MT Bold",11),bd=5)
        b6.place(x=2,y=290)
        root.mainloop()
        
        
        
    dashboard=Label(root,bg="khaki",text=" Dashboard ",font=("Arial bold",20),foreground="dark green")
    dashboard.place(x=620,y=100)

    # "VIEW ALL" button to display all  existing students' records--------
    view=Button(root,text="VIEW ALL",background = 'cyan', foreground ="brown",command=lambda: view_student(),width=10,font=("Arial bold",11),bd=6)
    view.place(x=31,y=165)

    # "NEW" button to open "ADD STUDENT" tkinter window--------
    add=Button(root,text="NEW",command=lambda: add_st(),width=10,background = 'cyan', foreground ="brown",font=("Arial bold",11),bd=6)
    add.place(x=220,y=165)

    # "UPDATE" button to open "UPDATE STUDENT" tkinter window-----
    update=Button(root,text="UPDATE",command=lambda: update_st(),width=10,background = 'cyan', foreground ="brown",font=("Arial bold",11),bd=6)
    update.place(x=420,y=165)

    # "DELETE" button to open "DELETE STUDENT" tkinter window
    delete=Button(root,text="DELETE",command=lambda: delete_st(),width=10,background = 'cyan', foreground ="brown",font=("Arial bold",11),bd=6)
    delete.place(x=620,y=165)

    # Open scrollable pane on the main window---------------
    txt = scrolledtext.ScrolledText(root,width=160,height=30,background = '#fff8dc', foreground ="black",font=("Aria bold",11))
    txt.place(x=30,y=205)
        
    # "SAVE AS SPREADSHEET" button to save students' existing record as a spreadsheet
    save=Button(root,text="Save As Spreadsheet",command=saveFile,width=18,background = 'skyblue', foreground ="black",font=("Arial bold",11),bd=8)
    save.place(x=1109,y=660)

    # Filter Student Records Classwise ---------------
    combo_class = ttk.Combobox(root,width=15)    
    combo_class['values']= ("CLASS","NURSERY","LKG","UKG",1, 2, 3, 4, 5,6,7,8,9,10,11,12)
    combo_class.current(0) #set the selected item
    combo_class.place(x=1107,y=173)

    combo_class_button=Button(root,text="SEARCH",command=classwise,width=10,background = 'cyan', foreground ="brown",font=("Arial bold",11),bd=6)
    combo_class_button.place(x=1222,y=165)

    root.mainloop()