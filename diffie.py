import random
def checklist(pri):
	duplicate=[]
	duplicate= pri
	check=1
	for i in range(len(pri)):
		for j in range(i+1,len(pri)):
			if pri[i]==duplicate[j]:
				check=0
				break
			else:
				check=1
				continue
		break	 
	return check


q=int(input("Enter the prime no."))
n=int(input("Enter no of users"))
keys=[]
for i in range(n):
	print("Enter secret key for user",i+1)
	key=int(input())
	keys.append(key)
if(n>2):	
	print("Enter the users between whom you want to communicate")
	temp1=int(input("Enter the user 1 "))
	xa=keys[temp1-1]
	temp2=int(input("Enter the user 2 "))
	xb=keys[temp2-1]
else:
	xa=keys[0]
	xb=keys[1]	
p=0
a=[]
pri=[]
alpha=0
for i in range(1,q):
	for j in range(1,q):
		pri.append((i**j)%(q))
	print(pri)	
	print(checklist(pri))
	if(checklist(pri)==1):
		p+=1
		a.append(i)
	pri.clear()
print(a)
alpha=random.choice(a)
print(alpha)
ya=(alpha**xa)%q
print("Public key of a:",ya)				
yb=(alpha**xb)%q
print("Public key of b:",yb)
Kab1=(yb**xa)%q
print("Shared session key with respect to user A is",Kab1)
Kab2=(ya**xb)%q
print("Shared session key with respect to user B is",Kab2)

'''Output
Case 1:
spit@NEW-Lab-702-U25:~/Desktop$ python3 diffie.py
Enter the prime no.11
Enter no of users3
Enter secret key for user 1
8
Enter secret key for user 2
4
Enter secret key for user 3
7
Enter the users between whom you want to communicate
Enter the user 1 1
Enter the user 2 2
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
0
[2, 4, 8, 5, 10, 9, 7, 3, 6, 1]
1
[3, 9, 5, 4, 1, 3, 9, 5, 4, 1]
0
[4, 5, 9, 3, 1, 4, 5, 9, 3, 1]
0
[5, 3, 4, 9, 1, 5, 3, 4, 9, 1]
0
[6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
1
[7, 5, 2, 3, 10, 4, 6, 9, 8, 1]
1
[8, 9, 6, 4, 10, 3, 2, 5, 7, 1]
1
[9, 4, 3, 5, 1, 9, 4, 3, 5, 1]
0
[10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
0
[2, 6, 7, 8]
8
Public key of a: 4
Public key of b: 2
Shared session key with respect to user A is 5
Shared session key with respect to user B is 5


Case 2:
Enter the prime no.11
Enter no of users2
Enter secret key for user 1
4
Enter secret key for user 2
5
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
0
[2, 4, 8, 5, 10, 9, 7, 3, 6, 1]
1
[3, 9, 5, 4, 1, 3, 9, 5, 4, 1]
0
[4, 5, 9, 3, 1, 4, 5, 9, 3, 1]
0
[5, 3, 4, 9, 1, 5, 3, 4, 9, 1]
0
[6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
1
[7, 5, 2, 3, 10, 4, 6, 9, 8, 1]
1
[8, 9, 6, 4, 10, 3, 2, 5, 7, 1]
1
[9, 4, 3, 5, 1, 9, 4, 3, 5, 1]
0
[10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
0
[2, 6, 7, 8]
6
Public key of a: 9
Public key of b: 10
Shared session key with respect to user A is 1
Shared session key with respect to user B is 1
'''