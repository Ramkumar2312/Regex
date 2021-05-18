import re

text_to_search = ''' 12214248253053057037535730403757393503580257 akjagerg 1220343242 q20508450q284 '''

number_pattern = re.compile(r'(\d)')

def most_occuring_number(user_string):

    number_list = []

    count = 0
    max_count = 0
    most_occured = []

    num_dict = {}

    for strings in user_string:

        num_value = number_pattern.match(strings)
        if num_value:
            number_list.append(num_value.group())

    for num in number_list:
        num_dict.setdefault(num,0)
    for num in number_list:
        num_dict[num] += 1

    print(number_list)
    print(num_dict)

    most_common_number = sorted(num_dict, key=num_dict.get, reverse=True)
    print(most_common_number)

    #for num in number_list :
most_occuring_number(text_to_search)

