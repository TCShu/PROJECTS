# Prolog
# Authors: Ticiana Ward, Shawn Shen, Tomy Vu
# Email: ticiana.ward@gmail.com
# Date: 2021-10-14
''' 
Purpose: create a password generator that can generate a random password with the following options:
1. Random password (user inputs how many characters)
2. Random password (included only letters)
3. Random password (includes only numbers)
4. Random password (user can adjust where certain characters appear front/end)
'''
import random
import string   

# list of characters (uppercase, lowercase, symbols, numbers)
upper = [chr(i) for i in range(65, 91)]
lower = [chr(i) for i in range(97, 123)]
symbol = string.punctuation
number = ["0","1","2","3","4","5","6","7","8","9"]

# funtion for random password that takes the ammount of characters from user input
def random_password(uppercase,lowercase,symbols,numbers): 
    password=""

# chooses random uppercase letter from the list and adds it to the password until it hits the user input lenght
    for i in range(uppercase):
        password += random.choice(upper)

# chooses random lowercase letter from the list and adds it to the password until it hits the user input lenght
    for i in range(lowercase):
        password += random.choice(lower)

# chooses random symbol from the list and adds it to the password until it hits the user input lenght
    for i in range(symbols):
        password += random.choice(symbol)
    
# chooses random number from the list and adds it to password until it hits the user input lenght
    for i in range(numbers):
        password += random.choice(number)

# shuffles all the characters in the password    
    password=''.join(random.sample(password,len(password)))

    return password 

# funtion for a (letters only) random password generator that takes the ammount of characters from the user input
def random_password_letters(uppercase,lowercase): 
    password=""

# chooses random uppercase letter from the list and adds it to the password until it hits the user input lenght
    for i in range(uppercase):
        password += random.choice(upper)

# chooses random lowercase letter from the list and adds it to the password until it hits the user input lenght
    for i in range(lowercase):
        password += random.choice(lower)
    
# shuffles all the characters in the password     
    password=''.join(random.sample(password,len(password)))

    return password

# funtion for a (numbers only) random password generator that takes the ammount of characters from the user input
def random_password_numbers(numbers): 
    password=""
    
# chooses random number from the list and adds it to password until it hits the user input lenght
    for i in range(numbers):
        password += random.choice(number)

# shuffles all the characters in the password     
    password=''.join(random.sample(password,len(password)))

    return password

# funtion for a random password generator
def random_password_adjust():
    upper2=""
    lower2=""
    symbol2=""
    number2=""

# ask user how many characters they want in the password
    uppercase=int(input("How many uppercase letters do you want in the password? "))
    lowercase=int(input("How many lowercase letters do you want in the password? "))
    symbols=int(input("How many symbols do you want in the password? "))
    numbers=int(input("How many numbers do you want in the password? "))

# create a varible that assigns a string of upperletter characters 
    for i in range(uppercase):
        upper2 += random.choice(upper)

# create a varible that assigns a string of lowerletter characters 
    for i in range(lowercase):
        lower2 += random.choice(lower)

# create a varible that assigns a string of symbols
    for i in range(symbols):
        symbol2 += random.choice(symbol)
    
# create a varible that assigns a string of numbers characters 
    for i in range(numbers):
        number2 += random.choice(number)

# ask user if they want specific characters at the front of the password
    a=input("Do you want your upper cases at the start? ")
    if a=="n"or a=="N":
        b=input("Do you want your lower cases at the start? ")
        if b=="n"or b=="N":
            c=input("Do you want your symbols at the start of the password? ")
            if c=="n"or c=="N":
                d=input("Do you want your numbers at the start of the password? ")
                
# if user responds with NO in all cases generate a random password                
                if d=="n"or d=="N":
                    print("I'm sorry but you can't do that! ")
                    print("I guess you can just have a random password then.\n")
                    random_password(uppercase,lowercase,symbols,numbers)
    
# ask user if they want specific characters at the end of the password (numbers at the front)
                else:
                    u=input("Do you want your upper cases at the end? ")
                    if u=="n"or u=="N":
                        l=input("Do you want your lower cases at the end? ")
                        if l=="n"or l=="N":
                            s=input("Do you want your symbols at the end? ")

# if user responds with NO in all cases generate a random password 
                            if s=="n"or s=="N":
                                print("I'm sorry but you can't do that! ")
                                print("I guess you can just have a random password then.\n")
                                random_password(uppercase,lowercase,symbols,numbers)
# if user chooses to have numbers at the front and symbols at the end of the password
                            else:
                                middle=upper2+lower2
                                middle=''.join(random.sample(middle,len(middle)))
                                password=number2+middle+symbol2
# if user chooses to have numebers at the front and lowercase letters at the end of the password                             
                        else:
                            middle=upper2+symbol2
                            middle=''.join(random.sample(middle,len(middle)))
                            password=number2+middle+lower2
# if user chooses to have numbers at the front and uppercase letters at the end of the password
                    else:
                        middle=lower2+symbol2
                        middle=''.join(random.sample(middle,len(middle)))
                        password=number2+middle+upper2

# ask user if they want specific characters at the end of the password (symbols at the front)
            else: 
                u=input("Do you want your upper cases at the end? ")
                if u=="n"or u=="N":
                        l=input("Do you want your lower cases at the end? ")
                        if l=="n"or l=="N":
                            n=input("Do you want your numnbers at the start of the end? ")
# if user responds with NO in all cases generate a random password                            
                            if n=="n"or n=="N":
                                print("I'm sorry but you can't do that! ")
                                print("I guess you can just have a random password then.\n")
                                random_password(uppercase,lowercase,symbols,numbers)
# if user chooses to have symbols at the front and numbers at the end of the password                                
                            else:
                                middle=upper2+lower2
                                middle=''.join(random.sample(middle,len(middle)))
                                password=symbol2+middle+number2
# if user chooses to have symbols at the front and lowercase letters at the end of the password                                
                        else:
                            middle=upper2+number2
                            middle=''.join(random.sample(middle,len(middle)))
                            password=symbol2+middle+lower2
# if user chooses to have symbols at the front and uppercase letters at the end of the password                            
                else:
                    middle=number2+lower2
                    middle=''.join(random.sample(middle,len(middle)))
                    password=symbol2+middle+upper2

# ask user if they want specific characters at the end of the password (lowercase letters at the front)                    
        else:
            u=input("Do you want your upper cases at the end? ")
            if u=="n"or u=="N":
                    s=input("Do you want your symbols at the end? ")
                    if s=="n"or s=="N":
                        n=input("Do you want your numbers at the end? ")

# if user responds with NO in all cases generate a random password                         
                        if n=="n"or n=="N":
                            print("I'm sorry but you can't do that! ")
                            print("I guess you can just have a random password then.\n")
                            random_password(uppercase,lowercase,symbols,numbers)
# if user chooses to have lowercase letters at the front and numbers at the end of the password 
                        else:
                            middle=upper2+symbol2
                            middle=''.join(random.sample(middle,len(middle)))
                            password=lower2+middle+number2
# if user chooses to have lowercase letters at the front and symbols at the end of the password                             
                    else:
                        middle=upper2+number2
                        middle=''.join(random.sample(middle,len(middle)))
                        password=lower2+middle+symbol2
# if user chooses to have lowercase letters at the front and uppercase letters at the end of the password                         
            else:
                middle=number2+symbol2
                middle=''.join(random.sample(middle,len(middle)))
                password=lower2+middle+upper2   

# promt user if they want specific characters at the end of the password (uppercase letters at the front)                
    else:       
        l=input("Do you want your lower cases at the end? ")
        if l=="n"or l=="N":
            s=input("Do you want your symbols at the end? ")
            if s=="n"or s=="N":
                n=input("Do you want your numbers at the end? ")

# if user responds with NO in all cases generate a random password                 
                if n=="n"or n=="N":
                    print("I'm sorry but you can't do that! ")
                    print("I guess you can just have a random password then.\n")
                    random_password(uppercase,lowercase,symbols,numbers)
# if user chooses to have uppercase letters at the front and numbers at the end of the password                     
                else:
                    middle=lower2+symbol2
                    middle=''.join(random.sample(middle,len(middle)))
                    password=upper2+middle+number2
# if user chooses to have uppercase letters at the front and symbols at the end of the password                     
            else:
                middle=lower2+number2
                middle=''.join(random.sample(middle,len(middle)))
                password=upper2+middle+symbol2
# if user chooses to have uppercase letters at the front and lowercase letters at the end of the password                     
        else:
            middle=number2+symbol2
            middle=''.join(random.sample(middle,len(middle)))
            password=upper2+middle+lower2

    return password

# main funtion
def main():

# introdution messege
    print("HELLO!! Welcome to our JettPassword Generator!")
    print("Please answer the question with y or n")
    print("This program can generate the following type of passwords")
# display choices
    print()
    print("     1.  Random password (user inputs how many characters)")
    print("     2.  Random password (included only letters)")
    print("     3.  Random password (includes only numbers)")
    print("     4.  Random password (user can adjust where certain characters appear front/end)")
    print()
    question=input("Which type of password would you like to generate?(Answer either 1, 2, 3, or 4) ")
# user choice 1 
# ask how many characters they want in the password
    if question =="1":
        a=int(input("How many uppercase letters do you want in the password? "))
        b=int(input("How many lowercase letters do you want in the password? "))
        c=int(input("How many symbols do you want in the password? "))
        d=int(input("How many numbers do you want in the password? "))
        print(random_password(a,b,c,d))
# choice 2
# ask how many characters they want in the password      
    elif question == "2":
        a=int(input("How many uppercase letters do you want in the password? "))
        b=int(input("How many lowercase letters do you want in the password? "))
# choice 3
# ask how many characters they want in the password              
        print(random_password_letters(a,b))
    elif question == "3":
        a=int(input("How many numbers do you want in the password? "))
        print(random_password_numbers(a))
# choice 4        
# ask how many characters they want in the password      
    elif question == "4":
        print(random_password_adjust())
# if user chooses to answer with anything else display dissappointing messege
    else:
        print(f'{question} was not an option -_-')
        try_again=input("Therefore, I will give you one more try, do you want to generate a new password? ")
        if try_again=="y" or try_again=="Y":
            main()
        else:
            print("bye bye")
main()
