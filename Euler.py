
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


main()
