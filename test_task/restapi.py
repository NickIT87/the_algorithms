import requests


# GET USER
r = requests.get('https://gorest.co.in/public/v1/users/71')
#print(r.json())


# REGISTER NEW USER
payload = {
    'name':'Mustafa Hibanov',
    'email': 'mhibanov@mail.com',
    'gender': 'male',
    'status': 'active'
}
rp = requests.post(
    'https://gorest.co.in/public/v1/users?access-token=78ab1bab3be86ad08857c152f1dc69282fb3d5b6be6f91111f9cc3a83e7b8b22', 
    data=payload
)
# print(rp.status_code)
# print(rp.headers)   # 'https://gorest.co.in/public/v1/users/1713'
newUser = requests.get('https://gorest.co.in/public/v1/users/1713')
#print(newUser.json())


# UPDATE USER
payload2 = {
    'name':'Mustafa Hibanovskiy',
    'email': 'mhibanovskiy@mail.com',
    'gender': 'female',
    'status': 'active'
}
update = requests.patch('https://gorest.co.in/public/v1/users/1713?access-token=78ab1bab3be86ad08857c152f1dc69282fb3d5b6be6f91111f9cc3a83e7b8b22', data=payload2)
#print(update.status_code)
#updatedUser = requests.get('https://gorest.co.in/public/v1/users/1713')
#print(updatedUser.json())


# DELETE USER
delusr = requests.delete('https://gorest.co.in/public/v1/users/1713?access-token=78ab1bab3be86ad08857c152f1dc69282fb3d5b6be6f91111f9cc3a83e7b8b22')
#print(delusr.status_code)