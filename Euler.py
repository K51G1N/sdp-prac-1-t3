
#g18m6734
# This is my solution to Even Fibonacci numbers
# Greatest solution ever
def fib(): # For creating the fibonacci sequence
    nums = [1]
    num1 = 1
    num2 = 1
    num3 = 0
    while nums[-1] < 4000000:
        num3 = num1 + num2
        nums.append(num3)
        num1 = num2
        num2 = num3
    return nums
def even(alist): # finding the even numbers 
    cnt = 0
    data = []
    while cnt != len(alist):
        if (alist[cnt]%2) == 0:
            data.append(alist[cnt])
        cnt += 1
    return data
def add(alist): # adds all the even numbers 
    cnt = 0
    for i in alist:
        cnt += i
    return cnt


def SquareSum(n): #g17e4476 Calculates the Square of the sum and returns the answer
    sum = 0
    while(n > 0):
        sum += n
        n -= 1
    return sum*sum
    
def SumSquares(n): #g17e4476 Calculates the Sum of the Squares and returns the answer
    sumsq = 0
    while(n > 0):    
        sumsq += n*n
        n -= 1
    return sumsq
        
def sumOfPRimes(n): #g19p6350 Calcultes the sum of all the primes 
	sumprime = 0;
	for num in range(0, n):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           sumprime += num
		   
	return sumprime	   

def SumSquareDiff(n):
   return(SquareSum(n)-SumSquares(n)) #g17e4476 returns the difference between
  
  
def main():
	#g17e4476
    p6sol = SumSquareDiff(100)  #g17e4476 Solved project Euler 6, 'https://projecteuler.net/problem=6'
    print("Project Euler, Problem 6 solution: ")
    print(p6sol) #g17e4476 Solution Output
	
	#17t4564
    prime = 0 
    for i in range(0,1000):
        if i%3==0 or i%5==0:
            prime+=i
    print (prime)
	#When the main function is executed, it adds all the numbers (from 0 to 1000) that are divisible by either 3 or 5 and then prints out the total sum.
	# g18m6734 made this
	# for the second Euler Problem
    dat = fib()
    get = even(dat)
    a = add(get)
    print (a)


main()

