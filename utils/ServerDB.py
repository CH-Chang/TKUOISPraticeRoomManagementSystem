import pymssql
import pyDes
import requests
import base64
import datetime


class ServerDB():
    def __init__(self):
        super(ServerDB, self).__init__()

    def getSQLKey(self):
        response = requests.get('http://163.13.100.118:1689/SQLText/SQL.txt')
        encryptKey = response.text
        encryptKey = base64.b64decode(encryptKey)

        chiper = pyDes.des('B7aDhz6W', pyDes.CBC, 'sMmBnR9c',
                           pad=None, padmode=pyDes.PAD_PKCS5)
        decryptKey = chiper.decrypt(encryptKey)
        decryptKey = decryptKey.decode(encoding='utf-8')

        return decryptKey

    def getLocalIP(self):
        response = requests.get('http://163.13.100.118:1689/getIP.ashx')
        ip = response.text
        return '163.13.144.100'.ljust(15)

    def getTableName(self):
        year = datetime.datetime.now().strftime('%Y')
        return 'ClientLoginTable_'+year

    def getClassReservationTableName(self):
        year = datetime.datetime.now().strftime('%Y')
        return 'ClassReservation_'+year

    def getSQLConn(self):
        SQLKey = self.getSQLKey()
        conn = pymssql.connect(server='163.13.100.118', user='TKU_CCR',
                               password=SQLKey, database='tkuComputerClassRoom')
        return conn

    def checkMember(self, stuID):
        conn = self.getSQLConn()
        cursor = conn.cursor()
        cursor.execute("select count(*) from Member where SID='"+stuID+"';")
        res = cursor.fetchall()
        conn.close()
        return res[0][0]

    def checkPassword(self, stuID, stuPWD):
        infor = {'stuID': stuID, 'stuPWD': stuPWD}
        response = requests.post(
            'http://163.13.100.118:1234/isLogin.ashx', data=infor)
        return int(response.text)

    def checkAccount(self, stuID, stuPWD):
        isVaild = self.checkPassword(stuID, stuPWD)
        isMember = self.checkMember(stuID)

        if (isVaild == 1 and isMember == 1):
            return 0
        elif (isVaild == 0):
            return 1
        elif (isVaild == 2):
            return 2
        elif (isVaild == 3):
            return 3
        else:
            return 4

    def getClassroomName(self):
        ip = self.getLocalIP()
        conn = self.getSQLConn()
        cursor = conn.cursor()
        cursor.execute("select * from ClassroomName where IP='"+ip+"';")
        res = cursor.fetchall()
        conn.close()
        classRoomName = res[0][1].strip()
        return classRoomName

    def getSeatStatus(self):

        tableName = self.getTableName()
        classroomName = self.getClassroomName().ljust(10)

        conn = self.getSQLConn()

        cursor = conn.cursor()
        cursor.execute("select classroomName, computerNum, stuID, convert(varchar, loginDateTime, 108) from " + tableName + " where logoutDateTime IS NULL AND classroomName = '" +
                       classroomName + "' AND convert(varchar(10),loginDateTime,120) = convert(varchar(10),getdate(),120) order by computerNum;")
        res = cursor.fetchall()

        conn.close()

        return res

    def getClassReservation(self):

        tableName = self.getClassReservationTableName()
        classRoomName = self.getClassroomName().ljust(10)
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        conn = self.getSQLConn()

        cursor = conn.cursor()
        cmd = "select _id, departmentLevel, dubjectChineseName, CONVERT(varchar(12) , date, 112 ) as 'date', classRoomID, SessionNum, TeacherName, startComputerNum, endComputerNum,UseType,BorrowTypeBoolean,departmentClassname,departmentClass,checkCode from " + \
            tableName + ", ClassroomName where ClassroomName.classroomNumber = " + \
            tableName + ".classroomID AND classroomName = '" + \
            classRoomName+"' AND date='"+date+"';"
        cursor.execute(cmd)
        res = cursor.fetchall()
        conn.close()
        return res

    def getPersonalReservation(self):

        date = datetime.datetime.now().strftime('%Y%m%d')
        classRoomName = self.getClassroomName().ljust(10)

        conn = self.getSQLConn()
        cursor = conn.cursor()
        cmd = "select * from ReservationData, ClassroomName where ClassroomName.classroomNumber = ReservationData.useClassroom AND classroomName = '" + \
            classRoomName+"' AND useDate='"+date+"';"
        cursor.execute(cmd)
        res = cursor.fetchall()
        conn.close()

        return res

    def onlineComputer(self, stuID, seatNum):

        tableName = self.getTableName()
        classroomName = self.getClassroomName().ljust(5)
        stuID = stuID.ljust(10)

        conn = self.getSQLConn()

        cursor = conn.cursor()
        cursor.execute("INSERT INTO "+tableName+" (classroomName, computerNum, stuID, loginDateTime) VALUES ('" +
                       classroomName+"',"+str(seatNum)+",'"+stuID+"', getdate());")

        conn.commit()

        effectedRowsCount = cursor.rowcount
        conn.close()

        return effectedRowsCount

    def offlineComputer(self, stuID, seatNum):

        tableName = self.getTableName()
        classRoomName = self.getClassroomName().ljust(5)
        stuID = stuID.ljust(10)
        conn = self.getSQLConn()

        cursor = conn.cursor()
        cursor.execute("update " + tableName + " set logoutDateTime = getdate() where classroomName='" +
                       classRoomName+"' and computerNum="+str(seatNum)+" and stuID='"+stuID+"' and logoutDateTime IS NULL")
        conn.commit()
        effectedRowsCount = cursor.rowcount
        conn.close()

        return effectedRowsCount

    def test(self):

        return
