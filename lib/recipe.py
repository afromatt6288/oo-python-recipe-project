from .recipecard import RecipeCard
from .recipeingredient import RecipeIngredient
from .allergy import Allergy

class Recipe: #Build the following functionality on the Recipe class

    all = [] # DONE !should return all of the recipe instances

    def __init__(self, name):
        self.name = name
        self.users_list = []
        self.ingredients_list = []
        self.allergens_list = []
        Recipe.all.append(self)
        pass

    def users(self):
        self.users_list = []
        for recipecard in RecipeCard.all:
            if self.name == recipecard.recipe.name:
                self.users_list.append(recipecard.user)
        return self.users_list
        # DONE? should return the user instances who have recipe cards with this recipe
        pass
    
    def ingredients(self):
        self.ingredients_list = []
        for recipeingredient in RecipeIngredients.all:
            if self.name == recipeingredient.recipe.name:
                self.ingredients_list.append(recipeingredient.ingredient)
        # DONE? should return all of the ingredients in this recipe
        pass

    def allergens(self):
        self.ingredients_list = []
        self.ingredients()
        self.allergens_list = []
        for ingredient in ingredients_list:
            if ingredient in Allergy.all:
                self.allergens_list.append(ingredient)
        return self.allergens_list
        # DONE? should return all of the `Ingredient`s in this recipe that are allergens for `User`s in our system.
        pass

    def add_ingredients(self, new_ingredient):
        new_ingredient = RecipeIngredient(new_ingredient, self)
        # Done? should take an list of ingredient instances as an argument, and associate each of those ingredients with this recipe

    @classmethod
    def most_popular(cls):
        for recipecard in RecipeCard.all:
            # grab number of users for each card. Sort by most number of users (TBD):
                # return recipecard with most users
        # should return the recipe instance with the highest number of users (the recipe that has the most recipe cards)
        pass
    
