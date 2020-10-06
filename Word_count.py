# put your code here.
# put your code here.

# define funcation(file):
#    open file 
#    strip non-alpha characters and right hand indent (.rstrip)
#    make each word .lower()
#    count_of_word_in_file = {"word": number}
#    for loop that is iterating over words not characters:
#        define count_of_word_file =  get function + 1
#    return count_of_word_in_file 
#    close file
#     

def get_word_count(file_name):
    """return count for each word in file."""
    file = open(file_name)
    
    count_of_word_in_file = {}
    words_in_file = []
    
    for line in file:
        line = line.lower()
        line = line.rstrip()
        line = line.split(" ")

        for each_word in line:
            each_word = each_word.rstrip(",").rstrip("?").rstrip(".")
            words_in_file.append(each_word)

    for word in words_in_file:
        count_of_word_in_file[word] = count_of_word_in_file.get(word, 0) + 1

    for word, count in count_of_word_in_file.items():
        print(word, count)


get_word_count("test.txt")


