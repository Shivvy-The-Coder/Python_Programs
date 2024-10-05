# WAP to take 3 favourite movues form user and store it in a list

print("Enter the name of your three favourite movies")
movies=[]
for i in range (0,3):
 movie=input("Enter your movie")
 movies.append(movie)

print(movies)


#WAP to check wheter a list contain a pallindrome or not
list =[1,2,2,3,1]
list2=list.copy()
list2.reverse()
if list==list2:
 print("it is a pallindrome")
else:
 print("it is not a pallindrome")


#Write a program to count the numer of student of grade A in tuple
tup=('C','D','B','B','A','A','A')
print(tup.count('A'))

ll=[]
for i in tup:
# this is how we access the elements of tup  via for loop
 ll.append(i)

ll.sort()
print(ll)
