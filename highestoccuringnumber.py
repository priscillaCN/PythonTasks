def highest_occuring_number(numbers):
    
    highest_occuring = 0
    final_count = 0
    
    for range in numbers:
        count = 0
        
        for digit in numbers:
     
            if range == digit :
                count +=1
                
        if(count > final_count):
            final_count = count
            highest_occuring = range
            
                
    return highest_occuring
	
