from webcrawler import get_ingredient_lists


class RecipeNode:
    def __init__(self, name, ingrediens, url):
        self.name = name
        self.ingredients = ingrediens
        self.url = ""

    def __str__(self):
        return f"{self.name} recipe"
    
    def __repr__(self):
        return f"{self.name}"

class QuestionNode:
    def __init__(self, question, ingredient):
        self.question = question #Do you want meat? 
        self.ingredient = ingredient #Meat
        self.recipe_with_ingredient = []
        self.recipe_without_ingredient = []
        self.yes_node = None
        self.no_node = None

    def __str__(self):
        return f"{self.ingredient} question_node"


    def ingredient_in_recipe(self, ingredient, recipe_node):
        if ingredient in recipe_node.ingrediens:
            return True
        return False
    
    def add_recipe(self, recipe_node, question_node):

        #Check if we reached bottom
        if question_node is None:
            print("Successfully added recipe")
            return

        current_node = question_node
        # If ingredient in recipe go left and add recipe to questionnode
        if self.ingredient_in_recipe(current_node.ingredient, recipe_node):
            #Ingredient in recipe, so add it to the children list and get next node
            print(f"Adding {recipe_node} to {current_node}")
            current_node.recipe_with_ingredient.append(recipe_node)
            self.add_recipe(recipe_node, self.yes_node)
                        
        else:
            self.add_recipe(self.no_node, recipe_node)

    def traverse_tree_and_add_question(self, root, question_node):
        current_node = root
        queue = [current_node]

        while queue:
            current_node = queue.pop(0)
            if current_node.yes_node is not None and current_node.no_node != question_node:
                queue.append(current_node.yes_node)
            else:
                print(f"Adding {question_node} to {current_node} as yes_node")
                current_node.yes_node = question_node
            if current_node.no_node is not None and current_node.no_node != question_node:
                queue.append(current_node.no_node)
            else:
                print(f"Adding {question_node} to {current_node} as no_node")
                current_node.no_node = question_node
            
        return "Done"
    
    def traverse_tree_and_add_recipe(self, root, recipe_node):
        current_node = root
        queue = [current_node]

        while queue:
            current_node = queue.pop(0)
            if current_node.ingredient in recipe_node.ingredients:
                print(f"Adding {recipe_node} to the includes {current_node} ")
                current_node.recipe_with_ingredient.append(recipe_node)
                # then 
                if current_node.yes_node is not None:
                    queue.append(current_node.yes_node)
            else:
                print(f"Adding {recipe_node} to the does not include {current_node} ")
                current_node.recipe_without_ingredient.append(recipe_node)
                if current_node.no_node is not None:
                    queue.append(current_node.no_node)
        
        return "Done"



