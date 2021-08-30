a=int(input())
def fib (a): 
   Array = [0] * (a+1) 
   Array[1] = 1
   for i in range (2,a+1): 
      Array[i] = Array[i-1] + Array[i-2] 
   return Array[a] 
print(fib(a))


##Question: Creating an array in the function to find the nth number in Fibonacci series
