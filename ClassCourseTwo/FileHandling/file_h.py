def make_file():
    my_file = open("demo.txt","a")

    for i in range(10):
        my_file.write("hello world")

    my_file.close()

def count_words():
    #open file
    my_file = open("demo.txt","r")
    total_words = 0
    for i in my_file:
        total_len = len(i)
        line_words = 0
        space = 0
        for j in range(total_len):
            if i[j] == " ":
                space += 1
        line_words = space + 1
        total_words += line_words
  
    return total_words


print(count_words())