from recipeingredient import RecipeIngredient
from .allergy import Allergy

class Ingredient: # Build the following functionality on the Ingredient class

    all = [] # DONE! should return all of the ingredient instances

    def __init__(self, name):
        self.name = name
        Ingredient.all.append(self)
    pass

    @classmethod
    def most_common_allergen(cls):
        for allergy in Allergy.all:
            # sort by ingredient, and return the highest one...
        # should return the ingredient instance that the highest number of users are allergic to
        pass
