def Fizzbuzz(a,b):
    c = len(a) + len(b)
    if ((c % 3) == 0 and (c % 5) == 0):
        print "FizzBuzz"
    else:
        if((c % 5) == 0):
            print "Buzz"
        elif((c % 3) == 0):
            print "Fizz"


    
