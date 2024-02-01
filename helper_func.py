from webcrawler import get_ingredient_lists
from treenode import QuestionNode, RecipeNode


def give_recommendations(question_root):
    current_node = question_root
    queue = [current_node]

    yes_ingredients = ""
    no_ingredients = ""


    while queue:
        current_node = queue.pop(0)

        yes_no = input(f"Do you want {current_node.ingredient} in your food? y/n? ")
        while yes_no != "n" and yes_no != "y":
            print("Wrong entry. Try again")
            yes_no = input(f"Do you want {current_node.ingredient} in your food? y/n? ")

        #Hvis person ønsker ingrediensen
        if yes_no == "y":
            yes_ingredients += current_node.ingredient + ", "
            print(f"Recipes with {yes_ingredients} and without {no_ingredients}:")
            for recipe in current_node.recipe_with_ingredient:
                print(recipe.name + "\n")
            
            #Hvis personen ønsker at få en af opskrifterne
            stick_with_a_recipe = input("Do you want to stick with a recipe? ")
            while stick_with_a_recipe != "n" and yes_no != "y":
                print("Wrong entry. Try again")
                stick_with_a_recipe = input("Do you want to stick with a recipe? ")

            if stick_with_a_recipe == "y":
                chosen_recipe = input("Which one? Write the exact text: ")
                chosen_recipe_node = None
                print(current_node.recipe_with_ingredient)
                while True:
                    found = False
                    for index, recipe in enumerate(current_node.recipe_with_ingredient):
                        if recipe.name == chosen_recipe:
                            found = True
                            chosen_recipe_index = index
                    if found:
                        break
                    chosen_recipe = input("Which one? Write the exact text: ")

                print(f"You have chosen {chosen_recipe}")
                print(current_node.recipe_with_ingredient[chosen_recipe_index])
                for ingredient in current_node.recipe_with_ingredient[chosen_recipe_index].ingredients:
                    print(ingredient)
                print(current_node.recipe_with_ingredient[chosen_recipe_index].url)

            else:
                queue.append(current_node.yes_node)
        else:
            no_ingredients += current_node.ingredient + ", "
            print(f"Recipes without {no_ingredients} and with {yes_ingredients}:")
            for recipe in current_node.recipe_without_ingredient:
                print(recipe.name + "\n")
            
            #Hvis personen ønsker at få en af opskrifterne
            stick_with_a_recipe = input("Do you want to stick with a recipe? ")
            while stick_with_a_recipe != "n" and yes_no != "y":
                print("Wrong entry. Try again")
                stick_with_a_recipe = input("Do you want to stick with a recipe? ")

            if stick_with_a_recipe == "y":
                chosen_recipe = input("Which one? Write the exact text: ")
                chosen_recipe_node = None
                print(current_node.recipe_without_ingredient)
                while True:
                    found = False
                    for index, recipe in enumerate(current_node.recipe_without_ingredient):
                        if recipe.name == chosen_recipe:
                            found = True
                            chosen_recipe_index = index
                    if found:
                        break
                    chosen_recipe = input("Which one? Write the exact text: ")

                print(f"You have chosen {chosen_recipe}")
                print(current_node.recipe_without_ingredient[chosen_recipe_index])
                for ingredient in current_node.recipe_without_ingredient[chosen_recipe_index].ingredients:
                    print(ingredient)
                print(current_node.recipe_without_ingredient[chosen_recipe_index].url)

            else:
                queue.append(current_node.no_node)

            



root_løg = QuestionNode("Løg?", "løg")
kartofler = QuestionNode("Kartofler?", "kartofler")
chili = QuestionNode("Chili?", "chili")
kikærter = QuestionNode("Kikærter?", "kikærter")
linser = QuestionNode("Linser?", "linser")
kokosmælk = QuestionNode("Kokosmælk?", "kokosmælk")
nødder = QuestionNode("Nødder?", "nødder")
ris = QuestionNode("Ris?", "ris")
tomater = QuestionNode("Tomater?", "tomater")
blomkål = QuestionNode("Blomkål?", "blomkål")
æg = QuestionNode("Æg?", "Æg")
aubeginer = QuestionNode("Auberginer?", "Auberginer")
bønner = QuestionNode("Bønner?", "bønner")

root_løg.traverse_tree_and_add_question(root_løg, kartofler)
root_løg.traverse_tree_and_add_question(root_løg, chili)
root_løg.traverse_tree_and_add_question(root_løg, kikærter)
root_løg.traverse_tree_and_add_question(root_løg, linser)
root_løg.traverse_tree_and_add_question(root_løg, kokosmælk)
root_løg.traverse_tree_and_add_question(root_løg, nødder)
root_løg.traverse_tree_and_add_question(root_løg, ris)
root_løg.traverse_tree_and_add_question(root_løg, tomater)
root_løg.traverse_tree_and_add_question(root_løg, blomkål)
root_løg.traverse_tree_and_add_question(root_løg, æg)
root_løg.traverse_tree_and_add_question(root_løg, aubeginer)
root_løg.traverse_tree_and_add_question(root_løg, bønner)

kødboller = RecipeNode("kødboller", {"løg", "chili", "kartofler"}, "fjkdlsfjksd")

root_løg.traverse_tree_and_add_recipe(root_løg, kødboller)


recipes = get_ingredient_lists('https://spisbedre.dk/temaer/vegetariske-gryderetter')
recipe_list = []

for name, ingredient_and_url in recipes.items():
    name = RecipeNode(name, ingredient_and_url[0], ingredient_and_url[1])
    recipe_list.append(name)

for recipe in recipe_list:
    root_løg.traverse_tree_and_add_recipe(root_løg, recipe)

give_recommendations(root_løg)


