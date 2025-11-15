from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BE.Setting import Setting
from datetime import datetime
conn=Setting().GetConn()
engine=create_engine(conn)
Sessions=sessionmaker(bind=engine)
session=Sessions()
import jdatetime

#CRUD
class Repository():
    #اضافه کردن داده
    def Add(self,obj):
        session.add(obj)
        session.commit()
        return True

    #خواندن داده ها
    def Read(self,TableName):
        return session.query(TableName).all()
        #output->List

    #خواندن یک داده
    def ReadById(self,TableName,id):
        return session.query(TableName).filter(TableName.prs_id==id).first()
        #output->Object

    #حذف داده
    def Delete(self,obj):
        session.delete(obj)
        session.commit()
        return True

    #اپدیت
    def UpdatePersonal(self,objold,objnew):
        objold.prs_id = objnew.prs_id
        objold.prs_name=objnew.prs_name
        objold.prs_family=objnew.prs_family
        objold.prs_age=objnew.prs_age
        objold.prs_date=objnew.prs_date
        objold.prs_ielts=objnew.prs_ielts
        objold.prs_speaking=objnew.prs_speaking
        session.commit()
        return True
    #اپدیت پویا
    def UpdateDynamic(self,oldobj,**kwargs):
        for key,val in kwargs.items():
            setattr(oldobj,key,val)
        session.commit()
        return True
    #دو روش جستجو
    def Search(self,TableName,search):
        result=session.query(TableName).filter((TableName.prs_id.like(f"%{search}%")) |
                                               (TableName.prs_name.like(f"%{search}%")) |
                                               (TableName.prs_family.like(f"%{search}%")) |
                                               (TableName.prs_age.like(f"%{search}%")) |
                                               (TableName.prs_date.like(f"%{search}%")) |
                                               (TableName.prs_ielts.like(f"%{search}%")) |
                                               (TableName.prs_speaking.like(f"%{search}%")))
        return result

    def Report(self, TableName, report):
        return session.query(TableName).filter(TableName.prs_date==report).all()
    def PrReport(self, TableName, Start,End):
        return session.query(TableName).filter(TableName.prs_date.between(Start,End)).all()
    #چک کردن عدم ثبت فرد تکراری
    def Exist(self,TableName,newobj):

        result=session.query(TableName).filter((TableName.prs_name==newobj.prs_name) &
                                               (TableName.prs_family==newobj.prs_family) &
                                               (TableName.prs_age==newobj.prs_age)).all()
        if result==[]:
            return True
        else:
            return False

    #لاگین و ورود با رمز

    def ExistLogin(self,TableName,newobj):
        result=session.query(TableName).filter((TableName.username==newobj.username) &
                                               (TableName.password==newobj.password)).all()
        return result
    def Restore(self,TableName,id):
        return session.query(TableName).filter(TableName.prs_id==id).first()


    def DeleteId(self,obj):
        session.delete(obj)
        session.commit()
        return True