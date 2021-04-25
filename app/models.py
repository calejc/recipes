#


class Schema:
    """
    Find the schema object containing the recipe information from various 'Recipe' schema structures (https://schema.org/Recipe).
    
    """
    def __init__(self, contents):
        self.target_schema = None
        self.parse(contents)

    def parse(self, obj):
        if isinstance(obj, dict):
            if '@type' in obj and 'Recipe' == obj['@type']:
                self.target_schema = obj
            else:
                for v in obj.values():
                    self.parse(v)
        elif isinstance(obj, list):
            for i in obj:
                self.parse(i)

class Recipe:
    def __init__(self, schema):
        self.title = schema['name']
        self.description = schema['description']
        self.totalTime = schema['totalTime'] if 'totalTime' in schema else ''
        self.cookTime = schema['cookTime'] if 'cookTime' in schema else ''
        self.prepTime = schema['prepTime'] if 'prepTime' in schema else ''
        self.servings = schema['recipeYield'] if 'recipeYield' in schema else ''
        self.ingredients = [Ingredient(s).__dict__ for s in schema['recipeIngredient']]
        self.instructions = [Instruction(i, c).__dict__ for i, c in enumerate(schema['recipeInstructions'])]

        categories = [Category(c).__dict__ for c in schema['recipeCategory']]
        cuisines = [Category(c).__dict__ for c in schema['recipeCuisine'] if 'recipeCuisine' in schema]
        self.categories = categories + cuisines


class Ingredient:
    """
    Ingredient entity 
    """
    def __init__(self, schema):
        self.name = schema


class Instruction:
    """
    Instruction Entity
    """
    def __init__(self, counter, schema):
        self.order = counter
        self.schema = schema


class Category:
    def __init__(self, name):
        self.name = name

