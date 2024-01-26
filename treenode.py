class RecipeNode:
    def __init__(self, name, ingrediens):
        self.name = name
        self.ingrediens = ingrediens

class QuestionNode:
    def __init__(self, question, ingredient):
        self.question = question
        self.ingredient = ingredient
        self.children = []
        self.recipes = []

    def add_child_question(self, child_node):
        self.children.append(child_node)

    def get_children_with_ingredient(self, ingredient):
        children = []
        
    
    def add_recipe(self, recipenode, questionroot):
        current_node = root
        nodes_to_visit = []
        while nodes_to_visit:
            y_n = input(current_node.question)
            if y_n:
                pass
                



    


root = QuestionNode("Kjøt?", "kjøt")

