import logging
from generator import names, titles


tix = ['Tiny', 'Good-Enough', 'Thrice-Divorced', 'Not-so-Mighty',
 'Hungry', 'Puzzled', 'Never-There', 'Tall-One', 'Smart', 'Over-thinker',
 'Forgetful', 'Coward', 'Un-dead', 'Crafty', 'Lion-hearted', 'Insane', 'Powerful',
 'Butcher', 'Caring', 'Keeper', 'Rich', 'Wild', 'Vigilant', 'Reviled', 'Giant', 'Trusted']

name_list = ['Galahad', 'Lancelot', 'Gawain', 'Percivale', 'Lionell', 'Tristram de Lyones',
 'Gareth', 'Bedivere', 'Bleoberis', 'Lacotemale Taile', 'Lucan', 'Palomedes', 'Chizaram',
 'Lamorak', 'Bors de Ganis', 'Safer', 'Pelleas', 'Kay', 'Ector de Maris', 'Dagonet',
 'Degore', 'Brunor le Noir', 'Lebius Desconneu', 'Alymere', 'Muna', 'Mordred', 'Gris', 'Jeremy' ]



# USING logging(), f-str, names and titles function
"the format of the logs must be: '..::Knight Generator::.. [process]-[levelname][message]'"

# loogging configuration
logging.basicConfig(format='..::Knight Generator::.. %(process)d-%(levelname) s%(message)s', level=logging.INFO)

# calling the function from names.py and titles.py within the log function while using f-str
logging.info("-Package __init__ executed")
logging.info("-[Name chosen.]")
logging.info("-[Title chosen.]")
logging.info(f"-Sir {names(name_list)} the {titles(tix)}")
logging.info("-[Name chosen.]")
logging.info("-[Title chosen.]")
logging.info(f"-Sir {names(name_list)} the {titles(tix)}")
logging.info("-[Name chosen.]")
logging.info("-[Title chosen.]")
logging.info(f"-Sir {names(name_list)} the {titles(tix)}")
logging.info("-[Name chosen.]")
logging.info("-[Title chosen.]")
logging.info(f"-Sir {names(name_list)} the {titles(tix)}")
logging.info("-[Name chosen.]")
logging.info("-[Title chosen.]")
logging.info(f"-Sir {names(name_list)} the {titles(tix)}")



