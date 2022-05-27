# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file_open = open("C:\Users\freelance space\Desktop\python class\Reading-Text-Files\Reading-Text-Files\story.txt" , "r")
    read_file_content = file_open.read()
    file_open.close()
    
    print(read_file_content)
    


def count_words():
    text = read_file_content("C:\Users\freelance space\Desktop\python class\Reading-Text-Files\Reading-Text-Files./story.txt")
    # [assignment] Add your code here
    
    
    return {"as": 10, "would": 20}