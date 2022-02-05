# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


def get_age(birth_year):
    return 2022 - birth_year


user_name = input('Please enter your username: ')
save_into_db(user_name)

birth_year = int(input('Please enter your birth year: '))
age = get_age(birth_year)
print("You are", age, "years old.")
