from datetime import datetime

birthday = datetime(1986, 6, 26)
today = datetime.now()
age = today.year - birthday.year
print(age)