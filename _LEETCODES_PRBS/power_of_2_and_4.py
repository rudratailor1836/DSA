class power_of_4:
    def isPowerOfFour(self, n: int) -> bool:
        # here '&' is bit operation  which will help to check if the number is power of 2 
        #  if you  have noticed all odd power of 2 when divided by 3 gives remainder 2 and all even power of 2 divided by 3 gives remainder 1 
        #  now we know that 4^k = (2^2)^k so all even power of 2 is the power of 4
        return (n & (n-1)) == 0 and n % 3 == 1
    
class power_of_2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n-1))
        