echo "Enter N:"
read N
echo "Enter Numbers "
declare arr
sum=0
for (( i=0; i<N; i++ ))
do 
	read arr[i]
	sum=$(expr $sum + ${arr[i]})

done
echo "SUM:" $sum

'''
OUPUT:
Enter total Number
4
Enter Numbers
1
2
3
4
sum: 10

'''
