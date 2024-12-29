from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import datetime
import time
import sv_ttk



class Train:

#=========================================== Gui Widget Structure ========================================================
    def __init__(self,root):
        self.root = root
        self.root.title("Advanced Train Management System")
        self.root.geometry("1920x1080+0+0")
        # self.root.config)

        MainFrame = Frame(self.root,width=1350,height=700,bd=10,relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame,width=1340,height=100,bd=10,relief=RIDGE)
        TopFrame1.grid()

        TopFrame2 = Frame(MainFrame,width=1300,height=500,bd=10,relief=RIDGE)
        TopFrame2.grid()

        f1 = Frame(TopFrame2,width=890,height=500,bd=5,relief=RIDGE)
        f1.grid(row=1,column=0)

        f2 = Frame(TopFrame2,width=400,height=500,pady=2,bd=5,relief=RIDGE)
        f2.grid(row=1,column=1)

        frametopRight = Frame(f2,width=404,height=420,bd=5,relief=RIDGE)
        frametopRight.pack(side=TOP)
        frameBottomRight = Frame(f2,width=408,height=100,bd=5,pady=15,relief=RIDGE)
        frameBottomRight.pack(side=BOTTOM)

        f1a = Frame(f1,width=900,height=330,bd=5,relief=RIDGE)
        f1a.pack(side=TOP)
        f2a = Frame(f1,width=900,height=320,bd=5,relief=RIDGE)
        f2a.pack(side=BOTTOM)

        topLeft1 = Frame(f1a,width=300,height=200,bd=5,padx=20,pady=1,relief=RIDGE)
        topLeft1.pack(side=LEFT)
        topLeft2 = Frame(f1a,width=300,height=200,bd=5,relief=RIDGE)
        topLeft2.pack(side=RIGHT)
        topLeft3 = Frame(f1a,width=300,height=200,bd=5,pady=12,relief=RIDGE)
        topLeft3.pack(side=RIGHT)

        bottomLeft1 = Frame(f2a,width=450,height=300,bd=5,pady=12,relief=RIDGE)
        bottomLeft1.pack(side=LEFT)

        bottomLeft2 = Frame(f2a,width=450,height=300,bd=5,relief=RIDGE)
        bottomLeft2.pack(side=RIGHT)

        lblTitle = Label(TopFrame1,font=("arial",40,"bold"),text="Train Ticketing Systems",bd=5,width=41,padx=4,justify="center")
        lblTitle.grid(row=0,column=0)

#=============================================== Variables Declaration ===============================================================
        date1 = StringVar()
        time1 = StringVar()
        Ticketclass = StringVar()
        TicketPrice = StringVar()
        Child_Ticket = StringVar()
        Adult_Ticket = StringVar()
        From_Destination = StringVar()
        To_Destination = StringVar()
        Fee_Price = StringVar()
        Route = StringVar()
        Receipt_Ref = StringVar()

        text_Input = StringVar()
        global operator
        operator = ""


        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = StringVar()
        var7 = StringVar()
        var8 = StringVar()
        var9 = StringVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()

        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()

        Ticketclass.set("")
        TicketPrice.set("")
        Child_Ticket.set("")
        Adult_Ticket.set("")
        From_Destination.set("")
        To_Destination.set("")
        Fee_Price.set("")
        Route.set("")
        Receipt_Ref.set("")

        var1.set("0")
        var2.set("0")
        var3.set("0")
        var4.set("0")
        var5.set("0")
        var6.set("0")
        var7.set("0")
        var8.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
#=========================================Label Widget =====================================================================================
        lblReceipt = Label(frametopRight,font=("arial",18,"bold"),text="Traveling Ticketing Systems",bd=5,pady=10,padx=5,width=42,justify="center")
        lblReceipt.grid(row=0,column=0)

        lblClass1 = Label(frameBottomRight,font=("arial",14,"bold"),text="Class",width= 15,relief="sunken",justify="center")
        lblClass1.grid(row=0,column=0)

        lblClass2 = Label(frameBottomRight,font=("arial",14,"bold"),textvariable=Ticketclass,width= 15,relief="sunken",justify="center")
        lblClass2.grid(row=1,column=0)

        lblTicket1 = Label(frameBottomRight,font=("arial",14,"bold"),text="Ticket",width= 15,relief="sunken",justify="center")
        lblTicket1.grid(row=0,column=1)

        lblTicket2 = Label(frameBottomRight,font=("arial",14,"bold"),textvariable=TicketPrice,width= 15,relief="sunken",justify="center")
        lblTicket2.grid(row=1,column=1)

        lblAdult1 = Label(frameBottomRight,font=("arial",14,"bold"),text="Adult",width= 15,relief="sunken",justify="center")
        lblAdult1.grid(row=0,column=2)

        lblAdult2 = Label(frameBottomRight,font=("arial",14,"bold"),textvariable=Adult_Ticket,width= 15,relief="sunken",justify="center")
        lblAdult2.grid(row=1,column=2)

        lblChild1 = Label(frameBottomRight,font=("arial",14,"bold"),text="Child",width= 15,relief="sunken",justify="center")
        lblChild1.grid(row=0,column=3)

        lblChild2 = Label(frameBottomRight,font=("arial",14,"bold"),textvariable=Child_Ticket,width= 15,relief="sunken",justify="center")
        lblChild2.grid(row=1,column=3)

#=========================================Space =====================================================================================
        lblsp=Label(frameBottomRight,font=("arial",14,"bold"),width= 62,height=2,bd=0,relief="sunken")
        lblsp.grid(row=2,column=0,columnspan=4)
#========================================= From widget =====================================================================================
        lblFrom1 = Label(frameBottomRight,font=("arial",14,"bold"),text="From",width=15,relief="sunken",justify="center")
        lblFrom1.grid(row=3,column=1)
        lblFrom2 = Label(frameBottomRight,font=("arial",14,"bold"),textvariable=From_Destination,width=15,relief="sunken",justify="center")
        lblFrom2.grid(row=3,column=2)
#=========================================To,Price widget =====================================================================================
        lblTo1 = Label(frameBottomRight, font=("arial", 14, "bold"), text="To", width=15, relief="sunken",justify="center")
        lblTo1.grid(row=4, column=1)
        lblTo2 = Label(frameBottomRight, font=("arial", 14, "bold"), textvariable=To_Destination, width=15, relief="sunken",justify="center")
        lblTo2.grid(row=4, column=2)

        lblPrice1 = Label(frameBottomRight, font=("arial", 14, "bold"), text="Price", width=15, relief="sunken",justify="center")
        lblPrice1.grid(row=5, column=1)
        lblPrice2 = Label(frameBottomRight, font=("arial", 14, "bold"), textvariable=Fee_Price, width=15, relief="sunken",justify="center")
        lblPrice2.grid(row=5, column=2)

#=========================================Space =====================================================================================
        lblsp=Label(frameBottomRight,font=("arial",14,"bold"),width= 62,height=2,bd=0,relief="sunken")
        lblsp.grid(row=6,column=0,columnspan=4)                                                                                          

#=========================================RefNo widget =====================================================================================
        lblRefNo1 = Label(frameBottomRight, font=("arial", 14, "bold"), text="Ref No", width=15, relief="sunken",justify="center")
        lblRefNo1.grid(row=7, column=0)
        lblRefNo2 = Label(frameBottomRight, font=("arial", 14, "bold"), textvariable=Receipt_Ref, width=15, relief="sunken",justify="center")
        lblRefNo2.grid(row=8, column=0)

        lblTime1 = Label(frameBottomRight, font=("arial", 14, "bold"), text="Time", width=15, relief="sunken",justify="center")
        lblTime1.grid(row=7, column=1)
        lblTime2 = Label(frameBottomRight, font=("arial", 14, "bold"), textvariable=time1, width=15, relief="sunken",justify="center")
        lblTime2.grid(row=8, column=1)

        lblDate1 = Label(frameBottomRight, font=("arial", 14, "bold"), text="Date", width=15, relief="sunken",justify="center")
        lblDate1.grid(row=7, column=2)
        lblDate2 = Label(frameBottomRight, font=("arial", 14, "bold"), textvariable=date1, width=15, relief="sunken",justify="center")
        lblDate2.grid(row=8, column=2)

        lblRoute1 = Label(frameBottomRight, font=("arial", 14, "bold"), text="Route", width=15, relief="sunken",justify="center")
        lblRoute1.grid(row=7, column=3)
        lblRoute2 = Label(frameBottomRight, font=("arial", 14, "bold"), textvariable=Route, width=15, relief="sunken",justify="center")
        lblRoute2.grid(row=8, column=3)

#============================================= Date Var Format Setup ==========================================================================
        date1.set(time.strftime("%d/%m/%Y")) #Date
        time1.set(time.strftime("%H:%M:%S")) #TIME

#==============================================Select Class==============================================================================================
        lblClass = (Label(topLeft1,font=("arial",14,"bold"),text="Class",bd=10,width=22,height=3)).grid(row=0,column=0,sticky=W)
        chkStandard = (Checkbutton(topLeft1,font=("arial",14,"bold"),text="Standard",height=3,variable=var1,onvalue=1,offvalue=0)).grid(row=1,column=0,sticky=W)
        chkEconomy = (Checkbutton(topLeft1, font=("arial",14,"bold"), text="Economy",height=3, variable=var2, onvalue=1,
                                   offvalue=0)).grid(row=2, column=0, sticky=W)
        chkFirstClass = (Checkbutton(topLeft1, font=("arial",14,"bold"), text="First Class",height=3, variable=var3, onvalue=1,
                                   offvalue=0)).grid(row=3, column=0, sticky=W)

        # ==============================================Select Destination==============================================================================================
        lblSelect = (Label(topLeft3, font=("arial",14,"bold"), text="Select Destination", bd=10,height=3)).grid(row=0, column=0, sticky=W,columnspan=2)
        lblDestination = (Label(topLeft3, font=("arial",14,"bold"), text="Destination", bd=10,height=3)).grid(row=1, column=0, sticky=W)
        combDestination = ttk.Combobox(topLeft3,textvariable=var9,font=("arial", 14, "bold"),height=3,state = "readonly",width=8)
        combDestination["value"] = ("","Kilburn","Preston","Oxford","Leeds","Brixton")
        combDestination.current(0)
        combDestination.grid(row=1, column=1)
        chkAdult = (Checkbutton(topLeft3, font=("arial",14,"bold"), bd=10,text="Adult", variable=var4, onvalue=1,
                                   offvalue=0)).grid(row=2, column=0, sticky=W)
        chkChild = (Checkbutton(topLeft3, font=("arial",14,"bold"), bd=10,text="Child", variable=var5, onvalue=1,
                                  offvalue=0)).grid(row=3, column=0, sticky=W)
# =========================================== Ticket Type Widgets =================================================================================
        lblTicketType = (Label(topLeft2, font=("arial", 14, "bold"), text="Ticket Type", bd=10,height=3)).grid(row=0, column=0, sticky=W)
        chkSingle = (Checkbutton(topLeft2, font=("arial",14,"bold"),bd=10, text="Single", variable=var4, onvalue=1,
                                   offvalue=0,height=3)).grid(row=1, column=0, sticky=W)
        entSingle = (Entry(topLeft2, font=("arial", 14, "bold"), textvariable=var12, bd=10)).grid(row=1, column=1,
                                                                                                 sticky=W)
        chkReturn = (Checkbutton(topLeft2, font=("arial",14,"bold"), bd=10,text="Return", variable=var5, onvalue=1,
                                  offvalue=0)).grid(row=2, column=0, sticky=W)
        entReturn = (Entry(topLeft2, font=("arial", 14, "bold"), textvariable=var6, bd=10)).grid(row=2, column=1,
                                                                                                 sticky=W)
        lblComment = (Label(topLeft2, font=("arial", 14, "bold"), text="Comment", bd=10,height=2)).grid(row=3, column=0,
                                                                                                     sticky=W)
        entComment = (Entry(topLeft2, font=("arial", 14, "bold"), textvariable=var7, bd=10)).grid(row=3, column=1,
                                                                                                     sticky=W)

# =========================================== Tax,subtotal,total Widgets =================================================================================
        lblTax = (Label(bottomLeft1, font=("arial", 14, "bold"), text="State Tax", bd=8)).grid(row=0, column=0,
                                                                                                     sticky=W)
        entTax = (Entry(bottomLeft1, font=("arial", 14, "bold"), textvariable=Tax, bd=5,width=40)).grid(row=0, column=1,
                                                                                                 sticky=W)
        lblSubTotal = (Label(bottomLeft1, font=("arial", 14, "bold"), text="Sub Total", bd=8)).grid(row=1, column=0,
                                                                                                     sticky=W)
        entSubTotal = (Entry(bottomLeft1, font=("arial", 14, "bold"), textvariable=SubTotal, bd=5,width=40)).grid(row=1, column=1,
                                                                                                 sticky=W)
        lblTotal = (Label(bottomLeft1, font=("arial", 14, "bold"), text="Total", bd=8)).grid(row=2, column=0,
                                                                                                     sticky=W)
        entTotal = (Entry(bottomLeft1, font=("arial", 14, "bold"), textvariable=Total, bd=5,width=40)).grid(row=2, column=1,
                                                                                                 sticky=W)
# =========================================== Calculator widgets =================================================================================

        ############################################### Text Input ######################################################################################################

        self.txtDisplay = Entry(bottomLeft2, font=("arial", 22, "bold"),width=28,bg="powder blue", textvariable=text_Input,insertwidth=4,bd=5,justify="right")
        self.txtDisplay.grid(columnspan=4)
        self.txtDisplay.insert(0, "0")

################################################## Addition#####################################################################################################

        self.btn7 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="7",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(7))
        self.btn7.grid(row=2,column=0)

        self.btn8 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="8",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(8))
        self.btn8.grid(row=2,column=1)

        self.btn9 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="9",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(9))
        self.btn9.grid(row=2,column=2)

        Addition = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="+",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick("+"))
        Addition.grid(row=2,column=3)

###############################################Substraction ######################################################################################################

        self.btn4 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="4",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(4))
        self.btn4.grid(row=3,column=0)

        self.btn5 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="5",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(5))
        self.btn5.grid(row=3,column=1)

        self.btn6 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="6",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(6))
        self.btn6.grid(row=3,column=2)

        Subtraction = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="-",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick("-"))
        Subtraction.grid(row=3,column=3)

        ############################################### Multiplication ######################################################################################################

        self.btn1 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="1",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(1))
        self.btn1.grid(row=4,column=0)

        self.btn2 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="2",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(2))
        self.btn2.grid(row=4,column=1)

        self.btn3 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="3",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(3))
        self.btn3.grid(row=4,column=2)

        Multiplication = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="*",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick("*"))
        Multiplication.grid(row=4,column=3)

        ############################################### Division ######################################################################################################

        self.btn0 = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="0",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick(0))
        self.btn0.grid(row=5,column=0)

        self.btnClear = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="C",width=8,height=1,padx=2,pady=16,bd=2)
        self.btnClear.grid(row=5,column=1)

        Division = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="/",width=8,height=1,padx=2,pady=16,bd=2,command=lambda:btnClick("/"))
        Division.grid(row=5,column=2)

        self.btnEqual = Button(bottomLeft2,fg="red",bg="coral2",font=("arial",12,"bold"),text="=",width=8,height=1,padx=2,pady=16,bd=2)
        self.btnEqual.grid(row=5,column=3)



#=========================================== Button Widgets =================================================================================

        btnTotal = Button(frameBottomRight,fg="red",bg="coral2",font=("arial",14,"bold"),text="Total",width=5,height=1,padx=20,pady=16,bd=2)
        btnTotal.grid(row=10,column=0)

        btnClear = Button(frameBottomRight,fg="red",bg="coral2",font=("arial",14,"bold"),text="Clear",width=5,height=1,padx=20,pady=16,bd=2)
        btnClear.grid(row=10,column=1)

        btnReset = Button(frameBottomRight,fg="red",bg="coral2",font=("arial",14,"bold"),text="Reset",width=5,height=1,padx=20,pady=16,bd=2)
        btnReset.grid(row=10,column=2)

        btnExit = Button(frameBottomRight,fg="red",bg="coral2",font=("arial",14,"bold"),text="Exit",width=5,height=1,padx=20,pady=16,bd=2)
        btnExit.grid(row=10,column=3)


if __name__ == "__main__":
    root = Tk()
    application = Train(root)
    sv_ttk.set_theme("dark")
    root.mainloop()
