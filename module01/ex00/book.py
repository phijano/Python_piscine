# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:54:44 by phijano-          #+#    #+#              #
#    Updated: 2023/03/16 10:00:22 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

class Book:

    def __init__(self, name:str):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter":{}, "lunch":{}, "dessert":{}}
        if not bool(name):
            raise ValueError("name cant be empty")

        """Your code here"""
        return txt

    def get_recipe_by_name(self, name):
        """Imprime la receta con el nombre \texttt{name} y devolver la instancia"""
        for x in self.recipes_list.keys():
            recipe = self.recipes_list.get(x).get(name)
            if  recipe != None:
                print(str(recipe))
                return recipe
        return None
    def get_recipes_by_types(self, recipe_type):
        """Devuelve todas las recetas dado un recipe_type """
        return self.recipe_list.get(recipe_type).values

    def add_recipe(self, recipe):
        """Añade una receta al libro y actualiza last_update"""
        self.recipes_list.get(recipe.recipe_type).update({recipe.name:recipe})
        self.last_update = datetime.now()
