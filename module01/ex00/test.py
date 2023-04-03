# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: phijano- <phijano-@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 13:02:17 by phijano-          #+#    #+#              #
#    Updated: 2023/03/16 09:44:27 by phijano-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book

tarta = Recipe("tarta", 4, 3, ["chocolate", "cerezas", "alcohol 100%"], "", "dessert")
print(tarta)
book = Book("cocinillas")
book.add_recipe(tarta)
book.get_recipe_by_name("tarta")
print(str(book))

