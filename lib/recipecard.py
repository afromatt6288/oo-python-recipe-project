class RecipeCard: # A RecipeCard is the join between a user instance and a recipe instance.  This is a has-many-through relationship. Build the following functionality on the RecipeCard class:  

    all = [] # DONE! should return all of the RecipeCard instances

    def __init__(self, user, recipe, date, rating):
        self.recipe = recipe # Done? should return the recipe to which the entry belongs
        self.date = date # Done? should return the date of the entry
        self.user = user # Done? should return the user to which the entry belongs
        self.rating = rating # Done? should return the rating (an integer) a user has given their entry
        RecipeCard.all.append(self)
        pass

