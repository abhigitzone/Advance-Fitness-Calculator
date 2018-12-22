from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Advance:

    def __init__(self,root):
        self.root = root
        self.root.title("Advance Fitness Calcultor")
       # self.root.geometry("1350*750")
        self.root.configure(background='powder blue')

        MType = StringVar()
        Age = StringVar()
        Title = StringVar()
        Firstname = StringVar()
        Address1 = StringVar()
        Height = StringVar()
        Weight = StringVar()
        Gender = StringVar()
        BMI= StringVar()
        MemberID = StringVar()
        CalorieIntake = StringVar()
        work = StringVar()
        FatBurn = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        SellingPrice = StringVar()
        MetabolicRate = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()
        

        def iReset():
            MType.set("")
            Age.set("")
            Title.set("")
            Firstname.set("")
            Address1.set("")
            Height.set("")
            Weight.set("")
            Gender.set("")
            MemberID.set("")
            CalorieIntake.set("")
            FatBurn.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            MetabolicRate.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0",END)
            
        def iDisplayData():
            self.txtFrameDetail.insert(END)    
            
        def iReceipt():
            self.txtDisplayR.insert(END,'Membership: \t\t' + MType.get() + "\n")
            self.txtDisplayR.insert(END,'Age: \t\t' + Age.get() + "\n")
            self.txtDisplayR.insert(END,'Title: \t\t' + Title.get() + "\n")
            self.txtDisplayR.insert(END,'Name: \t\t' + Firstname.get() + "\n")
            self.txtDisplayR.insert(END,'Address 1: \t\t' + Address1.get() + "\n")
            self.txtDisplayR.insert(END,'Height: \t\t' + Height.get() + "\n")
            self.txtDisplayR.insert(END,'Weight: \t\t' + Weight.get() + "\n")
            self.txtDisplayR.insert(END,'Member ID: \t\t' + MemberID.get() + "\n")
            self.txtDisplayR.insert(END,'Calorie Intake: \t\t' + CalorieIntake.get() + "\n")
            self.txtDisplayR.insert(END,'FatBurn: \t\t' + FatBurn.get() + "\n")
            

    

        def BMI():
            
            if(MType.get()==""or Age.get()==""or Firstname.get()==""or Address1.get()==""or Weight.get()==""):
                BMI =tkinter.messagebox.showwarning("Advance Fitness Calculator","Fill all necessary options")
            else :
                BMI=round(Weight.get() / (Height.get() * Height.get(), 2))
                #BMI =tkinter.messagebox.showwarning("Advance Fitness Calculator","Fill all necessary options" ,x)
                if iExit>0:
                    root.destroy()
                return



        #====================Frame==================

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width = 1350, padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle = Label(TitleFrame,width=39,font=('arial', 40,'bold'),text="\tAdvance Fitness Calculator\t",padx=12)
        self.lblTitle.grid()

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height = 50, padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame,bd=20, width = 1450,height=100, padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame,bd=20, width = 1300,height=400, padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame,bd=10, width = 800,height=350, padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Users Info:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame,bd=10, width = 450,height=300, padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Work Chart:")
        DataFrameRIGHT.pack(side=RIGHT)

        #=============================Widgets=============================

        self.lblMemberType = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Membership:",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0, sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT,font = ('arial',12,'bold'),state='readonly',textvariable = MType, width=23)
        self.cboMemberType['value']=('--','3 Month','6 Month','1 Year')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1, sticky=W)

        self.lblMemberID = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Member ID:",padx=2,pady=2)
        self.lblMemberID.grid(row=0,column=2, sticky=W)
        self.txtMemberID = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = MemberID,width=25)
        self.txtMemberID.grid(row=0,column=3)


        self.lblAge = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Age:",padx=2,pady=2)
        self.lblAge.grid(row=5,column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = Age,width=25)
        self.txtAge.grid(row=5,column=1)


        self.lblCalorieIntake = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Calorie Intake:",padx=2,pady=2)
        self.lblCalorieIntake.grid(row=1,column=2, sticky=W)
        self.txtCalorieIntake = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = CalorieIntake,width=25)
        self.txtCalorieIntake.grid(row=1,column=3)


        self.lblTitle = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=1,column=0, sticky=W)

        self.cboTitle = ttk.Combobox(DataFrameLEFT, state='readonly',font=('arial',12,'bold'),textvariable = Title,width=25)
        self.cboTitle['value']=('','Mr.','Miss.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=1,column=1)


        self.lblFatBurn = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Fat Burn:",padx=2,pady=2)
        self.lblFatBurn.grid(row=2,column=2, sticky=W)
        self.txtFatBurn = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = FatBurn,width=25)
        self.txtFatBurn.grid(row=2,column=3)


        self.lblFirstname = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Name:",padx=2,pady=2)
        self.lblFirstname.grid(row=2,column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = Firstname,width=25)
        self.txtFirstname.grid(row=2,column=1)

        self.lblDateBorrowed = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Date Joined:",padx=2,pady=2)
        self.lblDateBorrowed.grid(row=3,column=2, sticky=W)
        self.txtDateBorrowed = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = DateBorrowed,width=25)
        self.txtDateBorrowed.grid(row=3,column=3)


        #========================Account Combobox=========================
        self.lblBMI = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="BMI:",padx=2,pady=2)
        self.lblBMI.grid(row=8,column=0, sticky=W)
        self.txtBMI = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = BMI,width=25)
        self.txtBMI.grid(row=8,column=1)


        self.lblDateDue = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Required BMI:",padx=2,pady=2)
        self.lblDateDue.grid(row=4,column=2, sticky=W)
        self.txtDateDue = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = DateDue,width=25)
        self.txtDateDue.grid(row=4,column=3)

        self.lblAddress1 = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Address:",padx=2,pady=2)
        self.lblAddress1.grid(row=3,column=0, sticky=W)
        self.txtAddress1 = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = Address1,width=25)
        self.txtAddress1.grid(row=3,column=1)


        self.lblDaysOnLoan = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Blood Pressure:",padx=2,pady=2)
        self.lblDaysOnLoan.grid(row=5,column=2, sticky=W)
        self.txtDaysOnLoan = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = DaysOnLoan,width=25)
        self.txtDaysOnLoan.grid(row=5,column=3)


        self.lblHeight = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Height (m):",padx=2,pady=2)
        self.lblHeight.grid(row=6,column=0, sticky=W)
        self.txtHeight = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = Height,width=25)
        self.txtHeight.grid(row=6,column=1)


        self.lblMetabolicRate = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Metabolic Rate:",padx=2,pady=2)
        self.lblMetabolicRate.grid(row=6,column=2, sticky=W)
        self.txtMetabolicRate = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = MetabolicRate,width=25)
        self.txtMetabolicRate.grid(row=6,column=3)

        self.lblWeight = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Weight (kg):",padx=2,pady=2)
        self.lblWeight.grid(row=7,column=0, sticky=W)
        self.txtWeight = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = Weight,width=25)
        self.txtWeight.grid(row=7,column=1)


        self.lblDateOverDue = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Calorie Burn:",padx=2,pady=2)
        self.lblDateOverDue.grid(row=7,column=2, sticky=W)
        self.txtDateOverDue = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = DateOverDue,width=25)
        self.txtDateOverDue.grid(row=7,column=3)

        self.lblGender = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Gender:",padx=2,pady=2)
        self.lblGender.grid(row=4,column=0, sticky=W)

        self.cboGender = ttk.Combobox(DataFrameLEFT,font = ('arial',12,'bold'),state='readonly',textvariable = Gender, width=23)
        self.cboGender['value']=('--','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=4,column=1)


        self.lblSellingPrice = Label(DataFrameLEFT,font = ('arial',12,'bold'),text="Workout Price:",padx=2,pady=2)
        self.lblSellingPrice.grid(row=8,column=2, sticky=W)
        self.txtSellingPrice = Entry(DataFrameLEFT,font = ('arial',12,'bold'),textvariable = SellingPrice,width=25)
        self.txtSellingPrice.grid(row=8,column=3)

        #====================Button Add Acount==========================================================================
        self.btnAddAcount = Button(DataFrameLEFT,text='Calculate BMI',font = ('arial',12,'bold'),width=10,bd=4, command = BMI)
        self.btnAddAcount.grid(row=9,column=1)

        
        #======================================Widget============================================
        self.txtDisplayR = Text(DataFrameRIGHT,font = ('arial',12,'bold'),width=32, height=13,padx=8,pady=20)
        self.txtDisplayR.grid(row=0,column=2)



        #===============================Listbox=======================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')
        ListOfBooks = ['Cardio Exercise','Aerobic Exercise','Strength Exercise','Balance Exercise','Flexibility Exercise','Body Circuit Exercise','Body Building','Power Lifting']

        def WorkChart(evt):
            value =str(worklist.get(worklist.curselection()))
            #print(value)
            w = value

            if(w == "Cardio Exercise"):
                MemberID.set("YJ1234")
                CalorieIntake.set("2500 K/Cal")
                FatBurn.set("40 joule")
                DateDue.set("25")
                MetabolicRate.set("20 BMR")
                SellingPrice.set("$100")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("1 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)
                
                

            elif (w == "Aerobic Exercise"):
                MemberID.set("YJ3121")
                CalorieIntake.set("2230 K/Cal")
                FatBurn.set("30 joule")
                DateDue.set("21")
                MetabolicRate.set("20 BMR")
                SellingPrice.set("$80")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("2 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)

            elif (w == "Strength Exercise"):
                MemberID.set("YJ5631")
                CalorieIntake.set("3000 K/Cal")
                FatBurn.set("50 joule")
                DateDue.set("21")
                MetabolicRate.set("25 BMR")
                SellingPrice.set("$150")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("5 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)

            elif (w == "Balance Exercise"):
                MemberID.set("YJ5563")
                CalorieIntake.set("2211 K/Cal")
                FatBurn.set("30 joule")
                DateDue.set("15")
                MetabolicRate.set("20 BMR")
                SellingPrice.set("$50")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("1 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)

            elif (w == "Flexibility Exercise"):
                MemberID.set("YJ1234")
                CalorieIntake.set("1588 K/Cal")
                FatBurn.set("35 joule")
                DateDue.set("25")
                MetabolicRate.set("20 BMR")
                SellingPrice.set("$70")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("2 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)

            elif (w == "Body Circuit Traning"):
                MemberID.set("YJ4556")
                CalorieIntake.set("3400 K/Cal")
                FatBurn.set("60 joule")
                DateDue.set("30")
                MetabolicRate.set("20 BMR")
                SellingPrice.set("$200")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("4 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)

            elif (w == "Body Building"):
                MemberID.set("YJ8765")
                CalorieIntake.set("3000 K/Cal")
                FatBurn.set("50 joule")
                DateDue.set("25")
                MetabolicRate.set("22 BMR")
                SellingPrice.set("$300")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("6 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)

            elif (w == "Power Lifting"):
                MemberID.set("YJ6774")
                CalorieIntake.set("3500 K/Cal")
                FatBurn.set("40 joule")
                DateDue.set("25")
                MetabolicRate.set("20 BMR")
                SellingPrice.set("$500")
                DaysOnLoan.set("120/80 mmHg")
                DateOverDue.set("1 Pound a week")
                
                iReceipt()

                import datetime

                d1 = datetime.date.today()
                DateBorrowed.set(d1)
                
        worklist = Listbox(DataFrameRIGHT, width=20, height=12,font = ('arial',12,'bold'))
        worklist.bind('<<ListboxSelect>>',WorkChart)
        worklist.grid(row=0, column=0,padx=8)
        scrollbar.config(command=worklist.yview)

        for items in ListOfBooks:
            worklist.insert(END,items)
        
       

        #============================================Button=================================================

        self.btnDisplayData = Button(ButtonFrame,text='Display Data',font = ('arial',12,'bold'),width=30,bd=4,command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=0)

        '''self.btnDelete = Button(ButtonFrame,text='Delete',font = ('arial',12,'bold'),width=30,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=1)'''

        self.btnReset = Button(ButtonFrame,text='Reset',font = ('arial',12,'bold'),width=30,bd=4, command = iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit = Button(ButtonFrame,text='Exit',font = ('arial',12,'bold'),width=30,bd=4, command = iExit)
        self.btnExit.grid(row=0,column=3)





if __name__=='__main__':
    root = Tk()
    application = Advance(root)
    root.mainloop
