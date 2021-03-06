#!/usr/bin/env python
# coding: utf-8

# In[2]:


######### ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] 
word = "ACADGILD" 
alphabet_list = [ alphabet for alphabet in word ] 
print ("ACADGILD => " + str(alphabet_list)) 

######### ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>] 
input_list = ['x','y','z'] 
result = [ item*num for item in input_list for num in range(1,5)  ] 
print("['x','y','z'] => " +   str(result)) 
#########

######### ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 
# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>] 
input_list = ['x','y','z'] 
result = [ item*num for num in range(1,5) for item in input_list  ] 
print("['x','y','z'] => " +   str(result)) 
#########
 
######### [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
input_list = [2,3,4] 
result = [ [item+num] for item in input_list for num in range(0,3)] 
print("[2,3,4] =>" +  str(result)) 
#########
 
######### [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
input_list = [2,3,4,5] 
result = [ [item+num for item in input_list] for num in range(0,4)  ] 
print("[2,3,4,5] =>" +  str(result)) 
#########
 
######### [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
input_list=[1,2,3] 
result = [ (b,a) for a in input_list for b in input_list] 
print("[1,2,3] =>" +  str(result)) 
######### 

