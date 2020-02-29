import sys
import os
import json
import random
import pdb
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton,QLineEdit,QLabel,QMdiArea,QMdiSubWindow
from lesson_6.demoLoginWindow import *
from lesson_6.demoUserAccount import *
class MyForm(QDialog):
    def openWindow(self):
        # pdb.set_trace()
        self.window = QtWidgets.QDialog()
        self.ai = Ai_Dialog()
        self.ai.setupAi(self.window)
        self.ai.groupBox.hide()
        self.ai.pushButton.setText("Click to continue")
        self.ai.pushButton.clicked.connect(self.setName)
        w.hide()
        self.window.show()
    def setName(self):

        name = self.loginChecking()['name']
        number = self.loginChecking()['number']
        amount = self.loginChecking()['amount']
        self.ai.pushButton.hide()
        self.ai.userNameLabel.setText(name)
        self.ai.lineEditAccountNumber.setText(number)
        self.ai.lineEditFunds.setText(amount)
        self.ai.groupBox.show()
        self.window.setWindowTitle(name + "'s account")
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.passwordEditLine.setEchoMode(QLineEdit.Password)
        self.ui.regPasswordEdit.setEchoMode(QLineEdit.Password)
        # self.ui.regNameEdit.editingFinished.connect(self.saveRegistration)
        self.ui.registrationButton.clicked.connect(self.saveRegistration)
        self.ui.signInButton.clicked.connect(self.loginChecking)


    def saveRegistration(self):
       name = self.ui.regNameEdit.text()
       login = self.ui.regLoginEdit.text() + ".json"
       password = self.ui.regPasswordEdit.text()
       if(name and login and password) == "":
           self.ui.warningLabel.setText("<font color='red'>Please fill out all fields</font>")
       else:
           print(name, login, password)

           dataToFile = {'name': name, 'login': login, 'password': password}
           path = "C:/Users/NudleHead/PycharmProjects/try/lesson_6/users/" + login
           if os.path.exists(path):
               print("exist")
               self.ui.warningLabel.setText("<font color='red'>Login is already in use</font>")
           else:
               newFile = open(path, "w")
               newFile.close()
               with open(path, "w") as outfile:
                   json.dump(dataToFile, outfile)
               newFile.close()
               if os.path.exists(path):
                   print("Successful")
                   self.setNumberAccount()

                   with open(path) as json_file:
                       data = json.load(json_file)
                       idLogin = data["login"]
                       accountNumber = data["number"]
                       print(idLogin, accountNumber)


               else:
                   print("Error")


    def setNumberAccount(self):
        n = 0
        value = "0"
        numlist = ""
        while n < 22:
            numAccount = str(random.randint(0, 9))
            numlist = numlist + numAccount
            if numlist[0] == "0":
                numlist[0] = random.randint(1, 9)
            n += 1

        name = self.ui.regLoginEdit.text()+'.json'
        path = "C:/Users/NudleHead/PycharmProjects/try/lesson_6/users/" + name
        with open(path) as json_file:
            data = json.load(json_file)
            y = {"number": numlist, "amount":value}
            # appending data to emp_details
            data.update(y)
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
        return numlist

    def setIdAndNumberAccount(self):
        login = self.loginChecking()["login"]
        number = self.loginChecking()["number"]
        dataToFile = {'userId': login, 'accountNumber': number}
        path = "C:/Users/NudleHead/PycharmProjects/try/lesson_6/users/" + login
        if os.path.exists(path):
            print("exist")
            with open(path) as json_file:
                data = json.load(json_file)
                # appending data to emp_details
                data.update(dataToFile)
                with open(path, 'w') as f:
                    json.dump(data, f, indent=4)

        else:
            newFile = open(path, "w")
            newFile.close()
            with open(path, "w") as outfile:
                json.dump(dataToFile, outfile)
            newFile.close()
            if os.path.exists(path):
                print("Successful")
            else:
                print("Error")

    def loginChecking(self):
        loginToCheck = str(self.ui.loginEditLine.text() + ".json")
        passToCheck = str(self.ui.passwordEditLine.text())
        path = "C:/Users/NudleHead/PycharmProjects/try/lesson_6/users/" + loginToCheck
        if os.path.exists(path):
            print("exist")
            with open(path) as json_file:
                data = json.load(json_file)
                answere = data["name"]
                answereName = data["password"]
                answereLogin = data["login"]
                number = data["number"]
                amount = data['amount']
                if answereName == passToCheck:
                    print("logged in")
                    self.openWindow()
                    d = dict()
                    d['name'] = answere
                    d['number'] = number
                    d['amount'] = amount
                    d['login'] = answereLogin
                    return d

                else:
                    print("wrong pass")
        else:
            print("false")






if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())