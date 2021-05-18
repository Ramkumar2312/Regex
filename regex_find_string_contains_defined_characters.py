import re



User_input=input('Enter a string :')

""" string should Start with a Capital letter and should end with any of the special characters !@#$%^&* """

def defined_character_match(string_to_match):

    pattern = re.compile(r'([A-Z]\w+(!|@|#|\$|%|\^|&|\*))')
    return_value = pattern.match(str(string_to_match))
    if return_value :
        print(f"Valid string,{return_value}")
    else :
        print(f"InValid string,{return_value}")

defined_character_match(User_input)