class Employee:
    # class variables
    empID = 0
    empName =""
    empSal = 0
    empAddress=""
    empPhNO = 0
    empGender = ""
    empDOB = ""
    empPos = ""
    
    #class init method (constructor)
    def __init__(self):
        self.empName = "XYZ"
        self.empDOB = "1970"
    
    # class methods
    def getEmpDetails(self):
        print("Enter the Details of Employee")
        self.empName = input("Emp Name: ")
        #test case for checking name
        
        if self.__checkName(self.empName) == 0:
            print("Enter the correct Name")
            return
        
        self.empID = int(input("Emp ID: "))
        self.empDOB = input("Emp DOB: ")
        self.empPhNO = int(input("Emp Phno: "))
        self.empSal = input("Emp Sal: ")
        if self.__checkNum(self.empSal) == 0:
            print("check input error")
        self.empPos = input("Emp Job Title: ")
    
    def dispEmpDetails(self):
        print("==============================")
        print("\tEmployee Details are")
        print("==============================")
        print("Emp ID: ",self.empID)
        print("Emp Name: ",self.empName)
        print("Emp DOB: ",self.empDOB)
        print("Emp Salary",self.empSal)
        print("Emp PhNo: ",self.empPhNO)
        print("Emp Job Title: ",self.empPos)
    
    def __checkNum(self,str1):
        print("in __checkNum Method")
        if str1.isdigit() == True:
            print("True")
            return 1
        else:
            return 0
        
    def __checkName(self, str1):
        for ch in str1:
            if not (ch >= "A" and ch <= "Z" or ch>="a" and ch <= "z" or ch ==" "):
                return 0
            
                
              
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()
# emp1.dispEmpDetails()
# emp2.dispEmpDetails()
# emp3.dispEmpDetails()
emp1.getEmpDetails()
emp1.dispEmpDetails()
# emp2.dispEmpDetails()
# emp3.dispEmpDetails()
 