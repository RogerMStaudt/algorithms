str = input("Write a string to reverse it: ")

def reverse_string(string, reversed_str=''):
    if string == '':
        return reversed_str
    
    return reversed_str + reverse_string(string[0:len(string) - 1], string[-1])


print(f'The reversed {str} string is {reverse_string(str)}')