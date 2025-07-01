
class Logic:
    def even_number():
        a = int(input("enter the any number"))
        for i in range(a):
            if i%2  == 0:
                print(i)


    def odd_number():
        b = int(input("enter the any number")) 
        for x in range(b):
            if x%2 == 1:
                print(x)           

obj = Logic
print(obj.even_number())
print(obj.odd_number())

class Question:
    def lis(self):
        a = [1,2,3,4,5]
        a.append(a)
        a.append(6)
        print(a)

obj = Question()
print(obj.lis())

class Count:
    def name():
        a = 'anamika'
        c = 0
        for i in a:
            if i == 'a':
                c += 1
        print(c)        

obj = Count
print(obj.name())


class Log:
    def logic():
        x = "python is programming language, python is very simple language, python is awesome and i am python developr "
        c = 0  
        for i in x:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                c += 1
        print(c,"Total Vowel_number")      
obj = Log
print(Log.logic())            


        

