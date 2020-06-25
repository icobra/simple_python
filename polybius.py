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

# Hard dictonary
# TODO to many languages
SIGNS = '1234567890!@#$%&()-=+/*<>,.\'"\\{}:;'
ENG_LETTERS = "abcdefghijklmnopqrstuvwxyz"
RUS_LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

hard_dictionary = {"А":"11", "Б":"12", "В":"13", "Г":"14", "Д":"15", "Е":"16",
    "Ё":"21", "Ж":"22", "З":"23", "И":"24","Й":"25", "К":"26", "Л":"31",
    "М":"32", "Н":"33", "О":"34", "П":"35", "Р":"36", "С":"41", "Т":"42",
    "У":"43", "Ф":"44", "Х":"45", "Ц":"46", "Ч":"51", "Ш":"52", "Щ":"53",
    "Ъ":"54", "Ы":"55", "Ь":"56", "Э":"61", "Ю":"62", "Я":"63"}


# Code
def code(fraze):
    new_txt = ""
    list_fraze = list(fraze)
    for x in fraze:
        if x in hard_dictionary:
            new_txt += hard_dictionary.get(x)
        else:
            new_txt += (x + x)
    return new_txt

# Decode
# 63  3162123162  42161263 - test fraze
def decode(fraze):
    new_txt = ""
    list_fraze = []
    # str to list with letter length steep 
    step = 2
    for i in range(0, len(fraze), 2):
        list_fraze.append(fraze[i:step])
        step += 2
    # list to decode fraze
    key_hard_dictionary_list = list(hard_dictionary.keys())
    val_hard_dictionary_list = list(hard_dictionary.values())  

    for x in list_fraze:
        if x in val_hard_dictionary_list:
            i = val_hard_dictionary_list.index(x)
            new_txt += key_hard_dictionary_list[i]
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
    if "-c" in option:
        output_txt = code(fraze)    
    elif "-d" in option:
        output_txt = decode(fraze)
    else:
        print("Wrong key. See help")
        return 1
    print(output_txt, end='')

main()

