def is_isogram(string):
    no_char_match = True

    char_string = split_string(string)
    counter=1
    count=1
    for char in char_string:
        if char.isalpha():
            while count < len(char_string):
                if char.lower() == char_string[count].lower():
                    no_char_match = False
                count = count + 1
        counter = counter + 1        
        count = counter       
    return no_char_match

def split_string(word):
    return [char for char in word] 

