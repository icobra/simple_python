#!/usr/bin/python3
"""
    Polybius square
    Simple cipher
"""
import sys

"""
 	1 	2 	3 	4 	5 	6
1 	А 	Б 	В 	Г 	Д 	Е
2 	Ё 	Ж 	З 	И 	Й 	К
3 	Л 	М 	Н 	О 	П 	Р
4 	С 	Т 	У 	Ф 	Х 	Ц
5 	Ч 	Ш 	Щ 	Ъ 	Ы 	Ь
6 	Э 	Ю 	Я 	- 	- 	- 
"""


# Make dictonary
def make_dictionary(alphabets_used):
    SIGNS = '1234567890!@#$%&()-=+/*<>,.\'"\\{}:;'
    ENG_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    RUS_LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    if alphabets_used == "en":
        alphabet = ENG_LETTERS + ENG_LETTERS.upper() + SIGNS
        alphabet_len = 86
    elif alphabets_used == "rus":
        alphabet = RUS_LETTERS + RUS_LETTERS.upper() + SIGNS
        alphabet_len = 100
    else:
        print("Sorry, part under construction - use rus or en only")
        alphabet = RUS_LETTERS + RUS_LETTERS.upper() + SIGNS
        alphabet_len = 100
        """
        alphabet = ENG_LETTERS + ENG_LETTERS.upper() +\
        RUS_LETTERS + RUS_LETTERS.upper() + SIGNS
        alphabet_len = 169
        pass // TODO
        """
    def dict_generator(alphabet_len, alphabet):
        numbers = ["%02d"%(num) for num in range(alphabet_len)]
        letter_dict = {}
        for x in range (alphabet_len):
            letter_dict[alphabet[x]] = numbers[x]
        return letter_dict 

    new_dict = dict_generator(alphabet_len, alphabet)
    return new_dict
   

# Code
def code(fraze, dictionary):
    new_txt = ""
    list_fraze = list(fraze)
    for x in fraze:
        if x in dictionary:
            new_txt += dictionary.get(x)
        else:
            new_txt += (x + x)
    return new_txt

# Decode
# 63  3162123162  42161263 - test fraze
def decode(fraze, dictionary):
    new_txt = ""
    list_fraze = []
    # str to list with letter length steep 
    step = 2
    for i in range(0, len(fraze), 2):
        list_fraze.append(fraze[i:step])
        step += 2
    # list to decode fraze
    key_dictionary_list = list(dictionary.keys())
    val_dictionary_list = list(dictionary.values())  

    for x in list_fraze:
        if x in val_dictionary_list:
            i = val_dictionary_list.index(x)
            new_txt += key_dictionary_list[i]
        else:
            new_txt += x[0:1]
    return new_txt 

# Main
def main():
    # Choose mode
    
    option = sys.argv
    if len(option) == 1:
        print("You need more option. TODO HELP")
        return 0
    fraze = sys.stdin.read()
    lang = option[2]
    dictionary = make_dictionary(lang)
    if "-c" in option:
        output_txt = code(fraze,dictionary)    
    elif "-d" in option:
        output_txt = decode(fraze,dictionary)
    else:
        print("Wrong key. See help")
        return 1
    print(output_txt, end='')

main()

