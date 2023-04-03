# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 12:12:34 by phijano-          #+#    #+#              #
#    Updated: 2023/03/13 13:10:16 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print("whois.py number")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
else :
    try:
        number = int(sys.argv[1])
        if number == 0:
            print("I'm Zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
