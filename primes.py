# Create a list of prime numbers we've found
foundprimes = []

def main():
    # 1 isn't considered a prime number - it's much more special!
    for number in range(2,10000):
        result = testprimes(number)
        if result  == number:
            print("{} is a prime number. It is only divisible by 1 and itself".format(number))
        else:
            print("{} is divisible by {}, and therefore isn't a prime number".format(number,result)) 

def testprimes(number): 
    for prime in foundprimes: 
        if not number % prime: 
            return prime 
    foundprimes.append(number)  
    return number 

if __name__ == "__main__":
    main()
