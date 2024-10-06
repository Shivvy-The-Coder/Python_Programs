# store the following word meaning in  a dictionary
# table : "A peice of furniture","list if facts and figures"
# cat : "a small animal"

lis =[ "A peice of furniture","list if facts and figures"]
dic={}
dic.update({"table":lis})
dic.update({"cat":"a small animal"})

print(dic)


# you are given a list of subjects for students.Assume one classroom is required for 1 subject.How many clasrrom are
# needed by all students


set1 = set() 
# Use 'set1' or any other name instead of 'set'
set1.add("python")
set1.add("Java")
set1.add("C++")
set1.add("python")
set1.add("JavaScript")
set1.add("Java")
set1.add("python")
set1.add("Java")
set1.add("C++")
set1.add("C")

print(len(set1)) 
# This will work correctly now



# WAP to enter marks of 3 subjects from the usr and store them ina dictionary . tart with  an empty d
# dicitonary and add  one by one. use subject name as key and mark as value

subject ={}
subject.update({"math":90})
subject.update({"english":70})
subject.update({"COA":99})

print(subject)

#  figure a way to store 9 and 9.0 as separate value in the set
vals= set()
vals.add(9)
vals.add(float(9.0))
print(vals)

vals= set()
tup=(9,9.0)
vals.add(tup)
print(vals)