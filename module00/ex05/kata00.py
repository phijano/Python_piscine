# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/13 16:00:48 by phijano-          #+#    #+#              #
#    Updated: 2023/03/13 17:37:40 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata00.py file
kata = (19,42,21)

print("The " + str(len(kata)) + " numbers are: " + ', '.join(str(x) for x in kata))
