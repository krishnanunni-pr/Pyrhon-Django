# def check_palindrome(str):
#     reverse = str[::-1]
#     check=1
#     if(str!=reverse):
#         check=0
#     return check
#

def check_palindrome(str):
    reverse=str[::-1]
    check=1
    if(str!=reverse):
        check=0
    return check

str = input("Enter the string: ")
check= check_palindrome(str)
if(check==1):
    print("Is a palindrome ")
else:
    print("Not a palindrome")