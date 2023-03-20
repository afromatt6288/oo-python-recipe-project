class RecipeIngredient: # RecipeIngredient is the join between an ingredient and a recipe.  This is a has-many-through relationship. Build the following functionality on the RecipeIngredient class

    all = [] # DONE! should return all of the RecipeIngredient instances

    def __init__(self, ingredient, recipe):
        self.ingredient = ingredient  # DONE? should return the ingredient instance
        self.recipe = recipe # DONE? should return the recipe instance
        RecipeIngredient.all.append(self)