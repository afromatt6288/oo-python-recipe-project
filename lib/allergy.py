class Allergy: # An Allergy is a join between a user and an ingredient.  This is a has-many-through relationship.  What functionality should an instance of this model respond to?

    all = [] # DONE! should return all of the Allergy instances

    def __init__(self, user, ingredient):
        self.user = user
        self.ingredient = ingredient
        Allergy.all.append(self)

    pass