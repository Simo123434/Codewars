def high_and_low(numbers):
    #find highest and lowest value from numbers
    
    nums = list(map(int, numbers.split()))
    
    print(min(nums), max(nums))
    
    numbers = str(min(nums)) + ' ' + str(max(nums))
        
    return numbers
    
high_and_low('1 2 3 4 5 6 7 8 9')