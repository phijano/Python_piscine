# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 15:43:40 by phijano-          #+#    #+#              #
#    Updated: 2023/03/13 15:59:05 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
    print("operations.py numberA numberB")
elif len(sys.argv) == 3:
    try :
        number_a = int(sys.argv[1])
        number_b = int(sys.argv[2])
        print("Sum          " + str(number_a + number_b))
        print("Difference   " + str(number_a - number_b))
        print("Product      " + str(number_a * number_b))
        try :
            print("Quotient     " + str(number_a / number_b))
        except :
            print("Quotient     ERROR (division by zero)")
        try :
            print("Remainder    " + str(number_a % number_b))
        except :
            print("Remainder    ERRORi (modulo by zero)")
    except :
        print("AssertionError: only integers")
else :
    print("AssertionError: too many arguments")
