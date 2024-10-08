
# this will check if therer is a continous 1,2,3
def arraycheck (ll):
    for i in range(0,len(ll)-2):
        if ll[i]==1 and ll[i+1]==2 and ll[i+2]==3:
            return True
    return False

print(arraycheck([1,1,2,3,1]))
print(arraycheck([1,1,2,4,1]))
print(arraycheck([1,1,2,1,2,3]))


# given a string , generate a new string and print a string with consecutive letters in it


def print_consective (str):
    st=""
    for i in range (0,len(str),2):
        st=st+str[i]
    return st

print(print_consective("hello"))
print(print_consective("hi"))
print(print_consective("heeololeo"))

# givern two string return true if either of them appear at ther very end of each other case senitive is not taken as  case
def compareEnd(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        if s1[len1-len2:len1]==s2:
            return True
        else:
            return False
    else:
        if s2[len2-len1:len2]==s1:
            return True
        else:
            return False
         
print(compareEnd("abced","bcd"))

# given a string , return a string for verye char in the original 

def doubleString(ss):
    st=""
    for  i in range (0,len(ss)):
        st+=ss[i]*2
    print (st)
    return st
print(doubleString("hello"))

# count sum except teens
def countExceptTeens(a,b,c):
    sum=0
    if not checkteen(a):
        sum+=a
    if not checkteen(b):
        sum+=b
    if not checkteen(c):
        sum+=c
    return sum
        

def checkteen(a):
    if a>10 and a<=19:
        if a==15 or a==16:
            return False
        else:
            return True
print(countExceptTeens(10,5,15))
print(countExceptTeens(10,5,17))
print(countExceptTeens(1,16,15))



#  guess the number with 3 hint possible
import random
randi = random.randint(100,999)
print(randi)
st=str(randi)
print(st)

count=0
while count!=3:
    count=0
    inp=(input("Enter the number"))
    for i in range(len(st)):
        if st[i]==inp[i]:
            count+=1
    
    if(count==3):
        print("you won")
        break
    elif (count==1 or count==2):
        print("you are close")
    else:
        print("You guessed wrong")
        