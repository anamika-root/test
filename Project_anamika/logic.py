# __ Decorator __

def fun(sum):
    def inner():
        a = sum() + 10
        return a
    return inner    
@fun    
def sum():
    return 10
a = sum
a = sum()
print(a)
print(sum)
print(sum())


def last_name(first_name):
    def name(n):
        a = n + "singh"
        return first_name(a)
    return name 

@last_name       
def first_name(name):
    result = name + ""
    return result

print(first_name("Anamika "))   

def last_name(first_name):
    def name():
        a = first_name() + "singh"
        return a
    return name

@last_name

def first_name():
    return "Anamika "
print(first_name())


def name1(name):
    def name2():
        name3 = name() + "language"
        return name3
    return name2
@name1
def name():
    return "python "
print(name())


# Generator

# def fun():
#     yield 1
#     yield  10
# for i in fun():
#     print(i)
#         yield 1

def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function

for val in fun(): 
    print(val)

def sum():
    yield 1

for i in sum():
    print(i)

# __ Iterator __


a = "anamika"
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))