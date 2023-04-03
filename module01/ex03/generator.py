# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 15:54:15 by phijano-          #+#    #+#              #
#    Updated: 2023/03/17 09:17:19 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
    '''
    Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
    option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    '''
    if not isinstance(text, str) or option != None and option not in ("shuffle", "unique", "ordered"):
        return (["ERROR"])
    elif option == "shuffle":
        pack = text.split(sep)
        for x in range(len(pack)):
            old = random.choice(pack)
            pack.remove(old) 
            yield old
    elif option == "unique":
        pack = text.split(sep)
        pack2 = []
        for x in pack:
            if x not in pack2:
                pack2.append(x)
                yield x
    elif option == "ordered":
        pack = text.split(sep)
        pack.sort()
        for index in range(len(pack)):
            yield pack[index]
    else:
        pack = text.split()
        for index in range(len(pack)):
            yield pack[index]      

text = "a b c d e f f g"

a = "shuffle"
b = "unique"
c = "ordered"
d = "sdfsfd"

for word in generator(text, sep=" ", option="shuffle"):
    print(word)

for word in generator(text, sep=" ", option="unique"):
    print(word)

for word in generator(text, sep=" ", option="ordered"):
    print(word)


