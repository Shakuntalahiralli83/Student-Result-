#program for set()
#creating two sets
set1=set()
set2=set()
#add iteams to set1 using add() and update()
set1.add(5)
s={30.35,40,45,50}
set1.update(s)
print("set1=",set1)
#add iteams toset2 using range()
set2=set(range(40,100,10))
print("set2=",set2)
#remove an iteam from set2 using remove() and discard()
set2.remove(60)
print("after removing item set2=",set2)
set2.discard(40)
print("after discarding an iteam set2=",set2)
#union of two sets using 1
set3=set1|set2
print("set1|set2=",set3)
#union of two sets using union()
set4=set1.union(set2)
print("set1.union(set2)=",set4)
