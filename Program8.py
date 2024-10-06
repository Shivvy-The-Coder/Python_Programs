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
set1.add("java")
set1.add("C++")
set1.add("C")

print(len(set1)) 
# This will work correctly now
