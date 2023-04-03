# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 16:06:12 by phijano-          #+#    #+#              #
#    Updated: 2023/03/14 17:54:07 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import sys
from time import sleep
from time import time

def ft_progress(lst):
    '''
    This function show the progress of a for loop
    '''
    start_time = 0
    loop_time = 0
    start_time = time()
    for i, x in enumerate(lst):
        i +=1
        sys.stdout.write("\033[K")
#        print(" ", end='\r')
        print("ETA: {:.2f}".format(((time() - start_time) / i) * (len(lst) - i)) + " "  + str(int(i/len(lst) * 100)) + "%   "\
            + str(i) + "/" + str(len(lst)), end='\r')
        yield x

if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret+=(elem+3) %5
        sleep(0.01)
    print()
    print(ret)
