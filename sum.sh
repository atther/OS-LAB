echo "Enter total Number"
read N

i=1
sum=0

echo "Enter Numbers"
while [ $i -le $N ]
do
  read num
  sum=$((sum + num))
  i=$((i + 1))
done

echo "sum: $sum"

'''
OUTPUT:
Enter total Number
4
Enter Numbers
1
2
3
4
sum: 10

'''
