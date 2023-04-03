# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 11:31:32 by phijano-          #+#    #+#              #
#    Updated: 2023/03/13 12:26:20 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

string = ""
del sys.argv[0]
for x in sys.argv:
    string += " " + x
string = string.swapcase()
string = string[:0:-1]
print(string)
