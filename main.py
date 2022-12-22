path_to_file = 'books/frankenstein.txt'

def read_file(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):    
    counted_list = {}
    for letter in text:
        letter = letter.lower()
        if letter in counted_list:
            counted_list[letter]+=1
        else:
            counted_list[letter]=1            
    return counted_list

def print_report(path):
    text = read_file(path)
    num_words = word_count(text)
    chars_dict = count_letters(text)        
    sorted_char_list = convert_dict_to_list(chars_dict)

    print(f'--- Begin report of {path} ---')
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print('--- End report ---')

def sort_on(d):
    return d["num"]

def convert_dict_to_list(dict):
    list_items = []
    for item in dict:
        list_items.append({'char':item, 'num':dict[item]})
    list_items.sort(reverse=True, key=sort_on)
    return list_items

def main():
    print_report(path_to_file)

main()