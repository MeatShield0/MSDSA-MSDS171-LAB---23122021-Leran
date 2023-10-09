#TOTAL COUNTS OF THE VOWELS 
def vowels():                                       #DEFINE THE FUNCTION
    user_string=input("enter the string")           #ENTERING THE STRING  
    print("THE USER ENTER STRING :", user_string)    #PRINTING THE STRING 
    total_counter=0 
    user_string=user_string.upper()     #MAKING THE STRING IN UPPER CASE 
    user_string=user_string.strip()     #REMOVING THE WIDE SPACE FROM THE STRING
    length_string=len(user_string)      #TOTAL LENGTH OF THE STRING
    print("THE TOTAL LENGTH OF THE STRING IS :",length_string)       #PRINTING THE TOTAL LENGTH OF THE STRING
    for letter in user_string: 
        if (letter =='A' or letter=='E'or letter=='I' or letter=='O'or letter=='U'): #IF FUNCTION TO CHECK THE VOWELS
            total_counter += 1                                                   #COUNTER TO COUNT THE NO OF VOWELS
    print("THE TOTAL VOWELS IN THE STRINGS ARE",total_counter)                  #PRINTING THE NO OF VOWELS
    #ASSIGNING THE VARIABLE TO COUNT THE EACH VARIABLE
    a1=0 
    e1=0
    i1=0
    o1=0
    u1=0
    #CHECKING THE OCCURENCE OF EACH VOWELS AND THEN PRINTING THE COUNT OF THE VOWELS
    for letter in user_string:
        if (letter=='A'):
            a1+=1
        elif (letter=='E'):
            e1+=1
        elif (letter=='I'):
            i1+=1
        elif (letter=='O'):
            o1+=1
        elif (letter=='U'):
            u1+=1 
    print("A=",a1)
    print("E=",e1)
    print("I=",i1)
    print("O=",o1)
    print("U=",u1)
    #calculation for the percentage of vowels in the string
    perc=0
    float(perc)     #USING FLOAT DATA TYPE AS PERCENTAGE IS IN DECIMAL
    perc=(total_counter*100)/length_string      #FORMULA TO CALCULATE THE PERCENTAGE
    print("THE PERCENTAGE OF THE VOWELS IN THE STRING ARE",perc)      #PRINTING THE PERCENTAGE
    #PROGRAM END!!!!!!!!!!!!!