# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 13:19:11 by phijano-          #+#    #+#              #
#    Updated: 2023/03/13 16:35:09 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(text = None):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if text == None:
        text = input("Introduce texto:")
    if type(text) == str:
        u_letters = 0
        l_letters = 0
        punct = 0
        spaces = 0
        for letra in text:
            if letra.isupper():
                u_letters += 1
            elif letra.islower():
                l_letters +=1
            elif letra.isspace():
                spaces +=1
            elif letra in string.punctuation:
                punct +=1
        print("The text contains " + str(len(text)) + " character(s):")
        print("- " + str(u_letters)  + " upper letter(s)")
        print("- " + str(l_letters)  + " lower letter(s)")
        print("- " + str(punct)  + " punctuation mark(s)")
        print("- " + str(spaces)  + " space(s)")
    else :
        print("AssertionError: argument is not a string")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: too many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else :
        text_analyzer()
