def contacts(container, info, operation):
    import re

    # container_arg = {}
    # info_arg = {'name': '\w\s', 'email': '[A-Za-z]@[A-Za-z].[A-Za-z]'}
    #  operation must be 'add', 'update', or 'delete'


    # note [A-Za-z] for this task reprsent [not '@']
    # i.e [not `@`]@[not `@`].[not `@`] = '[A-Za-z]@[A-Za-z].[A-Za-z]'


    #  operation must be 'add', 'update', or 'delete'
    if operation == 'add':

        if info['email'] in container:
            # if the container dict already has an item with such key, it gets overwritten

            # variable that stores the value of the key 'email' in info
            key = info['email']

            # del the key in the container that is the same for the value of the 'email' key in info
            del container[info['email']]

            # using pop remove the item 'email and its value while retaining other keys and value in the info dict
            info.pop('email')

            # using the created varible above
            # create a key in the container that is same for the value of the key 'email' deleted above
            container[key] = info

            return container



        elif info['email'] not in container:

            # variable that holds the value of 'email' in the info dictionary
            newkey = info['email']

            # del the 'email' item
            del info['email']

            # the key of the newly created item is the value of 'email' in the info dic
            container[newkey] = info
            return container


    elif operation == 'update':

        # iterate through everykey in container thats is equal to the value of key 'email' in info dict
        for key in container.keys():

            # updates the found contact (the element in the container with key equal to the email value in the info)
            # returns False. if no key is equal to the email value in the info dictionary
            if key == info['email']:

                # don't add the 'email' item in the info, there we are going to del the email item before updating
                info.pop('email')

                # update dictionary using the update() fn
                # dict1.update(dict2)
                # Note: update to key in container and not to the container its self
                container[key].update(info)
                return container
                break


            else:
                return False


    elif operation == 'del':

        for key in container.keys():

            if key == info['email']:
                # dict.pop(key, none)
                container.pop(key, 'No key found')
                return container
                break

            else:
                return False


    # returns False if either the info or the operation is not valid
    else:
        return False


container = {'a@a.a': {'name': 'a', 'age': 25}, 'b@b.b': {'name': 'b', 'age': 37}}
#container = {}
info = {'email': 'a@a.a', 'name': 'x', 'id': '5'}
operation = 'del'


print (contacts(container, info, operation))







# note: in over add operation where we had to overwrite the key.
# due to deleting and creating of our key it changes the index sequence of our dictionary
