# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 10:03:34 by phijano-          #+#    #+#              #
#    Updated: 2023/03/16 09:27:25 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
    
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not bool(name):
            raise ValueError("name cant be empty")
        if not (isinstance(cooking_lvl,int) and (cooking_lvl > 0 and cooking_lvl < 6 )):
            raise ValueError("cooking level must be an int from 1 to 5")      
        if not (isinstance(cooking_time, int) and cooking_time > 0):
            raise ValueError("cooking_time must be a positive int")
        if not (bool(ingredients) and all(isinstance(n, str) for n in ingredients)):
            raise ValueError("ingredients is expected to be a list of strings")
        if  bool(description) and not isinstance(description, str):
            raise ValueError("description is expected to be a string")
        if not (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
            raise ValueError("recipe is expected to be \"entrante\", \"comida\" o \"postre\"")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = self.name + " " + str(self.cooking_lvl) + " " + str(self.cooking_time) + " " + " ".join(self.ingredients) + " " + self.description + " " + self.recipe_type
        """Your code here"""
        return txt
