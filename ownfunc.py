 #len
def length(string):
    c=0
    for i in string:
        c+=1
    return c
#capitalize
def Capital(string):
    s=''
    a=string[0]
    ordinal=ord(a)
    letter=ordinal-97
    capletter=chr(65+letter)
    s+=capletter
    for i in range(1,length(string)):
        s+=string[i]
    return s
# occurence count
def countocc(string,char):
    c=0
    for i in string:
        if i==char:
            c+=1
    return c
# find
def findtheindex(string,char):
     c=0
     for i in range(length(string)):
         if string[i]==char:
             c=i
             break
         else:
             c=-1
     return c
#  isalpha
def Isalpha(string):
    r=True
    for i in string:
        if i in "1234567890!@#$%^&*()_+=-[]{}'<>?/,.~`|'\'" or i in " ":
            r=False
        else:
            r="not a character"
    return r
# isnum
def Isnumeric(string):
     r=True
     for i in string:
         if i.lower() in "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-[]{}'<>?/,.~`|'\'" or i in " ":
             r=False
         else:
             r= "Not a character"
     return r          
#upper
def Upper(string):
   s=''
   for i in string:
        if i.lower() and i!=" " :
            if ord(i)>=97:
                letter=ord(i)-97
                cap=chr(letter+65)
                s+=cap
                
            else:
                s+=i
        elif i==" ":
            s+=" "
    
   return s      
#lower
def Lower(string):
   s=''
   for i in string:
        if Upper(i) and i!=" " :
            if ord(i)>=65 and ord(i)<97:
                letter=ord(i)-65
                cap=chr(letter+97)
                s+=cap
                
            else:
                s+=i
        elif i==" ":
            s+=" "
    
   return s  
# is Uper  
def isUpper(string):
    r=False
    for i in string:
        if ord(i)>64 and ord(i)<97:
            r=True
        else:
            r=False
    return r
def isLower(string):
    r=False
    for i in string:
        if   ord(i)>96 and ord(i)<123:
            r=True
        else:
            r=False
    return r
# startswith
def StartingWith(string,chr):
    if string[0]==chr:
        r=True
    else:
        r=False
    return r
# endswith
def EndingWith(string,chr):
    if string[-1]==chr:
        r=True
    else:
        r=False
    return r
# replace
def replaceing(string,old,new):
    s=''
    for i in range(len(string)):
        if string[i]==old:
            s+=new
        else:
            s+=string[i]
    return s


