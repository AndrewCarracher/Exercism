# Doesn't pass tests due to difference in number of characters being returned 

number_array = ["first","second","third","fourth","fith","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"] 
                
song = {
    "first" : "a Partridge in a Pear Tree.",
    "second" : "two Turtle Doves",
    "third" : "three French Hens",
    "fourth" : "four Calling Birds",
    "fith" : "five Gold Rings",
    "sixth" : "six Geese-a-Laying",
    "seventh" : "seven Swans-a-Swimming",
    "eighth" : "eight Maids-a-Milking",
    "ninth" : "nine Ladies Dancing",
    "tenth" : "ten Lords-a-Leaping",
    "eleventh" : "eleven Pipers Piping",
    "twelfth" : "twelve Drummers Drumming"
    }


def check_difference(start_verse, end_verse):
    if start_verse == end_verse:
        return False
    else:
        return True
    

def check_validity(start_verse, end_verse):
    if start_verse > 0 and end_verse < 13:
        return True
    else:
        raise ValueError("Start Verse must be 1 or greater and End Verse must be 12 or less")
        return False

def create_constant_phrase(index_end):
    end_day = number_array[index_end]
    return f"On the {end_day} day of Christmas my true love gave to me: "

def create_list(index_start, index_end, c):
    list_to_return = []
    count =  index_end
    
    while count >= index_start:
        day = number_array[count]
        if list_to_return == "day":
            list_to_return.append(day)
        else:
            line_to_add = song.get(day)
            if index_start != 0:
                if count != index_start:
                    line_to_add = line_to_add + ", "
                else:
                    line_to_add = line_to_add + ". "
            else:
                if count == 1:
                    line_to_add = line_to_add + ", and"
                else:
                    line_to_add = line_to_add + ", "
                    
            list_to_return.append(line_to_add)
            
        count = count - 1
        
    return list_to_return
        

def recite(start_verse, end_verse):
    if check_validity(start_verse, end_verse):
        
        index_start = start_verse - 1
        index_end = end_verse - 1    
        
        if not check_difference(start_verse, end_verse):
            days = create_list(0, index_end, "day")
            verses = create_list(0, index_end, "verse")
        else:
            days = create_list(start_verse, index_end, "day")
            verses = create_list(start_verse, index_end, "verse")

        end_day = days[0]
        constant_phrase = create_constant_phrase(index_end)

        return constant_phrase, [verse for verse in verses];
    
    
