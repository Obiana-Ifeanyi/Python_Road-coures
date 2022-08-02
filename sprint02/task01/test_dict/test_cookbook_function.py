# DESCRIPTION:
# Create a script with a function search_cookbook(), which takes in three arguments: cookbook, recipe, and section, the cookbook is a dict of dicts.
# The function looks for an item in the cookbook dict with recipe as the key.
# If found, it then looks for an item in the recipe dict with section as the key.
# On success, the function returns the found item.
# If there is no recipe in the cookbook, the function returns the string: 'There is no "[recipe]" recipe in the cookbook.'
# If there is no item with section key in the recipe, the function returns the string: 'There is no section "[section]" in the "[recipe]" recipe.'

##############
# NOTE: The function must use the method get().

def search_cookbook(cookbook, recipe, section):

    if recipe in cookbook.keys():
        if f"{section}" in section:
            return cookbook[f"{recipe}"].get(f"{section}", f'There is no section "{section}" in the "{recipe}" recipe.')


    elif recipe not in cookbook.keys():
        return f'There is no "{recipe}" recipe in the cookbook.'





# Note: using this function with the script in this folder returns 'None' when the script executes the code below.

# cookbook = {15: {('1', '0'): 'ten', 'a': 'something'}}
    #test_cookbook(cookbook, 15, ('1', '0'))
