def is_palindrome(word):
    '''
    Function returning True/Fals value depending whether the word given is a palindrome or not
    Arguments:
    word in a str format
    '''
    if word == word[::-1]:
        return True
    else: 
        return False
       
result=is_palindrome('kajak')
print(result)
help(is_palindrome)