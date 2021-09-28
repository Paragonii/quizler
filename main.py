import random
#Generate 2 random numbers
a = random.randint(1,1000)
b = random.randint(1,1000)

print(' '+str(a)+'\n+`'+str(b))
#Take user prompt
ans = int(input())
if a+b==ans:
print('Congratulations! Ans is correct')
else:
print('Sorry! Correct ans is '+str(a+b))
