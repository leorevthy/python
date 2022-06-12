
class sum :

    def input(self,num1,num2) :
        self.num1=num1
        self.num2=num2
    def add(self) :
        result=float(self.num1) + float(self.num2)
        return result
x=sum()
x.input(10,14)
res=x.add()
print(res)

