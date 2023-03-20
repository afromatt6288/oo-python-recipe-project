from .allergy import Allergy
from .recipecard import RecipeCard

class User: # Build the following functionality on the User class

    all = [] # DONE! should return all of the user instances

    def __init__(self, name):
        self.name = name
        self.recipes = []
        self.alergic_to = []
        User.all.append(self)
    pass

    def recipes(self):
        recipes = []

        # should return all of the recipes this user has recipe cards for
        pass
    
    def add_recipe_card(self, recipe, date, rating):
        recipe_card = RecipeCard(recipe, date, self, rating)
        # DONE? should accept a recipe instance as an argument, as well as a date and rating, and create a new recipe card for this user and the given recipe
        pass
    
    def declare_allergy(self, ingredient):
        newallergy = Allergy(self, ingredient)
        self.allergic_to.append(ingredient)
        # DONE? should accept an `Ingredient` instance as an argument, and create a new `Allergy` instance for this `User` and the given `Ingredient`
        pass
    
    def allergens(self):
        allergic_to = []
        for allergy in Allergy.all:
            if user == allergy.user:
                allergic_to.append(allergy.ingredient)
        # DONE ? should return all of the ingredients this user is allergic to
        pass
    
    def top_three_recipes(self):
        recipecard_list = []
        top_three = []
        for recipecard in RecipeCard.all:
            if recipecard.user = self:
                recipecard_list.append(recipecard)
        # sort(recipecard_list) by rating: (not sure how to do this... but will look later)
            top_three.append(recipe[0], recipe[1], recipe[2])
        return top_three            
        #should return the top three highest rated recipes for this user.
        pass
    
    def most_recent_recipe(self):
        recipecard_list = []
        for recipecard in RecipeCard.all:
            if recipecard.user = self:
                recipecard_list.append(recipecard)
        # sort(recipecard_list) by date: (not sure how to do this... but will look later)
        return recipe_card_list[0]     
        # should return the recipe most recently added to the user's cookbook.
        pass
    
    def safe_recipes(self):
        recipecard_list = []
        for recipecard in RecipeCard.all:
            if recipecard.user = self:
                recipecard_list.append(recipecard)
        # should return all recipes that do not contain ingredients the user is allergic to
        pass

