# Collitz 0502

def equation(n):
    result = int(3 * n + 1) 
    result = n
    # We want to limit the session 
    session_count = 0 
    session_limit = 30
    
# We want the program to contineously run the equation and bring back the equation

    while result != 1: 

        # We do a while_loop to contineously run the equation again and again. While the result is the result, 
        # the loop continue to run the command. #
        # Or we can also state that while result is not equal to one, run the command #
       
        if result % 2 == 0: 
            result = int(result / 2)
            print(result)
            
            session_count += 1 

        else:
            result = int(3 * result + 1 )
            print(result)
            
            session_count += 1 

# We call in the function to execute the code 

num = int(input('Number: '))
equation(num) 

