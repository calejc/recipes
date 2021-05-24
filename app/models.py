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
        self.ingredients = None # Set later after sending ingredient strings through the parser
        self.title = schema['name'] if 'name' in schema else ''
        self.description = schema['description'] if 'description' in schema else '' 
        self.photoUrl = schema['image'][0] if 'image' in schema else ''
        self.totalTime = schema['totalTime'] if 'totalTime' in schema else ''
        self.cookTime = schema['cookTime'] if 'cookTime' in schema else ''
        self.prepTime = schema['prepTime'] if 'prepTime' in schema else ''
        self.servings = schema['recipeYield'] if 'recipeYield' in schema else ''
        self.instructions = [Instruction(i, c).__dict__ for i, c in enumerate(schema['recipeInstructions'])]  if 'recipeInstructions' in schema else []
        self.fullStringIngredients = [s for s in schema['recipeIngredient']] if 'recipeIngredient' in schema else []

        categories = [Category(c).__dict__ for c in schema['recipeCategory']]
        cuisines = [Category(c).__dict__ for c in schema['recipeCuisine']] if 'recipeCuisine' in schema else []
        self.categories = categories + cuisines


class Ingredient:
    """
    Ingredient entity 
    """
    def __init__(self, schema):
        self.full = schema['input']
        self.content = schema['name'] if 'name' in schema else ''
        self.quantity = schema['qty'] if 'qty' in schema else schema['other'] if 'other' in schema else ''
        self.measure = schema['unit'] if 'unit' in schema else ''


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

