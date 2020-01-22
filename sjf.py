at=[]
bt=[]
ct=[]
wt=[]
tat=[]    
avgtat=0
avgwt=0     
print("Enter the number of process: ")
n=int(input())

print("Enter the Burst time of the processes: \n")
bt=list(map(int, raw_input().split()))
print("Enter the Arrival time of the processes: \n")
at=list(map(int, raw_input().split()))

ct.insert(0,bt[0])
wt.insert(0,0)
tat.insert(0,bt[0])


for i in range(0,len(bt)-1):  
 for j in range(1,len(bt)-i-1):
  if(bt[j]>bt[j+1]):
   temp=bt[j]
   bt[j]=bt[j+1]
   bt[j+1]=temp
   temp=at[j]
   at[j]=at[j+1]
   at[j+1]=temp



for i in range(1,n):
	ct.insert(i,ct[i-1]+bt[i])
	tat.insert(i,ct[i]-at[i])
	wt.insert(i,tat[i]-bt[i])
	avgwt+=wt[i]
	avgtat+=tat[i]




avgwt=float(avgwt)/n
avgtat=float(avgtat)/n

#Sorting based on arrival time
for i in range(0,len(bt)-1):  
 for j in range(0,len(bt)-i-1):
  if(at[j]>at[j+1]):
   
   temp=bt[j]
   bt[j]=bt[j+1]
   bt[j+1]=temp
   
   temp=at[j]
   at[j]=at[j+1]
   at[j+1]=temp
   
   temp=wt[j]
   wt[j]=wt[j+1]
   wt[j+1]=temp
   
   temp=tat[j]
   tat[j]=tat[j+1]
   tat[j+1]=temp
   
   temp=ct[j]
   ct[j]=ct[j+1]
   ct[j+1]=temp
   
   
   
print("\n")
print("Arrival time\t  Burst Time\t  Waiting Time\t  Turn Around Time\t  Completion Time")
for i in range(0,n):
 print(str(at[i])+"\t\t"+str(bt[i])+"\t\t\t"+str(wt[i])+"\t\t"+str(tat[i])+"\t\t\t"+str(ct[i]))
 print("\n")
print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))

'''
Output
Enter the number of process: 
4
Enter the Burst time of the processes: 

8 4 9 5
Enter the Arrival time of the processes: 

0 1 2 3


Arrival time	  Burst Time	  Waiting Time	  Turn Around Time	  Completion Time
0		8			0		8			8


1		4			7		11			12


2		9			15		24			26


3		5			9		14			17


Average Waiting time is: 7.75
Average Turn Arount Time is: 12.25

'''
