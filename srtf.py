n = int(input('Enter the no of processes\n'))
p = []
BT = []
AT = []
WT = [0]*n
CT = [0]*n
TAT = [0]*n
t = 0
orde = []

for i in range(n):
	p.append(i)
	AT.append(int(input("Enter the arrival time of process {}\n".format(i+1))))
	BT.append(int(input('Enter the burst time of process {}\n'.format(i+1))))

RT = BT[:]
print(RT)
def printall():
	print('Process\tAT\tBT\tCT\tWT\tTAT')

	for i in range(n):
		print(p[i],'\t',AT[i],'\t',BT[i],'\t',CT[i],'\t',WT[i],'\t',TAT[i])

def averT():
	sumT,sumW = 0,0
	for i in range(n):
		sumT += TAT[i]
		sumW += WT[i]
	avT = sumT/n
	avW = sumW/n
	print("Average Turn Around Time=",avT,"\nAverage Waiting Time=",avW)

printall()




while(sum(RT)!=0):
	CURR = []
	for i in range(n):
		if (AT[i]<=t) and (RT[i]!=0):
			CURR.append(RT[i])
	if sum(CURR)!=0:
		i = RT.index(min(CURR))
		orde.append(p[i])
		RT[i]-=1
		if(RT[i]==0):
			CT[i]=(t+1)
			TAT[i] = CT[i]-AT[i]
			WT[i] = TAT[i] - BT[i]
		t+=1
		print(RT)

print(t,'\n')
print('ORDER')
for i in range(len(orde)):
	print('Process',orde[i])

printall()



