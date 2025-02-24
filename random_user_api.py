from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_users = RandomUser.generate_users(10)

name = r.get_full_name()
for user in some_users:
    print(user.get_full_name(), user.get_email())

# generating protos of random users

for user in some_users:
    print(user.get_picture())

# generating a Pandas table about users


def get_users():
    users = []
    for user in RandomUser.generate_users(10):
        users.append({'Name': user.get_full_name(), 'Gender': user.get_gender(), 'City': user.get_city(),
                      'Age': user.get_age(), 'Email': user.get_email(), 'DOB': user.get_dob()})
    return pd.DataFrame(users)


print(get_users())




