#!/usr/bin/env python2.7
import time
from firebase import firebase
import occupiedo

input_state = 1
prev_state = 0

occupiedo.change_occupied_state(input_state)

# while True:
#
# 	print "input_state: " + str(input_state)
# 	print "prev_state: " + str(prev_state)
#
# 	if input_state != prev_state:
# 		#door state has changed so fire off actions
# 		occupiedo.change_occupied_state(input_state)
#
# 	prev_state = input_state
# 	time.sleep(0.2)