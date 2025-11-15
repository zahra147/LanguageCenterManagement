from DAL.Repository import Repository

class blPersonal():
    def blAdd(self,obj):
        repos=Repository()
        result=repos.Add(obj)
        return result

    def blRead(self,TableName):
        repos=Repository()
        result=repos.Read(TableName)
        return result

    def blReadById(self,TableName,id):
        repos=Repository()
        result=repos.ReadById(TableName,id)
        return result

    def blDelete(self,TableName,id):
        repos=Repository()
        obj=repos.ReadById(TableName,id)
        return repos.Delete(obj)

    def blUpdatePersonal(self,TableName,id,datanew):
        repos=Repository()
        obj=repos.ReadById(TableName,id)
        return repos.UpdatePersonal(obj,datanew)

    def blUpdateDynamic(self,TableName,id,**kwargs):
        repos=Repository()
        obj=repos.ReadById(TableName,id)
        return repos.UpdateDynamic(obj,**kwargs)

    def blSearch(self,TableName,search):
        repos=Repository()
        lstobj=repos.Search(TableName,search)
        return lstobj
    def blReport(self,TableName,report):
        repos=Repository()
        lstobj=repos.Report(TableName,report)
        return lstobj
    def blPrReport(self,TableName,Start,End):
        repos=Repository()
        lstobj=repos.PrReport(TableName,Start,End)
        return lstobj
    def blExist(self,TableName,newobj):
        repos=Repository()
        result=repos.Exist(TableName,newobj)
        return result

    def IsAdministrator(self, TableName, newobj):
        repos=Repository()
        result=repos.IsAdministrator(TableName,newobj)

    def blExistLogin(self, TableName, newobj):
        repos = Repository()
        result = repos.ExistLogin(TableName, newobj)
        return result
    def Restore(self, TableName, id):
        repos = Repository()
        result = repos.Restore(TableName,id)
        return result

class blBakPersonal():
    def blBakAdd(self,obj):
        repos=Repository()
        result=repos.Add(obj)
        return result

    def blBakReadById(self, TableName, id):
        repos = Repository()
        result = repos.ReadById(TableName, id)
        return result
    def blBakDelete(self,obj):
        repos=Repository()
        return repos.DeledirteId(obj)

