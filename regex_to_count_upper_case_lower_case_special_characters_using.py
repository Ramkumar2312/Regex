import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyzwhfuehrgoehgoeghghhepghperihp ##^&&&@@@^^&*&*
ABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&* !@#$%^&#* 1221424825305305703$75305730403757393503580257 '''

#to count upper case lower case special characters and numeric values in a string

def character_count(text):
    upper_case_list = []
    lower_case_list = []
    special_characters_list = []
    numeric_values_list = []

    upper_case_pattern = re.compile(r'[A-Z]')

    lower_case_pattern = re.compile(r'[a-z]')

    special_characters_pattern = re.compile(r'(!|@|#|\$|%|\^|&|\*)')

    numeric_values_pattern = re.compile(r'\d')



    for texts in text:
        u_text = upper_case_pattern.match(str(texts))
        if u_text :
            upper_case_list.append(texts)

        l_text = lower_case_pattern.match(str(texts))
        if l_text :
            lower_case_list.append(l_text)

        special_text = special_characters_pattern.match(str(texts))
        if special_text:
            special_characters_list.append(texts)

        num_text = numeric_values_pattern.match(str(texts))
        if num_text:
            numeric_values_list.append(texts)

    print(f'Number of Uppercase Characters :{len(upper_case_list)}')
    print(f'Number of Lowercase Characters :{len(lower_case_list)}')
    print(f'Number of Specialcase Characters :{len(special_characters_list)}')
    print(f'Number of Numericcase Characters :{len(numeric_values_list)}')

character_count(text_to_search)
