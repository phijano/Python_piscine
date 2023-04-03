# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 09:17:53 by phijano-          #+#    #+#              #
#    Updated: 2023/03/17 09:55:52 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator():

    def zip_evaluate(words, coefs):
        if isinstance(words, list) and isinstance(coefs, list) and len(words) == len(coefs):
            result = zip(words, coefs)
            length = 0
            for x in list(result):
                length = length + len(x[0]) * x[1]
            return length
        else:
            return -1
            
        print(list(result))

    def enumerate_evaluate(words, coefs):
        if isinstance(words, list) and isinstance(coefs, list) and len(words) == len(coefs):
            words = enumerate(words)
            length = 0
            for x in list(words):
                length = length + len(x[1]) * coefs[x[0]]
            return length
        else:
            return -1


print(str(Evaluator.zip_evaluate(["aaa", "ss", "ccc"], [0.5, 1, 1])))
print(str(Evaluator.enumerate_evaluate(["aaa", "ss", "ccc"], [0.5, 1, 1])))
