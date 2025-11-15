from tkinter import *
from tkinter import ttk
from persiantools.jdatetime import JalaliDate
from BE.bePersonal import Personal, BakPersonal
from BE.bePersonal import Login
from BL.blPersonal import blPersonal, blBakPersonal
import customtkinter
import customtkinter as ctk
import time
import threading
from tkinter import messagebox
from datetime import datetime
import jdatetime




class App(Frame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen
        self.CreateWidget()
    #تابع المان ها و ویجت های صفحه
    def CreateWidget(self):
        #استایل دادن به المان هایی که با ttk
        style=ttk.Style()
        style.theme_use("xpnative")

        self.outtime=[]

        custom_font = ("Nazanin", 15)
        hilight_font=("Tahoma", 10)
        Title_font= ("Nazanin", 30,"bold")
        Header3_font= ("Nazanin", 15,"bold")
        Header2_font = ("Nazanin", 10, "bold")
        #Images/تصاویر
        self.img1=PhotoImage(file="img/lng2.png")
        self.img2=PhotoImage(file="img/lng5.png")
        self.img4=PhotoImage(file="img/p2.png")
        self.img5=PhotoImage(file="img/ln3.png")
        self.Exit_1 = PhotoImage(file="img/Exit.png")
        self.Search_1 = PhotoImage(file="img/search.png")
        self.TimeSet_1= PhotoImage(file="img/stopwatch.png")
        self.Report_1 = PhotoImage(file="img/report.png")


        #Labels/لیبل ها
        self.lblId = customtkinter.CTkLabel(self.master, text="شناسه", font=custom_font).place(x=1100, y=50)
        self.lblName=customtkinter.CTkLabel(self.master,text="نام",font=custom_font).place(x=1100,y=90)
        self.lblFamily=customtkinter.CTkLabel(self.master,text="نام خانوادگی",font=custom_font).place(x=1100,y=130)
        self.lblAge=customtkinter.CTkLabel(self.master,text="سن",font=custom_font).place(x=1100,y=170)
        self.lblDate=customtkinter.CTkLabel(self.master,text="تاریخ ثبت نام",font=custom_font).place(x=1100,y=210)
        self.lblielts =customtkinter.CTkLabel(self.master, text="تمرین آیلتس",font=custom_font).place(x=1100, y=250)
        self.lblPriceG =customtkinter.CTkLabel(self.master, text="40000", justify="center",font=custom_font)
        self.lblPriceG.place(x=1015, y=250)
        self.lblPriceAllG =ttk.Label(self.master, text="0", justify="center",font=custom_font)
        self.lblPriceAllG.place(x=950, y=250)
        self.lblspeaking =customtkinter.CTkLabel(self.master, text="تمرین اسپیکینگ",font=custom_font).place(x=1100, y=300)
        self.lblPriceH =ttk.Label(self.master, text="30000", justify="center", width=4,font=custom_font)
        self.lblPriceH.place(x=1015, y=300)
        self.lblPriceAllH =ttk.Label(self.master, text="0", justify="center", width=7,font=custom_font)
        self.lblPriceAllH.place(x=950, y=300)
        self.lblPriceAll =customtkinter.CTkLabel(self.master, text=":هزینه کل",font=custom_font).place(x=1100, y=350)
        self.FactorPrice =ttk.Label(self.master, text="0",font=custom_font)
        self.FactorPrice.place(x=1000, y=350)
        self.lbl1=customtkinter.CTkLabel(self.master,text="برای ثبت نام اپراتور جدید",font=custom_font)
        self.lbl1.place_forget()
        self.lbl2=customtkinter.CTkLabel(self.master,text="اینجا",text_color="#854bcf", font=Header3_font)
        #نوشتن بایند برای لیبل lbl2 که با کلیک روی "اینجا" و اجرای تابع self.ShowFrmReg
        self.lbl2.bind("<Button-1>",self.ShowFrmReg)
        self.lbl2.place_forget()
        self.lbl3=customtkinter.CTkLabel(self.master,text="کلیک کنید",font=custom_font)
        self.lbl3.place_forget()
        self.lblimg4=customtkinter.CTkLabel(self.master,text="",image=self.img4).place(x=900,y=500)
        self.lblRem=customtkinter.CTkLabel(self.master,text="جلسات باقیمانده",text_color="#854bcf",font=custom_font).place(x=750,y=60)
        self.lblRemg=customtkinter.CTkLabel(self.master,text="آیلتس",font=custom_font).place(x=870,y=100)
        self.lblRemh=customtkinter.CTkLabel(self.master,text="اسپیکینگ",font=custom_font).place(x=870,y=140)


        #Search Frame/فریم سرچ
        self.frmReport = Frame(self.master, height=800, width=600, background="#cae5f9")
        self.frmReport.place_forget()
        # Report
        self.btnPrReport1 = customtkinter.CTkButton(self.frmReport, text="اجرای گزارش بازه ای",fg_color="#854bcf",
                                                    command=self.OnClickPrReport,
                                                    font=Header3_font)
        self.btnPrReport1.place_forget()

        self.frmSearch = Frame(self.master, height=800, width=600,background="#ffefcc")
        self.frmSearch.place(x=20, y=40)
        self.btnRestore = customtkinter.CTkButton(self.master, text="بازگردانی داده", fg_color="#bb87ff",
                                                  command=self.OnClickRestore,
                                                  font=Header3_font)
        self.btnRestore.place(x=1025, y=470)
        self.lblimg1=customtkinter.CTkLabel(self.frmSearch,text="",image=self.img1)
        self.lblimg1.place(x=0,y=0)
        self.btnSearch = customtkinter.CTkButton(self.frmSearch, text="",image=self.Search_1, command=self.OnClickSearch,width=5,font=custom_font)
        self.btnSearch.place(x=250, y=12)
        self.lblSearch =customtkinter.CTkLabel(self.frmSearch, text="عبارت جستجو را وارد کنید",font=custom_font)
        self.lblSearch.place_forget()
        self.btnPrReport2 = customtkinter.CTkButton(self.master, text="گزارش گیری",fg_color="#4ad295",
                                                    command=self.OnClickShowReport,image=self.Report_1,
                                                    font=Header3_font)
        self.btnPrReport2.place_forget()

        self.btnPrclose = customtkinter.CTkButton(self.frmReport, text="برگشت به صفحه اصلی",fg_color="#8973ff",
                                                    command=self.OnClickCloseReport,
                                                    font=Header3_font)
        #Reminder

        #Vars/متغیرها
        self.Id=IntVar()
        self.Name=StringVar()
        self.Family=StringVar()
        self.Age=StringVar()
        self.Date=StringVar()
        self.ielts=IntVar()
        self.speaking=IntVar()
        self.Search=StringVar()
        self.Report=StringVar()
        self.Remielts=StringVar()
        self.Remspeaking=StringVar()
        self.radio=IntVar()
        self.User=StringVar()
        self.Pass=StringVar()
        self.IsAdmin=IntVar()
        self.DateStart=StringVar()
        self.DateEnd=StringVar()
        self.Restore=StringVar()
        self.btnRemind = customtkinter.CTkButton(self.master, text="تنظیم زمان",fg_color="#ff9109",image=self.TimeSet_1,width=10, command=self.reminderShow,
                                                 font=Header3_font)
        self.btnRemind.place(x=40, y=300)
        self.txtRestore = customtkinter.CTkEntry(self.master, textvariable=self.Restore,width=50, font=Header3_font)
        self.txtRestore.configure(placeholder_text_color="light_color")
        self.txtRestore.insert(0, "ID")
        self.txtRestore.place(x=970,y=470)


        # گزارش بازه ای براساس تاریخ
        self.txtDateStart = customtkinter.CTkEntry(self.frmReport, textvariable=self.DateStart, font=custom_font)
        self.txtDateStart.configure(placeholder_text_color="light_color")
        self.txtDateStart.insert(0, "YYYY-MM-DD")

        self.txtDateEnd = customtkinter.CTkEntry(self.frmReport, textvariable=self.DateEnd, font=custom_font)
        self.txtDateEnd.configure(placeholder_text_color="light_color")
        self.txtDateEnd.insert(0, "YYYY-MM-DD")
        #Entry/باکس متن
        self.txtReport = customtkinter.CTkEntry(self.frmSearch, textvariable=self.Report, font=custom_font)
        self.txtReport.configure(placeholder_text_color="light_color")
        self.txtReport.place_forget()
        self.txtId = customtkinter.CTkEntry(self.master, textvariable=self.Id, font=custom_font)
        self.txtId.configure(placeholder_text_color="light_color")
        self.txtId.place(x=950, y=50)
        self.txtName=customtkinter.CTkEntry(self.master,textvariable=self.Name,font=custom_font)
        self.txtName.configure(placeholder_text_color="light_color")
        self.txtName.place(x=950,y=90)

        self.txtFamily = customtkinter.CTkEntry(self.master, textvariable=self.Family,font=custom_font)
        self.txtFamily.configure(placeholder_text_color="light_color")
        self.txtFamily.place(x=950, y=130)

        self.txtAge = customtkinter.CTkEntry(self.master, textvariable=self.Age,font=custom_font)
        self.txtAge.configure(placeholder_text_color="light_color")
        self.txtAge.place(x=950, y=170)

        self.txtDate = customtkinter.CTkEntry(self.master, textvariable=self.Date,font=custom_font)
        self.txtDate.configure(placeholder_text_color="light_color")
        self.txtDate.insert(0,"YYYY-MM-DD")


        #زمانیکه روی اینترای txtDate کلیک شد متن داخلش پاک شه
        self.txtDate.bind("<FocusIn>",self.FocusInEntry)
        # زمانیکه از اینترای تاریخ جای دیگه کلیک شد مجدد متن داخلش نمایش داده شه
        self.txtDate.bind("<FocusOut>",self.FocusOutEntry)
        self.txtDate.place(x=950, y=210)

        self.txtSearch=customtkinter.CTkEntry(self.frmSearch,textvariable=self.Search)
        self.txtSearch.configure(placeholder_text_color="light_color")
        self.txtSearch.place(x=320, y=12)



        self.txtRemielts =customtkinter.CTkEntry(self.master, textvariable=self.Remielts)
        self.txtRemielts.configure(placeholder_text_color="light_color")
        self.txtRemielts.place(x=700, y=100)

        self.txtRemspeaking = customtkinter.CTkEntry(self.master, textvariable=self.Remspeaking)
        self.txtRemspeaking.configure(placeholder_text_color="light_color")
        self.txtRemspeaking.place(x=700, y=140)

        #Chombo/کمبوباکس تعداد جلسات در ماه
        self.Comboielts = ttk.Combobox(self.master, justify="center", width=3, state="readonly",
                                       textvariable=self.ielts,font=custom_font)
        self.Comboielts["value"] = list(range(0, 31))#حداکثر تعداد جلسات ورزش آیلتس
        self.Comboielts.set("0")
        self.Comboielts.place(x=1050, y=250)
        #انتخاب مقادیر کمبو و محاسبه هزینه
        self.Comboielts.bind("<<ComboboxSelected>>", lambda event: self.multiply(ComboNumber=1))

        self.Combospeaking = ttk.Combobox(self.master, justify="center", width=3, state="readonly",
                                          textvariable =self.speaking,font=custom_font)
        self.Combospeaking["value"] = list(range(0, 31))
        self.Combospeaking.set("0")
        self.Combospeaking.place(x=1050, y=300)
        self.Combospeaking.bind("<<ComboboxSelected>>", lambda event: self.multiply(ComboNumber=2))

        #لیست هزینه ها بر حسب تعداد جلسات هر آموزش(آیلتس/اسپیکینگ)
        self.PriceAll = [self.lblPriceAllG, self.lblPriceAllH]#هزینه کل
        self.Combo = [self.Comboielts, self.Combospeaking]#تعداد جلسات
        self.Price = [self.lblPriceG, self.lblPriceH]#هزینه هر جلسه

        #Buttons
        self.btnRegister=customtkinter.CTkButton(self.master,text="ثبت نام",fg_color="#20c997",command=self.OnClickRegister,font=Header3_font)
        #تغییر ظاهر دکمه ثبت نام بعد از امدن ماوس(برای سایر دکمه ها نیز نوشته شده)
        self.btnRegister.bind("<Enter>", self.ChangeShape)
        self.btnRegister.bind("<Leave>", self.ResetShape)
        self.btnRegister.place(x=1025,y=380)

        self.btnDelete=customtkinter.CTkButton(self.master,text="حذف",fg_color="#f96262",command=self.OnClickDelete,font=Header3_font)
        self.btnDelete.bind("<Enter>", self.ChangeShape)
        self.btnDelete.bind("<Leave>", self.ResetShape)
        self.btnDelete.place(x=1025,y=440)

        self.btnEdit = customtkinter.CTkButton(self.master, text="ویرایش",fg_color="#62c1f9", command=self.OnClickEditDy,font=Header3_font)
        self.btnEdit.bind("<Enter>",self.ChangeShape)
        self.btnEdit.bind("<Leave>",self.ResetShape)
        self.btnEdit.place(x=1025, y=410)
        #دکمه حضوروغیاب
        self.btnEdit = customtkinter.CTkButton(self.master,fg_color="#28a745", text="حضور",width=15, command=self.present,font=Header3_font)
        self.btnEdit.bind("<Enter>", self.ChangeShape)
        self.btnEdit.bind("<Leave>", self.ResetShape)
        self.btnEdit.place(x=755, y=230)

        self.btnExit = customtkinter.CTkButton(self.master,fg_color="#ffffff",font=Header3_font,image=self.Exit_1, command=self.Exit)
        self.btnExit.place(x=1150, y=5)



        # Checkbox/چک باکس
        self.radioielts =  customtkinter.CTkRadioButton(self.master, text="آیلتس",variable=self.radio,value=1)
        self.radioielts.place(x=705, y=180)
        self.radiospeaking = customtkinter.CTkRadioButton(self.master, text="اسپیکینگ",variable=self.radio,value=0).place(x=755, y=180)

        #tbls/جدول مشخصات ورزشکاران ثبت نام شده
        self.tbl = ttk.Treeview(self.master, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show="headings",height=15)
        self.tbl.heading("#9",text="شماره")
        self.tbl.column("#9",width=70,anchor=E)
        self.tbl.heading("#8", text="نام")
        self.tbl.column("#8", width=50, anchor=E)
        self.tbl.heading("#7", text="نام خانوادگی", anchor=S)
        self.tbl.column("#7", width=80, anchor=E)
        self.tbl.heading("#6", text="سن", anchor=S)
        self.tbl.column("#6", width=50, anchor=E)
        self.tbl.heading("#5", text="تاریخ ثبت نام", anchor=S)
        self.tbl.column("#5", width=80, anchor=E)
        self.tbl.heading("#4", text="کل جلسات آیلتس"
                                    ""
                                    "", anchor=S)
        self.tbl.column("#4", width=100, anchor=E)
        self.tbl.heading("#3", text="کل جلسات اسپیکینگ", anchor=S)
        self.tbl.column("#3", width=100, anchor=E)
        self.tbl.heading("#2", text="باقیمانده جلسات آیلتس", anchor=S)
        self.tbl.column("#2", width=130, anchor=E)
        self.tbl.heading("#1", text="باقیمانده جلسات اسپیکینگ", anchor=S)
        self.tbl.column("#1", width=130, anchor=E)
        self.tbl.place(x=40, y=350)
        self.tbl.bind("<Button-1>",self.GetSelection)
        #لیست برای محاسبات آتی زمان
        self.outtime=[]
        self.tbl.bind("<Map>", self.set_cell_color)

        self.Load()

        #FrameLogin/فریم لاگین برای اوپراتور های آموزشگاه
        self.frmLogin = Frame(self.master, height=700, width=1200, background="#e0e0e2")
        self.frmLogin.place(x=0, y=0)
        self.lblwellcome=customtkinter.CTkLabel(self.frmLogin,text="آموزشگاه آنلاین زبان",font=Title_font).place(x=500,y=50)
        self.lblUser=customtkinter.CTkLabel(self.frmLogin,text="نام کاربری",font=custom_font).place(x=750,y=215)
        self.lblPass=customtkinter.CTkLabel(self.frmLogin,text="رمز عبور",font=custom_font).place(x=750,y=265)
        self.txtUser=customtkinter.CTkEntry(self.frmLogin,textvariable=self.User)
        self.txtUser.configure(placeholder_text_color="light_color",font=custom_font)
        self.txtUser.place(x=550,y=215)
        self.txtPass =customtkinter.CTkEntry(self.frmLogin, textvariable=self.Pass,font=custom_font)
        self.txtPass.configure(placeholder_text_color="light_color",show="*")
        self.txtPass.place(x=550, y=265)

        #دکمه مخفی سازی و نمایش پسورد هنگام ورود
        self.btnShowPass=customtkinter.CTkButton(self.frmLogin,fg_color="#854bcf",width=30,text="نمایش/پنهان رمز",command=self.ShowPass,font=Header3_font)
        self.btnShowPass.place(x=600,y=340)
        '''self.button3=customtkinter.CTkButton(self.frmLogin,text="TESTTTT",command=self.Login())
        self.button3.place(x=450, y=300)
        ,font="nazanin 10",bg="#d5d7dd"'''
        self.btnLogin=customtkinter.CTkButton(self.frmLogin,width=35,fg_color="#4ad295",text="ورود",command=self.Login,font=Header3_font)
        self.btnLogin.place(x=550,y=340)
        #قرار دادن تصویر
        self.lblimg2=customtkinter.CTkLabel(self.frmLogin,text="",image=self.img2).place(x=300,y=200)
        print(self.User.get())
        #Frame NewUser/فریم ثبت نام اوپراتور جدید برای باشگاه
        self.frmReg = Frame(self.master, height=700, width=1200, background="#ffedcb")
        self.frmReg.place_forget()
        self.lblimg5=customtkinter.CTkLabel(self.frmReg,image=self.img5,text="").place(x=600,y=200)
        self.FullName=StringVar()
        self.UserReg=StringVar()
        self.PassReg=StringVar()
        self.lblUserReg =customtkinter.CTkLabel(self.frmReg, text="نام کاربری",font=Header2_font).place(x=400, y=220)
        self.lblPassReg =customtkinter.CTkLabel(self.frmReg, text="رمز عبور",font=Header2_font).place(x=400, y=270)
        self.lblIsAdmin = customtkinter.CTkLabel(self.frmReg, text="کاربر ارشد", font=Header2_font).place(x=400, y=320)
        self.lblFullNameReg=customtkinter.CTkLabel(self.frmReg,text="نام").place(x=400,y=170)
        self.txtFullName=customtkinter.CTkEntry(self.frmReg,textvariable=self.FullName)
        self.txtFullName.configure(placeholder_text_color="light_color",font=custom_font)
        self.txtFullName.place(x=220, y=170)

        self.txtUserReg =customtkinter.CTkEntry(self.frmReg, textvariable=self.UserReg,font=custom_font)
        self.txtUserReg.configure(placeholder_text_color="light_color")
        self.txtUserReg.place(x=220, y=220)

        self.txtPassReg =customtkinter.CTkEntry(self.frmReg, textvariable=self.PassReg,font=custom_font)
        self.txtPassReg.configure(placeholder_text_color="light_color")
        self.txtPassReg.place(x=220, y=270)
        self.txtPassReg.configure(show='*')

        self.txtIsAdmin = customtkinter.CTkEntry(self.frmReg, textvariable=self.IsAdmin, font=custom_font)
        self.txtIsAdmin.configure(placeholder_text_color="light_color")
        self.txtIsAdmin.place(x=220, y=320)
        self.btnRegister = customtkinter.CTkButton(self.frmReg,fg_color="#4ad295",width=10, text="ثبت نام", command=self.OnClickRegisterNewUser,font=custom_font)
        self.btnRegister.bind("<Enter>", self.ChangeShape)
        self.btnRegister.bind("<Leave>", self.ResetShape)
        self.btnRegister.place(x=220, y=360)

        self.btnRegister = customtkinter.CTkButton(self.frmReg, text="بازگشت", command=self.forgetReg,font=Header3_font)
        self.btnRegister.bind("<Enter>", self.ChangeShape)
        self.btnRegister.bind("<Leave>", self.ResetShape)
        self.btnRegister.place(x=1100, y=30)

        #Reminder Frame
        self.frmReminder=Frame(self.master,height=100, width=3000,background="#c8b3df")
        self.frmReminder.place_forget()
        self.datetime_label = ctk.CTkLabel(self.frmReminder, fg_color="#854bcf",font=("Nazanin", 10),text="تاریخ و ساعت را وارد کنید (YYYY-MM-DD HH:MM):")
        self.datetime_label.pack(pady=10)

        self.datetime_entry = ctk.CTkEntry(self.frmReminder)
        self.datetime_entry.pack(pady=10)

        # ورودی پیام
        self.message_label = ctk.CTkLabel(self.frmReminder, text="پیام یادآوری:")
        self.message_label.pack(pady=10)

        self.message_entry = ctk.CTkEntry(self.frmReminder)
        self.message_entry.pack(pady=10)

        # دکمه تنظیم ریمایندر
        self.set_button = ctk.CTkButton(self.frmReminder, fg_color="#854bcf",text="تنظیم یادآور", command=self.set_reminder)
        self.set_button.pack(pady=20)
        self.set_button = ctk.CTkButton(self.frmReminder,fg_color="#854bcf", text="بستن", command=self.ExitReminer)
        self.set_button.pack(pady=20)

    def set_reminder(self):
        reminder_datetime_str = self.datetime_entry.get()
        message = self.message_entry.get()

        try:
            # تبدیل رشته به تاریخ شمسی
            year, month, day_time = reminder_datetime_str.split("-")  # 1403-09-23
            day, time_str = day_time.split(" ")
            hour, minute = map(int, time_str.split(":"))
            reminder_datetime = jdatetime.datetime(int(year), int(month), int(day), hour, minute).togregorian()

            current_datetime = datetime.now()

            if reminder_datetime > current_datetime and message:
                # محاسبه زمان باقی‌مانده تا آلارم
                time_to_wait = (reminder_datetime - current_datetime).total_seconds()
                threading.Thread(target=self.remind, args=(time_to_wait, message)).start()
                self.datetime_entry.delete(0, ctk.END)
                self.message_entry.delete(0, ctk.END)
                messagebox.showinfo("یادآور تنظیم شد", f"یادآور برای {reminder_datetime} تنظیم شد.")  # تغییر این خط
            else:
                messagebox.showerror("خطا", "لطفاً یک تاریخ و پیام معتبر وارد کنید.")  # تغییر این خط
        except ValueError:
            messagebox.showerror("خطا",
                                 "لطفاً فرمت تاریخ و زمان را به درستی وارد کنید (YYYY-MM-DD HH:MM).")  # تغییر این خط

    def remind(self, seconds, message):
        time.sleep(seconds)
        messagebox.showinfo("یادآور", message)  # تغییر این خط





    #مخفی سازی فریم ثبت نام
    def forgetReg(self):
        self.frmReg.place_forget()
    #چک کردن اتمام تاریخ ورزشکاران
    def present(self):
        rg=self.Remielts.get()

        rh=self.Remspeaking.get()
        if int(self.Id.get()) in self.outtime:
            messagebox.showerror("خطا","مهلت جلسات کاربر از یک ماه گذشته مجدد ثبت نام کنید")
        else:
            if int(rg)==0 and int(rh)==0:
                messagebox.showerror("خطا", "تعداد جلسات کاربر تمام شده است مجدد ثبت نام کنید")
            else:
                self.presentone()

    #انتخاب جلسه اسپیکینگ یا آیلتس ورزشکار و چک کردن اتمام یا وجود جلسات باقی مانده
    def presentone(self):
        objbl = blPersonal()
        if int(self.radio.get()) == 1:
            result = messagebox.askyesno("حضور", f"{self.Name.get(), self.Family.get()}امروز یک جلسه آیلتس می خواهد؟")
            if result == True:
                if int(self.Remielts.get()) == 0:
                    messagebox.showerror("خطا", "تعداد جلسات آیلتس کاربر تمام شده است")
                else:
                    newRem = int(self.Remielts.get()) - 1
                    self.Remielts.set(str(newRem))
                    objbl.blUpdateDynamic(Personal, self.Id.get(), prs_remainder_ielts=self.Remielts.get())
                    self.Load()
        if int(self.radio.get()) == 0:
            result = messagebox.askyesno("حضور", f"{self.Name.get(), self.Family.get()}امروز یک جلسه اسپیکینگ می خواهد؟")
            if result == True:
                if int(self.Remspeaking.get()) == 0:
                    messagebox.showerror("خطا", "تعداد جلسات اسپیکینگ کاربر تمام شده است")
                else:
                    newRem = int(self.Remspeaking.get()) - 1
                    self.Remspeaking.set(str(newRem))
                    objbl.blUpdateDynamic(Personal, self.Id.get(), prs_remainder_speaking=self.Remspeaking.get())
                    self.Load()
    def set_cell_color(self,event):
        #l = ""
        for child in self.tbl.get_children():
            date_str = self.tbl.item(child)['values'][4]
            if self.calculate_date_difference(date_str) > 30:
                #l += "\n" + str(self.tbl.item(child)['values'][8])
                self.outtime.append(self.tbl.item(child)['values'][8])
                #lbl =customtkinter.CTkLabel(self.master, text=l).place(x=100, y=300)
    #محاسبه تاریخ باقیمانده ورزشکار
    def calculate_date_difference(self,date_str1):
        date_str = datetime.strptime(date_str1, "%Y-%m-%d")
        jalali_date=date_str
        jalali_today = JalaliDate.today()
        date1 = datetime(jalali_date.year, jalali_date.month, jalali_date.day)
        date2 = datetime(jalali_today.year, jalali_today.month, jalali_today.day)
        delta = date2 - date1
        return delta.days
    #نمایش فریم ثبت نام
    def ShowFrmReg(self,e):
        self.frmReg.place(x=0,y=0)
    #تابع خروج از صفحه اصلی و رفتن به صفحه لاگین
    def Exit(self):
        self.frmLogin.place(x=0, y=0)
        self.lblLoginUser.place_forget()
        self.User.set('')
        self.Pass.set('')
        self.txtUser.focus_set()
    def ExitReminer(self):
        self.frmReminder.place_forget()
    #تابع نمایش پسورد
    def ShowPass(self):
        if self.txtPass['show']=='*':
            self.txtPass.config(show='')
        else:
            self.txtPass.config(show='*')
    #تابع ورود


    def FocusInEntry(self,e):
        if self.txtDate.get()=="YYYY-MM-DD":
            self.txtDate.delete(0,"end")
            '''self.txtDate.configure(fg="white")'''

    def FocusOutEntry(self,e):
        if self.txtDate.get() == "":
            self.txtDate.insert(0,"YYYY-MM-DD")
            '''self.txtDate.configure(fg="#b8b8b8")'''
    #محاسبه هزینه جلسات ورزشکار
    def multiply(self, ComboNumber):
        self.PriceAll[ComboNumber - 1].config(
            text=int(self.Combo[ComboNumber - 1].get()) * int(self.Price[ComboNumber - 1].cget("text")))

        # FactorPriceAll
        sum = 0
        for item in self.PriceAll:
            sum += int(item.cget("text"))
        self.FactorPrice.config(text=str(sum) + "تومان")

    #ثبت نام ورزشکار
    def OnClickRegister(self):
        jdate=jdatetime.datetime.strptime(self.Date.get(), "%Y-%m-%d").togregorian().date()
        if self.Name.get()=="":
            self.txtName.focus_set()
            messagebox.showwarning("توجه","لطفا نام را وارد کنید")
        elif self.Family.get()=="":
            self.txtFamily.focus_set()
            messagebox.showwarning("توجه","لطفا نام خانوادگی را وارد کنید")
        elif self.Age.get()=="":
            self.txtAge.focus_set()
            messagebox.showwarning("توجه","لطفا سن را وارد کنید")
        elif self.Date.get()=="":
            self.txtDate.focus_set()
            messagebox.showwarning("توجه","لطفا تاریخ ثبت نام را وارد کنید")
        elif self.ielts.get()==0 and self.speaking.get()==0:
            messagebox.showwarning("توجه","لطفا نوع تمرین خود را انتخاب کنید")
        else:
            if self.isExist()==True:
                objp=Personal(prs_id=self.Id.get(),prs_name=self.Name.get(),prs_family=self.Family.get(),prs_age=self.Age.get(),prs_date=self.Date.get(),prs_ielts=self.ielts.get(),prs_speaking=self.speaking.get(),prs_remainder_ielts=self.ielts.get(),prs_remainder_speaking=self.speaking.get())
                objbl=blPersonal()
                result=objbl.blAdd(objp)
                if result==True:
                    self.Load()
                    self.set_cell_color(None)
                    self.Name.set("")
                    self.Family.set("")
                    self.Age.set("")
                    self.Date.set("YYYY-MM-DD")
                    self.ielts.set(0)
                    self.speaking.set(0)
                    self.Remielts.set("")
                    self.Remspeaking.set("")

                    messagebox.showinfo("ثبت نام","اطلاعات فرد با موفقیت ثبت گردید")
            else:
                messagebox.showerror("تکراری","!این فرد قبلا ثبت نام شده است")
    #حذف مقادیر جدول
    def Clean(self):
        for item in self.tbl.get_children():
            self.tbl.delete(item)
    #رفرش و لود جدول
    def Load(self):
        self.Clean()
        objbl=blPersonal()
        lstPersonal=objbl.blRead(Personal)
        for item in lstPersonal:
            self.tbl.insert('',"end",values=[item.prs_remainder_speaking,item.prs_remainder_ielts,item.prs_speaking,item.prs_ielts,item.prs_date,item.prs_age,item.prs_family,item.prs_name,item.prs_id])

    #انتخابگر جدول
    def GetSelection(self,e):
        objbl=blPersonal()
        SelectRow=self.tbl.selection()
        if SelectRow!=():
            idrow=self.tbl.item(SelectRow)["values"][8]
            self.Id.set(idrow)

            obj=objbl.blReadById(Personal,idrow)
            self.Name.set(obj.prs_name)
            self.Family.set(obj.prs_family)
            self.Age.set(obj.prs_age)
            self.Date.set(obj.prs_date)
            self.ielts.set(obj.prs_ielts)
            self.speaking.set(obj.prs_speaking)
            self.Remielts.set(obj.prs_remainder_ielts)
            self.Remspeaking.set(obj.prs_remainder_speaking)



    #حذف داده
    def OnClickDelete(self):
        ask=messagebox.askyesno("توجه","آیا از حذف این داده مطمئن هستید؟")
        if ask==True:
            Id=self.Id.get()
            objbak=blBakPersonal()
            objbl=blPersonal()
            objp = BakPersonal(prs_id=self.Id.get(),prs_name=self.Name.get(),prs_family=self.Family.get(),prs_age=self.Age.get()
                                     ,prs_date=self.Date.get(),prs_ielts=self.ielts.get(),prs_speaking=self.speaking.get(),
                                     prs_remainder_ielts=self.Remielts.get(),prs_remainder_speaking=self.Remspeaking.get())
            resultbak = objbak.blBakAdd(objp)
            result=objbl.blDelete(Personal,Id)
            if result==True:
                self.Load()
                self.Name.set("")
                self.Family.set("")
                self.Age.set("")
                self.Date.set("YYYY-MM-DD")
                self.ielts.set(0)
                self.speaking.set(0)
                self.Remielts.set("")
                self.Remspeaking.set("")
                messagebox.showinfo("عملیات موفق","عملیات حذف با موفقیت انجام شد")
            else:
                messagebox.showinfo("عملیات ناموفق", "عملیات حذف انجام نشد")

    #ویرایش داده
    def OnClickEdit(self):
        jdate = jdatetime.datetime.strptime(self.Date.get(), "%Y-%m-%d").togregorian().date()
        Id=self.Id.get()
        #NewObject
        objp=Personal(prs_id=self.Id.get(),prs_name=self.Name.get(),prs_family=self.Family.get(),prs_age=self.Age.get(),prs_date=self.Date.get(),prs_ielts=self.ielts.get(),prs_speaking=self.speaking.get(),prs_remainder_ielts=self.ielts.get(),prs_remainder_speaking=self.speaking.get())
        objbl=blPersonal()
        result=objbl.blUpdatePersonal(Personal,Id,objp)
        if result==True:
            self.Load()
            self.outtime=[]
            self.set_cell_color(None)
            self.Name.set("")
            self.Family.set("")
            self.Age.set("")
            self.Date.set("YYYY-MM-DD")
            self.ielts.set(0)
            self.speaking.set(0)
            self.Remielts.set("")
            self.Remspeaking.set("")
            messagebox.showinfo("عملیات موفق", "عملیات ویرایش با موفقیت انجام شد")
        else:
            messagebox.showinfo("عملیات ناموفق", "عملیات ویرایش انجام نشد")

    #ویرایش پویا
    def OnClickEditDy(self):
        objbl=blPersonal()
        id=self.Id.get()
        result=objbl.blUpdateDynamic(Personal,id,prs_id=id,prs_name=self.Name.get(),prs_family=self.Family.get(),prs_age=self.Age.get()
                                     ,prs_date=self.Date.get(),prs_ielts=self.ielts.get(),prs_speaking=self.speaking.get(),
                                     prs_remainder_ielts=self.Remielts.get(),prs_remainder_speaking=self.Remspeaking.get())
        if result==True:
            self.Load()
            self.outtime = []
            self.set_cell_color(None)
            messagebox.showinfo("عملیات موفق", "عملیات ویرایش با موفقیت انجام شد")
        else:
            messagebox.showinfo("عملیات ناموفق", "عملیات ویرایش انجام نشد")

    #تغییر شکل دکمه
    def ChangeShape(self,e):
        e.widget.config(relief=SUNKEN)

    # تغییر شکل دکمه
    def ResetShape(self,e):
        e.widget.config(relief=RAISED)
    def OnClickReport(self):
        rprt=self.Report.get()
        jalali_date = JalaliDate(1403, 9, 1)
        gregorian_rprtdate = jalali_date.to_gregorian()
        print(gregorian_rprtdate)  # خروجی به فرمت میلادی

        if gregorian_rprtdate == "":
            self.Load()
        else:
            objbl = blPersonal()
            result = objbl.blReport(Personal, gregorian_rprtdate)
            if result != []:
                self.Clean()
                for item in result:
                    self.tbl.insert('', "end", values=[item.prs_remainder_speaking, item.prs_remainder_ielts, item.prs_speaking, item.prs_ielts, item.prs_date, item.prs_age, item.prs_family, item.prs_name, item.prs_id])
    #جستجو
    def OnClickSearch(self):
        srch=self.Search.get()
        if srch=="":
            self.Load()
        else:
            objbl=blPersonal()
            result=objbl.blSearch(Personal,srch)
            if result!=[]:
                self.Clean()
                for item in result:
                    self.tbl.insert('', "end", values=[item.prs_remainder_speaking,item.prs_remainder_ielts,item.prs_speaking, item.prs_ielts, item.prs_date, item.prs_age,
                                                       item.prs_family, item.prs_name, item.prs_id])


    #تکراری بودن
    def isExist(self):
        objp=Personal(prs_id=self.Id.get(),prs_name=self.Name.get(),prs_family=self.Family.get(),prs_age=self.Age.get(),prs_date=self.Date.get(),prs_ielts=self.ielts.get(),prs_speaking=self.speaking.get(),prs_remainder_ielts=self.ielts.get(),prs_remainder_speaking=self.speaking.get())
        objbl=blPersonal()
        return objbl.blExist(Personal,objp)

    def OnClickPrReport(self):
        StartDate = self.DateStart.get()
        EndDate = self.DateEnd.get()
        Sdate = jdatetime.datetime.strptime(StartDate,'%Y-%m-%d').strftime('%Y-%m-%d')
        Edate = jdatetime.datetime.strptime(EndDate,'%Y-%m-%d').strftime('%Y-%m-%d')
        if Sdate == "" or Edate=="":
            self.Load()
            print("no")
        else:
            print(Sdate)
            objblpr = blPersonal()
            result = objblpr.blPrReport(Personal, Sdate,Edate)
            if result != []:
                print(Sdate)
                self.Clean()
                for item in result:
                    self.tbl.insert('', "end",
                                    values=[item.prs_remainder_speaking,item.prs_remainder_ielts,item.prs_speaking, item.prs_ielts, item.prs_date, item.prs_age,
                                                       item.prs_family, item.prs_name, item.prs_id])

    #ثبت نام اوپراتور جدید
    def OnClickRegisterNewUser(self):
        if self.FullName.get()=="":
            self.txtFullName.focus_set()
            messagebox.showwarning("توجه","لطفا نام را وارد کنید")
        elif self.UserReg.get()=="":
            self.txtUserReg.focus_set()
            messagebox.showwarning("توجه","لطفا نام کاربری را وارد کنید")
        elif self.PassReg.get()=="":
            self.txtPassReg.focus_set()
            messagebox.showwarning("توجه","لطفا رمز عبور را وارد کنید")
        elif self.PassReg.get()=="":
            self.txtPassReg.focus_set()
            messagebox.showwarning("توجه","لطفا رمز عبور را وارد کنید")
        else:
            objL=Login(self.FullName.get(),self.UserReg.get(),self.PassReg.get(),self.IsAdmin.get())
            objbl=blPersonal()
            result=objbl.blAdd(objL)
            if result==True:
                self.FullName.set("")
                self.UserReg.set("")
                self.PassReg.set("")
                messagebox.showinfo("ثبت نام","اطلاعات اپراتور جدید با موفقیت ثبت گردید")


    def Login(self):
        objL = Login("", self.User.get(), self.Pass.get(), self.IsAdmin.get())
        objbl = blPersonal()
        r = objbl.blExistLogin(Login, objL)
        userName=self.txtUser.get()
        self.lblLoginUser = customtkinter.CTkLabel(self.master, text="text",text_color="#854bcf", font= ("Nazanin", 15,"bold"))
        self.lblLoginUser.configure(text=userName)
        self.lblLoginUser.place(x=50, y=10)
        if r!=[]:
            if r[0].isAdmin==1:
                self.frmLogin.place_forget()
                self.lbl1.place(x=1024,y=12)
                self.lbl2.place(x=997, y=12)
                self.lbl3.place(x=940, y=12)
                self.lblSearch.place(x=470, y=12)
                self.btnPrReport2.place(x=450, y=120)
                self.frmReport.place(x=20, y=40)
                self.btnPrReport2.place(x=450, y=120)
                '''self.btnPrReport.place(x=190, y=260)
                self.lblReport.place(x=360, y=200)
                self.lblReportdate.place(x=350, y=190)'''
                self.txtDateStart.place(x=350, y=160)
                self.txtDateEnd.place(x=200, y=160)
                '''self.txtReport.place(x=190, y=215)'''



            else:
                self.frmLogin.place_forget()
                print("2")


        else:
            messagebox.showerror("خطا", "!نام کاربری یا رمز عبور اشتباه است")
    def reminderShow(self):
        self.frmReminder.place(x=10,y=40)
    def OnClickShowReport(self):
        self.frmReport.place(x=0,y=0)
        self.frmSearch.place_forget()
        self.btnRemind.place_forget()
        self.btnPrReport2.place_forget()
        self.btnPrReport1.place(x=450, y=120)
        self.btnPrclose.place(x=60, y=50)

    def OnClickCloseReport(self):
        self.frmReport.place_forget()
        self.frmSearch.place(x=0, y=0)
        self.btnPrReport2.place(x=450, y=120)
        self.btnRemind.place(x=450, y=250)

    def OnClickRestore(self):
        ask=messagebox.askyesno("توجه","آیا از ریکاوری این داده مطمئن هستید؟")
        if ask==True:
            IdRes=self.Restore.get()
            print(IdRes)
            objp =blBakPersonal()
            objl=blPersonal()
            row=objp.blBakReadById(BakPersonal, IdRes)
            print(row.prs_name)
            resultbak = Personal(prs_id=row.prs_id,prs_name=row.prs_name,prs_family=row.prs_family,prs_age=row.prs_age,prs_date=row.prs_date,prs_ielts=row.prs_ielts,prs_speaking=row.prs_speaking,prs_remainder_ielts=row.prs_remainder_ielts,prs_remainder_speaking=row.prs_remainder_speaking)
            r2=objl.blAdd(resultbak)
            print(r2)
            r=objp.blBakDelete(row)
            print(r)
            if r==True:
                print("row")
                messagebox.showinfo("عملیات موفق","عملیات ریستور با موفقیت انجام شد")
                self.Load()
            else:
                messagebox.showinfo("عملیات ناموفق", "عملیات ریستور انجام نشد")

    '''def BackuoData(self):

        backup_dir = 'C:/backup'
        # Backup file name
        backup_file = 'mydatabase_backup_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.bak'

        objbl = blPersonal()
        objbl.backupdata(objbl,backup_dir,backup_file)'''

