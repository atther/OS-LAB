print("Enter the Time Quantum: ")
tq=int(input())
print("Enter the number of process: ")
n=int(input())

at=[0]*n
bt=[0]*n
ct=[0]*n
wt=[0]*n
tat=[0]*n
rem_bt=[0]*n    
avgtat=0
avgwt=0

print("Enter the Burst time of the processes: \n")
bt=list(map(int, raw_input().split()))
print("Enter the Arrival time of the processes: \n")
at=list(map(int, raw_input().split()))

for i in range(n):
	rem_bt[i] = bt[i] 

t=0 # current time
while(1):
	done = True
	for i in range(n):
		if (rem_bt[i] > 0) : 
                	done = False
                	if (rem_bt[i] > tq) :
                		t += tq
                		rem_bt[i] -= tq
                	else:
                		t = t + rem_bt[i]
                		wt[i] = t - bt[i]
                		rem_bt[i] = 0
	if (done == True):
		break

for i in range(n):
	tat[i] = bt[i] + wt[i]
	avgwt+=wt[i]	# Averge wt
	avgtat+=tat[i]

avgwt=float(avgwt)/n
avgtat=float(avgtat)/n

   
print("\n")
print("Arrival time\t  Burst Time\t  Waiting Time\t  Turn Around Time\t  Completion Time")
for i in range(0,n):
 print(str(at[i])+"\t\t"+str(bt[i])+"\t\t\t"+str(wt[i])+"\t\t"+str(tat[i])+"\t\t\t"+str(ct[i]))
 print("\n")
print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))



'''
OUTPUT
Enter the Time Quantum: 
2
Enter the number of process: 
3
Enter the Burst time of the processes: 

10 5 8
Enter the Arrival time of the processes: 

1 2 3


Arrival time	  Burst Time	  Waiting Time	  Turn Around Time	  Completion Time
1		10			13		23			0


2		5			10		15			0


3		8			13		21			0


Average Waiting time is: 12.0
Average Turn Arount Time is: 19.6666666667

'''
