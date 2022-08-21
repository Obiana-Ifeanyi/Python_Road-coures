def witch_hunt(suspect_sets, innocent_sets):



    if len(suspect_sets) > 0 and len(innocent_sets) > 0:
        suspect_sets = can_read & talk_to_self & healers
        suspect_sets = set(suspect_sets)

        innocent_sets = wealthy | men
        innocent_sets = set(innocent_sets)
        witch_names = suspect_sets.difference(innocent_sets)
        return list(witch_names)

    elif len(suspect_sets) > 0 and len(innocent_sets) == 0:
        suspect_sets = can_read & talk_to_self & healers
        suspect_sets = set(suspect_sets)

        innocent_sets = []
        innocent_sets = set(innocent_sets)
        witch_names = suspect_sets.difference(innocent_sets)
        return list(witch_names)

    elif len(suspect_sets) == 0 and len(innocent_sets) > 0:
        suspect_sets = []
        suspect_sets = set(suspect_sets)

        innocent_sets = wealthy | men
        innocent_sets = set(innocent_sets)
        witch_names = suspect_sets.difference(innocent_sets)
        return []




can_read = {'Keeva', 'Daegal', 'Adam', 'Bellatrix', 'Ulrich', 'Keene', 'Evanora', 'Earthan', 'Paxton', 'Alice', 'Candice', 'Cedonia', 'Zelig', 'Lydia', 'Mortimer'}
talk_to_self = {'Candice', 'Lydia', 'Chilton', 'Alice', 'Cedonia', 'Minerva', 'Adam', 'Daegal', 'Camilla', 'Keene', 'Chalmers', 'Keeva', 'Paxton'}
healers = {'Bellatrix', 'Cullen', 'Adam', 'Alice', 'Lydia', 'Ulrich', 'Zelig', 'Cedonia', 'Paris', 'Chalmers', 'Chilton', 'Minerva', 'Paxton', 'Mortimer', 'Earthan', 'Daegal'}
wealthy = {'Chalmers', 'Keeva', 'Alice', 'Cullen', 'Minerva'}
men = {'Keene', 'Zelig', 'Mortimer', 'Adam', 'Ulrich', 'Chalmers', 'Paxton', 'Cullen', 'Chilton', 'Earthan', 'Daegal'}

suspect_sets = [can_read, talk_to_self, healers]
innocent_sets = [wealthy, men]

print (witch_hunt(suspect_sets, innocent_sets))

suspect_sets = [can_read, talk_to_self, healers]
innocent_sets = []

print (witch_hunt(suspect_sets, innocent_sets))

suspect_sets = []
innocent_sets = [wealthy, men]

print (witch_hunt(suspect_sets, innocent_sets))
