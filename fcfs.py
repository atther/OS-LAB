at=[]
bt=[]
ct=[]
wt=[]
tat=[]
avgtat=0
avgwt=0

print("Enter the number of process: ")
n=int(input())
print("Enter the burst time of the processes: \n")
bt=list(map(int, raw_input().split()))

print("Enter the Arrival time of the processes: \n")
at=list(map(int, raw_input().split()))

wt.insert(0,0)
tat.insert(0,bt[0])

ct.append(bt[0]+at[0]+wt[0])
for i in range(1,n):
	ct.insert(i,ct[i-1]+bt[i])
	tat.insert(i,ct[i]-at[i])   #  or bt+wt
	wt.insert(i,tat[i]-bt[i])
	
for i in range(n):
	avgwt+=wt[i]
	avgtat+=tat[i]

avgwt=float(avgwt)/n
avgtat=float(avgtat)/n
print("\n")
print("Arrival Time\t  Burst Time\t  Compeletion Time\t  Turn Around Time\t  Waiting Time")

for i in range(0,n):
   print(str(at[i])+"\t\t\t"+str(bt[i])+"\t\t\t"+str(ct[i])+"\t\t\t"+str(tat[i])+"\t\t\t"+str(wt[i]))
   print("\n")

print("Average Waiting time is: "+str(avgwt))
print("Average Turn Around Time is: "+str(avgtat))

'''
Enter the number of process: 
4
Enter the burst time of the processes: 

8 4 9 5
Enter the Arrival time of the processes: 

0 1 2 3

Arrival Time	  Burst Time	  Compeletion Time	  Turn Around Time	  Waiting Time
0			8			8			8			0


1			4			12			11			7


2			9			21			19			10


3			5			26			23			18


Average Waiting time is: 8.75
Average Turn Around Time is: 15.25

'''
