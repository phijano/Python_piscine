# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 10:35:19 by phijano-          #+#    #+#              #
#    Updated: 2023/03/16 14:57:59 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector():

        def __init__(self, vector):
            self.values = []
            if isinstance(vector, int):
                for i in range(vector):
                    self.values.append([float(i)])
                self.shape = (vector, 1)
            elif isinstance(vector, tuple):
                if vector[0] < vector[1]:
                    for i in range(vector[0], vector[1]):
                        self.values.append([float(i)])
                    self.shape = (vector[1] - vector[0], 1)
                else :
                    raise ValueError("Range error: " + str(vector[0]) + " >= " + str(vector[1]) + ". Expected value_1 < value_2 ")
            elif isinstance(vector, list):
                if all(isinstance(x, list) and len(x) == 1 and isinstance(x[0], float) for x in vector):
                    self.values = vector
                    self.shape = (1, len(vector))
                elif all(isinstance(x, float) for x in vector):
                    self.values.append(vector)
                    self.shape = (len(vector), 1)
            else:
                print("Vector ERROR")
        
        def dot(self, vector):
            result = 0
            if self.vector_row(vector.values):
                if self.shape[0] == vector.shape[0] and self.shape[1] == vector.shape[1]:
                    for i in range(len(self.values[0])):
                        result = result + self.values[0][i] * vector.values[0][i]
                    return result
                else:
                    raise ValueError("Vectors dont have same shape")
            elif self.vector_col(vector.values):
                if self.shape[0] == vector.shape[0] and self.shape[1] == vector.shape[1]:
                    for i in range(len(self.values)):
                        result = result + self.values[i][0] * vector.values[i][0]
                    return result
                else:
                    raise ValueError("Vectors dont have same shape")
            else:
                raise ValueError("Error")


        def T(self):
            temp = []
            if self.vector_row(self.values):
                for x in self.values[0]:
                    temp.append([x])
                self.value = temp
            elif self.vector_col(self.values):
                for x in self.values:
                    temp.append(x[0])
                self.value = temp
            else:
                raise ValueError("Error")
            self.shape = (self.shape[1], self.shape[0])
        
        @staticmethod
        def vector_row(vector):
            if isinstance(vector, list) and len(vector) == 1 and isinstance(vector[0], list) and all(isinstance(x, float) for x in vector[0]):
                return True
            else:
                return False

        @staticmethod
        def vector_col(vector):
            if isinstance(vector, list) and all(isinstance(x, list) and len(x) == 1 and isinstance(x[0], float) for x in vector):
                return True
            else:
                return False


