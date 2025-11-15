from sqlalchemy import create_engine,Column,Integer,String,NVARCHAR,DATETIME
from sqlalchemy.orm import declarative_base
from BE.Setting import Setting
import pyodbc
#آدرس دیتابیس
conn=Setting().GetConn()
engine=create_engine(str(conn))
Base=declarative_base()

#Personal ساخت جدول
class Personal(Base):
    __tablename__="Personal"
    prs_id=Column(Integer,primary_key=True,autoincrement=True)
    prs_name=Column(NVARCHAR)
    prs_family=Column(NVARCHAR)
    prs_age=Column(NVARCHAR)
    prs_date=Column(NVARCHAR)#تاریخ ثبت نام
    prs_ielts=Column(NVARCHAR)#آموزش ایلتس
    prs_speaking=Column(NVARCHAR)#آموزش اسپیکینگ
    prs_remainder_ielts = Column(NVARCHAR)#جلسات باقی مانده ایلتس
    prs_remainder_speaking = Column(NVARCHAR)#جلسات باقی مانده اسپیکینگ


class BakPersonal(Base):
    __tablename__="BakPersonal"
    prs_id=Column(Integer,primary_key=True)
    prs_name=Column(NVARCHAR)
    prs_family=Column(NVARCHAR)
    prs_age=Column(NVARCHAR)
    prs_date=Column(NVARCHAR)#تاریخ ثبت نام
    prs_ielts=Column(NVARCHAR)#آموزش ایلتس
    prs_speaking=Column(NVARCHAR)#آموزش اسپیکینگ
    prs_remainder_ielts = Column(NVARCHAR)#جلسات باقی مانده ایلتس
    prs_remainder_speaking = Column(NVARCHAR)#جلسات باقی مانده اسپیکینگ


#جدول Login
class Login(Base):
    __tablename__="Login"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(NVARCHAR)#نام اوپراتور(کارمند آموزشگاه زبان)
    username=Column(NVARCHAR)#نام کاربری
    password=Column(NVARCHAR)#رمز عبور
    isAdmin=Column(Integer)  # مدیر ارشد

    def __init__(self,Name,UserName,Password,Isadmin):
        self.name=Name
        self.username=UserName
        self.password=Password
        self.isAdmin=Isadmin


Base.metadata.create_all(engine)

'''def __init__(self,prs_id,prs_name,prs_family,prs_age,prs_date,prs_ielts,prs_speaking,prs_remainder_ielts,prs_remainder_speaking):
    self.prs_id = prs_id
    self.prs_name=prs_name
    self.prs_family=prs_family
    self.prs_age=prs_age
    self.prs_date=prs_date
    self.prs_ielts=prs_ielts
    self.prs_speaking=prs_speaking
    self.prs_remainder_ielts=prs_remainder_ielts
    self.prs_remainder_speaking=prs_remainder_speaking'''