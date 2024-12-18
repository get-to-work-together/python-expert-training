from user import User

user = User(username = 'peteranema',
            email='peter.anema@tip.nl',
            fullname = 'Peter Anema')

user.set_password('Welkom01!')

print(user)

try:
    user.set_email('invalid')
except:
    print('That is an invalid e-mail address! Nothing has been changed.')

passwords = ['WRONGPASSWORD!', 'XX', 'Welkom01!']
for password in passwords:
    correct = user.validate_password(password)
    if correct:
        print(f'The password {password} is correct.')
    else:
        print(f'The password {password} is incorrect.')

user.active = False
print(user.login('Welkom01!'))
user.active = True
print(user.login('Welkom01!'))


print(user.password_hash)

print(user.token)