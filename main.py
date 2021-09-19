from alfavit import MORSE_CODE_DICT

# 'cipher' -> 'stores the morse translated form of the english string'
# 'decipher' -> 'stores the english translated form of the morse string'
# 'morse_code_of_a_single_character' -> 'stores morse code of a single character'
# 'i' -> 'keeps count of the spaces between morse characters'

# 1.Переводим key и value в list[]
MORSE_CODE_DICT_KEYS = list(MORSE_CODE_DICT.keys())
MORSE_CODE_DICT_VALUES = list(MORSE_CODE_DICT.values())


def encrypt(main_text):
    """Function to encrypt the string according to the morse code chart"""
    cipher = ''
    for letter in main_text:
        if letter != ' ':
            # Looks up the dictionary and adds the corresponding morse code along with a space to separate morse
            # codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters and 2 indicates different words
            cipher += ' '
    return cipher


def decrypt(main_text):
    """Function to decrypt the string from morse to english"""
    # extra space added at the end to access the last morse code
    main_text += ' '

    decipher = ''
    morse_code_of_a_single_character = ''
    for letter in main_text:
        # checks for space
        if letter != ' ':
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            morse_code_of_a_single_character += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1   #каждую последующую букву в decipher i так и буден постоянно равен 1,
                     #оэтому если letter сразу будет равно ' ' , то i += 1 (i = 2), а значит decipher += ' ' , т.е. начинается новое слово

            # if i = 2 that indicates a new word (2 пробела между словами)
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += MORSE_CODE_DICT_KEYS[MORSE_CODE_DICT_VALUES.index(morse_code_of_a_single_character)]
                # ['A', 'B', 'C', ...]['.-', '-...', '-.-.', ...   .index('-.-.')]
                # ['A', 'B', 'C', ...][2]   ->   'C'
                morse_code_of_a_single_character = ''  # заново задаем пустой str для morse_code_of_a_single_character,
    return decipher                                    # чтобы потом добавлять по одной точке или тире


should_continue = True

while should_continue:
    direction = input('Выберите:"зашифровать" или "расшифровать" текст: \n')
    text = input("\nВведите текст:\n")
    if direction == 'зашифровать':
        result = encrypt(text.upper())
        print(result)
    else:
        result = decrypt(text.upper())
        print(result)

    question = input('Хотите повторить? "да" или "нет" ')
    if question == "нет":
        should_continue = False
        print("Пока!")