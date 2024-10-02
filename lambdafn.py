#lambda argument-list:expression
#  lambda x,y:x+y
f=lambda x:x*x
print(f)
print(f(10))

f=lambda x,y:x+y
print(f(10,20))

#types of argument lambda function support

#Named arguments

namedArgs=(lambda x,y=3,z=5:x*y*z)(7)
print(namedArgs)

#variable arguments

variable=(lambda x,y=3,z=5: x+y+z)(x=7)
print(variable)

#variable keyword arguments

variableKey=(lambda*args:sum(args)(3,5,7))
print(variableKey) 


positional=(lambda x,y,z:x*y*z)(3,5,7)
print(positional)


#string libraries using lambda function
print("string libraries using lambda function")
#slicing
print("\n\t\t\t\t SILICING FUNCTION : \n")
slicing=lambda z='  my name is bharti lalotra':z[2:22]
print(slicing)
print("\n\t\t------------------------------------------------------------\n")

#strip
print("\n\t\t\t\t strip() FUNCTION: \n")
strip= (lambda a:a.strip()) ('           My name is  bharti lalotra            ')
print(strip)
print("\n\t\t------------------------------------------------------------\n")

#lstrip
print("\n\t\t\t\t lstrip() FUNCTION : \n") 
lstrip=(lambda a:a.lstrip() )('                My name is  bharti lalotra    ')
print(lstrip)
print("\n\t\t------------------------------------------------------------\n")

#rstrip
print("\n\t\t\t\t rstrip() FUNCTION : \n") 
rstrip=(lambda a:a.rstrip() )('                    My name is  bharti lalotra                     ')
print(rstrip)
print("\n\t\t------------------------------------------------------------\n")

#strip() with combination
print("\n\t\t\t\t strip() FUNCTION WITH COMBINATION  : \n") 
strip=(lambda b:b.strip('123456'))('12366hello456' )
print(strip)
print("\n\t\t------------------------------------------------------------\n")


#strip() removing specific characters
print("\n\t\t\t\t strip() FUNCTION : \n") 
strip=(lambda b:b.strip("w"))('www.example.com')
print(strip)
print("\n\t\t------------------------------------------------------------\n")


#removeprefix
print("\n\t\t\t\t removepreix() FUNCTION :\n")
prefix=(lambda a:a.removeprefix("bharti"))('bharti lalotra')
print(prefix)
print("\n\t\t------------------------------------------------------------\n")

#removesuffix
print("\n\t\t\t\t removesuffix() FUNCTION: \n")
suffix=(lambda a:a.removesuffix("lalotra"))('bharti lalotra')
print(suffix)
print("\n\t\t------------------------------------------------------------\n")

#replace()
print("\t\t\t\t replace() FUNCTION: \n")
replace=(lambda a:a.replace('#',' *'))('#### bharti lalotra \n ')
print(replace)
print("\n\t\t------------------------------------------------------------\n")

#rsplit
print("\t\t\t\t RESPLIT() FUNCTION : \n")
rsplit=(lambda a:a.rsplit())("python is object oriented langauge.")
print(rsplit)
print("\n")
print("\t\t\t\t RESPLIT() FUNCTION WITH MAXVALUE :\n")
rsplit=(lambda a:a.rsplit(' ',maxsplit=2))("python is object oriented langauge.")
print(rsplit)
print("\n\t\t------------------------------------------------------------\n")

#split()
print("\t\t\t\t SPLIT() FUNCTION :\n")
split=(lambda a:a.split())("python is object oriented langauge.")
print(split)
print("\n\t\t------------------------------------------------------------\n")

#swapcase()
print("\t\t\t\t swapcase() FUNCTION : \n")
swapcase=(lambda a: a.swapcase())("DEPARTMENT cse")
print(swapcase)
print("\n\t\t------------------------------------------------------------\n")

#f-string()
num1=80
num2=80
print(f"the addition of {num1} and {num2} : {num1+num2}")
print("\n\t\t------------------------------------------------------------\n")


#center()
print("\t\t\t\t center() FUNCTION : \n")
center=(lambda a:a.center(60,"*"))("python is a programming language")
print(center)
print("\n\t\t------------------------------------------------------------\n")


#ljust()
print("\t\t\t\t ljust() FUNCTION : \n")
ljust=(lambda a:a.ljust(80,"*"))("python is a programming language")
print(ljust)
print("\n\t\t------------------------------------------------------------\n")


#rjust()
print("\t\t\t\t rjust() FUNCTION : \n")
rjust=(lambda a:a.rjust(80,"*"))("python is a programming language")
print(rjust)
print("\n\t\t------------------------------------------------------------\n")


#partition
print("\t\t\t\t partition() FUNCTION : \n")
partition=(lambda a: a.partition("is"))("python is a programming language")
print(partition)
print("\n")
partition=(lambda a: a.partition("not"))("python is a programming language")
print(partition)
print("\n\t\t------------------------------------------------------------\n")


#startswith
print("\t\t\t\t startswith() FUNCTION : \n")
startwith=(lambda a: a.startswith("programming"))("python is a programming language")
print(startwith)
print(" \n")
startwith=(lambda a: a.startswith("python"))("python is a programming language")
print(startwith)
print("\n\t\t------------------------------------------------------------\n")

#endswith
print("\t\t\t\t endswith() FUNCTION : \n")
endwith=(lambda a: a.endswith("language"))("python is a programming language")
print(endwith)
print(" \n")
endwith=(lambda a: a.endswith("is"))("python is a programming language")
print(endwith)
print("\n\t\t------------------------------------------------------------\n")


#find()
print("\t\t\t\t find() FUNCTION : \n")
find=(lambda a: a.find("o"))("python is a programming language")
print(find)
print("\n\t\t------------------------------------------------------------\n")

#rfind()
print("\t\t\t\t rfind() FUNCTION : \n")
rfind=(lambda a: a.rfind("o"))("python is a programming language")
print(rfind)
print("\n\t\t------------------------------------------------------------\n")

#count()
print("\t\t\t\t count() FUNCTION : \n")
count=(lambda a: a.count("o"))("python is a programming language")
print(count)
print("\n\t\t------------------------------------------------------------\n")

#isalpha(),isnumeric(),isalnum()
print("\t\t\t\t CHECK THE STRING : isalpha(),isnumeric(),isalnum()  FUNCTION : \n")
z=(lambda c:(c.isalpha(),c.isnumeric(),c.isalnum()))("python")
print(z)
print("\n")

y=(lambda d:(d.isalpha(),d.isnumeric(),d.isalnum()))("Bharti123")
print(y)
print("\n")

x=(lambda e:(e.isalpha(),e.isnumeric(),e.isalnum()))("2105375")
print(x)
print("\n")

w=(lambda f:(f.isalpha(),f.isnumeric(),f.isalnum()))("Bharti-123")
print(w)
print("\n\t\t------------------------------------------------------------\n")

#lower
print("\t\t\t\t lower() FUNCTION : \n")
lower=(lambda a:a.lower())("Python is a Programming Language")
print(lower)
print("\n\t\t------------------------------------------------------------\n")

#islower()
print("\t\t\t\t islower() FUNCTION : \n")
islower=(lambda a:a.islower())("PYTHON IS A PROGRAMMING LANGUAGE")
print(islower)
islower=(lambda a:a.islower())("python is a programming language")
print(islower)
print("\n\t\t------------------------------------------------------------\n")

#upper()
print("\t\t\t\t upper() FUNCTION : \n")
upper=(lambda a:a.upper())("Python is a Programming Language")
print(upper)
print("\n\t\t------------------------------------------------------------\n")


#isupper()
print("\t\t\t\t isupper() FUNCTION: \n")
isupper=(lambda a:a.isupper())("PYTHON IS A PROGRAMMING LANGUAGE")
print(isupper)
isupper=(lambda a:a.isupper())("python is a programming language")
print(isupper)
print("\n\t\t------------------------------------------------------------\n")


#capitalize
print("\t\t\t\t capitalize() FUNCTION:\n")
capitalize=(lambda a:a.capitalize())("python is a programming language")
print(capitalize)
print("\n\t\t------------------------------------------------------------\n")

#join()
print("\t\t\t\t join() FUNCTION :\n")
join=(lambda list:' '.join(list))
print(join(["python"," is ","object", "oriented", "langauge."]))
print("\n\t\t------------------------------------------------------------\n")

#re.sub()
print("\t\t\t\tre.sub() FUNCTION :\n")
import re
resub=(lambda a:re.sub(' ',"-",a))("my name is bharti")
print(resub)
print("\n\t\t------------------------------------------------------------\n")
