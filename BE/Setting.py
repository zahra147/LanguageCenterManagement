class Setting():
    def GetConn(self):
        with open("constr") as f:
            return str(f.read())