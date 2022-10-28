#Input variables: first and last name
print("Hello, please enter your first and last name:")
first_name = input("Enter your first name: ")
print(first_name)
last_name = input("Enter your last name: ")

#Username = first three letters of last name and last four numbers of the last name
def username_generator(first_name, last_name):
  if len(first_name) < 3:
    username = first_name
  else:
    username = first_name[0:3]
  if len(last_name) < 4:
    username += last_name
  else:
    username += last_name[0:4]
  return username

#Def username variable w/ username func, print username
username = username_generator(first_name, last_name)
print("Your username is: " + username)

#Password = last letter of username moves to the front of the name
def password_generator(username):
    temp_pass = ""
    for i in range(0, len(username)):
        temp_pass += username[i-1]
    return temp_pass

temp_pass = password_generator(username)
print("Your temporary password is: " + temp_pass)
print("Don't forget to change your password.")