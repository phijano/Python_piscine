# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:16:13 by phijano-          #+#    #+#              #
#    Updated: 2023/03/14 14:16:16 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) == 3 and sys.argv[2].isnumeric():
    text_input = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    list_output = [x for x in text_input.split(' ') if len(x) >= int(sys.argv[2])]
    print(list_output)
else:
    print("ERROR")
