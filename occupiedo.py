from firebase import firebase
import requests
from config import fbRef

FIREBASE = firebase.FirebaseApplication(fbRef, None)

# updates firebase to the new state
def change_occupied_state(state):
	if state == 0:
		#toilet is now unoccupied
		FIREBASE.put('/', 'occupied', 'false')
		print('Set green')
		get_next_in_queue()
	else:
		#toilet is now occupied 
		FIREBASE.put('/', 'occupied', 'true')
		print('Set red')

# gets next in queue
def get_next_in_queue():
	url = fbRef +'queue.json?orderBy="$key"&limitToFirst=1&print=pretty'
	data = requests.get(url)
	json_object = data.json()
	person = None
	number = None

	# get lastest entry
	for key in json_object: 
		person = json_object[key]
	
	# check if anyone is in queue
	if person == None:
		print ("no one in queue")
	else:
		name = person['name']
		#number = os.getenv(name)
		# delete entry
		FIREBASE.delete('/queue', key)