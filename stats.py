# Grabs the file and turns its contents into a string
def get_book_text(filename):
    with open(filename) as f:
        book_text = f.read()
    return book_text

# Takes the string input and counts the number of characters 
def get_book_words(text_in):
    counter = 0
    words = text_in.split()
    for word in words:
        counter += 1
    return counter

#Takes a text input and generates a counter of each character in the text
def get_book_chars(text): 
    chars = {}
    for unit in text:
        item = unit.lower()
        has = False
        #This loop checks the current char list for the character, if it has it, it adds 1
        for char in chars:
            if char == item:
                chars[char] += 1
                has = True
        #After checking all chars, if it cannot find the char, it adds it to the dictionary
        if has == False:
            chars[item] = 1
    return chars

def sortlist(character_dict):
    baselist = []
    for char in character_dict:
        baselist.append({"char": char, "num": character_dict[char]})
    def sort_on(item):
        return item["num"]
    baselist.sort(reverse=True, key=sort_on)
    return baselist

def printformat(list,path,words):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    print(f"----------- Word Count ----------\nFound {words} total words")
    print("-------- Character Count -------")
    for item in list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    return 0