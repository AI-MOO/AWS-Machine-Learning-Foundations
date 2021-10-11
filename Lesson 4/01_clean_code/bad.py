s = [88, 92, 79, 93, 85] #student test scores 
print(sum(s)/len(s)) #print mean of test scores 

s1 = [x ** 0.5 * 10 for x in s] #curve socres wiuth square root method and store in new list
print(sum(s1)/len(s1)) 