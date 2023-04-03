# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 09:06:53 by phijano-          #+#    #+#              #
#    Updated: 2023/03/14 13:14:45 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_recipe_names():
   
    print("  " + "\n  ".join(x for x in cookbook.keys()))

def recipe_details(name):
   
    if cookbook.get(name):
        print("  Ingredients list: {}".format(cookbook.get(name).get(keys[0])))
        print("  To be eaten for {}".format(cookbook.get(name).get(keys[1])))
        print("  Takes {} minutes of cooking\n".format(cookbook.get(name).get(keys[2])))
    else:
        print("  recipe for " + name + " doesnt exist in cookbook\n")

def delete_recipe(name):
   
    if cookbook.get(name):
        del cookbook[name]
        print("  recipe for " + name + " eliminated\n")
    else:
        print("  recipe for " + name + " doesnt exist in cookbook\n")


def add_recipe():
    
    text_name = None
    while not text_name:
        text_name = input("Enter a name: ")
    text_ingredients = []
    text = None
    while not text_ingredients or text:
        text = input("Enter ingredients: ")
        if text:
            text_ingredients.append(text)
    text_type = None
    while not text_type:
        text_type = input("Enter a meal type: ")
    prep_time = None
    while not prep_time or not prep_time.isnumeric():
        prep_time = input("Enter a preparation time: ")
    recipe = {keys[0]:text_ingredients, keys[1]:text_type, keys[2]:prep_time}
    cookbook[text_name] = recipe

if __name__ == "__main__":
    ingredients = [["jamón", "pan", "queso", "tomate"], ["harina", "azucar", "huevos"], ["aguacate", "rúcula", "tomates", "espinacas"]]
    meal = ["almuerzo", "postre", "almuerzo"]
    prep_time = [10, 60, 15]
    names = ["bocadillo", "tarta", "ensalada"]
    keys = ["ingredients", "meal", "prep_time"]
    cookbook = {}
    index = range(3)
    for x in index:
        recipe = {keys[0]:ingredients[x], keys[1]:meal[x], keys[2]:prep_time[x]}
        cookbook[names[x]] = recipe
    print("Welcome to the Python Cookbook !\nList of available option:\n  1: Add a recipe\n  2: Delete a recipe")
    print("  3: Print a recipe\n  4: Print the cookbook\n  5: Quit\n")
    finish = None
    while not finish:
        option = None
        while not option or not option.isnumeric() or (option.isnumeric() and (int(option) < 1 or int(option) > 5)):
            option = input("Please select an option:\n>> ")
            if not option or not option.isnumeric() or (option.isnumeric() and (int(option) < 1 or int(option) > 5)):
                print("\nSorry, this option does not exist.\nList of available option:\n  1: Add a recipe\n  2: Delete a recipe")
                print("  3: Print a recipe\n  4: Print the cookbook\n  5: Quit")
            print("")
        if option == '1':
            add_recipe()
        elif option == '2':
            name = None
            while not name:
                name = input("Please enter a recipe name to delete:\n>> ")
                delete_recipe(name)
        elif option == '3':
            name = None
            while not name:
                name = input("Please enter a recipe name to get its details:\n>> ")
                recipe_details(name)
        elif option == '4':
            print_recipe_names()
        else:
            exit()
