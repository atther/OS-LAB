# Program for Fibonacci 
# Series 
echo "Enter N"
read N
# Static input fo N 
#N=6 
  
# First Number of the 
# Fibonacci Series 
a=0 
  
# Second Number of the 
# Fibonacci Series 
b=1  
   
echo "The Fibonacci series is : "
   
for (( i=0; i<N; i++ )) 
do
    echo -n "$a "
    fn=$((a + b)) 
    a=$b 
    b=$fn 
done
# End of for loop 

'''
OUPUT:
Enter N
4
The Fibonacci series is : 
0 1 1 2 

'''
