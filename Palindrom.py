def is_palindrome(given):
    '''
    Function returning True/Fals value depending whether the word given is a palindrome or not
    Arguments:
    word in a str format
    '''
    word = ""
    for i in given:
        if i.isalpha():
            word += i.lower()
    return word== word[::-1]
result=is_palindrome('Ada i w oplu żaba! – żul powiada')
print(result)