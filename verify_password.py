import re


""" 
This function check if password created by user follows the below given norms as per website.
    * the password must begin with a latin letter,
    * the password can consist of Latin letters, numbers, dot and minuses,
    * the password must end only with a latin letter or number;
    * minimum password length is one character
    * maximum password length is 20 characters
"""
def check_password(password): 
    flag = True 
    min_flag =len(password)<1
    max_flag = len (password)>20
    start_flag = bool(re.search('^[a-zA-Z]', password))
    end_flag = bool(re.search('[a-zA-Z0-9]$', password))
    spl_flag = bool(re.search('^[a-zA-Z0-9-.]+$', password))
    
    if min_flag :
        print("password must be at least 1 character long")
        flag = False
    if max_flag :
        print("password must be not more than 20 character long")
        flag = False
    if start_flag==False:
        print("password must start with alphabet")
        flag = False
    if end_flag == False:
        print("password must end with alphanumeric latter")
        flag = False
    if spl_flag == False:
        print("password should not contain special symbols")
        flag = False
    if flag :
        print ("Its Valid Password !!!")
    return flag
