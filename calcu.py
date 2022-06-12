class Calc:

    def __init__(self,num1,num2) :
        self.num1=num1
        self.num2=num2

    def add(self) :
        sum=self.num1+self.num2
        return sum

    def diff(self) :
        sub=self.num1-self.num2
        return sub

    def mul(self) :
        pro=self.num1*self.num2
        return pro

    def div(self) :
        divi=self.num1/self.num2
        return divi
        
    def operation(self,operand) :
        if(operand == "+") :
            return self.add()
        elif(operand == "-") :
            return self.diff()
        elif(operand == "*") :
            return self.mul()
        elif(operand == "/") :
            return self.div()
            
while True:

    num1=(input("Enter first number"))
    if(num1.isdigit() == False) :
        print("Invalid input")
    elif(num1 == None) :
        print("Invalid input")
        

    num2=(input("Enter second number"))
    if(num2.isdigit() == False) :
        print("Invalid input")
    elif(num2 == None) :
        print("Invalid input")

    calculation=Calc(int(num1),int(num2))
    opr=(input("Enter operand"))
    result=calculation.operation(opr)
    print(result)
    
    def append(file,text) :

      with open(file,'a') as f :
        f.write(str(text) + '\n')
    

        
        
    append('file_new.txt',result)

    

    