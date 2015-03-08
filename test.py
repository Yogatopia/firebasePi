from firebase import firebase
firebase = firebase.FirebaseApplication('https://occupied-demo.firebaseio.com/', None)
new_user = 'Mando'

# result = firebase.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
# print (result)

result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print (result)
