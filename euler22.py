'''
 def function():
    // get all the names and convert into something we can sort
    // sort the names alphabetically

    // function? name position
        for each name
            get index 
            // function? alphabetical value
                // get each letter in the name
                // find alphabetical position 
                // add each letter's position
            // multiply the alphabetical value by the position and return the score

    // add all the scores

'''

def alphebetical_value(name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetical_value = 0


    for letter in name:
        letter_lowercase = letter.lower()
        letter_position = alphabet.find(letter_lowercase) + 1
        alphabetical_value += letter_position
    return alphabetical_value


def alphabetize_file_names(file):
    file_of_names = open(file)
    string_of_names = file_of_names.read()
    list_of_names = string_of_names.split(',')
    processed_names = []

    for name in list_of_names:
        name = name.replace('"', '')
        processed_names.append(name)

    alphabetized_names = sorted(processed_names)
    return alphabetized_names

def get_final_value(alphabetized_names):
    final_value = 0

    for i in range(0, len(alphabetized_names)):
        final_value += alphebetical_value(alphabetized_names[i]) * (i+1)
    return final_value




