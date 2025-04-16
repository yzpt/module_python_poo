# Calculer l'âge d'une personne à partir de sa date de naissance au jour d'aujourd'hui

from datetime import datetime

birthday = datetime(1986, 6, 26)
today = datetime.now()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) # on enlève un an si l'anniversaire n'est pas encore passé cette année
print(age)