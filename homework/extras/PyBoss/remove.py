# put your code below
def remove_vowels(string):
    '''
    Removes all vowels from a string.
    Parameters:
    ----------
    string : (str)
        The string from which vowels should be removed.
    Return:
    ----------
    The string without any vowels.
    '''
    vowels = ('a', 'e', 'i', 'o', 'u')
    for letter in string.lower():
        if letter in vowels:
            string = string.replace(letter, '')
    return string


print(remove_vowels("George"))
