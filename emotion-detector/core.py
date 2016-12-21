#############################################################################
#	Copyright 2015 A. Romeo & S. Romeo
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#   	 http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#############################################################################



import string
import sys
import numpy as np

from helpers import *

def main():

	if (len(sys.argv) != 2):
		print "Usage:"
		print "python NexLP.py [arg1]"
		print "	[arg1]: input file containing emails"
		exit()

	ID = setup_dictionary()
	our_file = sys.argv[1]

	# state vars
	happy = 0
	sad = 0
	angry = 0
	irritated = 0
	appreciative = 0
	noword = 0
	linenumber = 0
	previous_word = ""

	
	try:
		with open(our_file, 'r') as f:
			for line in f:
				linenumber = linenumber + 1
				if '########NEXTEMAIL##########' in line:
					if (return_greatest(happy, sad, angry, irritated, appreciative) != 0):
						print linenumber
					happy = 0
					sad = 0
					angry = 0
					irritated = 0
					appreciative = 0
					noword = 0
					previous_word = ""
					
				line = line.translate(string.maketrans("",""), string.punctuation)
				for word in line.split():
					word = word.lower()
					#print word
					try:
						if (word in ID.keys()):
							if (ID[word] >= 1000 and ID[word] < 2000):
								happy = happy + 1
							elif (ID[word] >= 2000 and ID[word] < 3000):
								sad = sad + 1
							elif (ID[word] >= 3000 and ID[word] < 4000):
								angry = angry + 1
							elif (ID[word] >= 4000 and ID[word] < 5000):
								irritated = irritated + 1
							elif (ID[word] >= 5000 and ID[word] < 6000):
								appreciative = appreciative + 1
							elif (ID[previous_word + "" + word] >= 1000 and ID[previous_word + "" + word] < 2000):
								happy = happy + 1
							elif (ID[previous_word + "" + word] >= 2000 and ID[previous_word + "" + word] < 3000):
								sad = sad + 1
							elif (ID[previous_word + "" + word] >= 3000 and ID[previous_word + "" + word] < 4000):
								angry = angry + 1
							elif (ID[previous_word + "" + word] >= 4000 and ID[previous_word + "" + word] < 5000):
								appreciative = appreciative + 1
						else:
							noword = noword + 1
						
						previous_word = word
					except ValueError:
						continue
	except IOError as e:
		print "File does not exist! Please try again with the correct file."
	except:
		print "Unexpected error:", sys.exc_info()[0]

	return_greatest(happy, sad, angry, irritated, appreciative)



# return greatest number
def return_greatest(happy_ct, sad_ct, angry_ct, irritated_ct, appreciative_ct):

	emotion_list = [happy_ct,sad_ct,angry_ct,irritated_ct,appreciative_ct]
	max_emotion = max(emotion_list)
	max_emotion_indx = np.argmax(emotion_list)
	
	if (max_emotion == 0):
		#print 'none'
		return 0
	elif (max_emotion_indx == 0):
		print 'happy'
		return happy_ct
	elif (max_emotion_indx == 1):
		print 'sad'
		return sad_ct
	elif (max_emotion_indx == 2):
		print 'angry'
		return angry_ct
	elif (max_emotion_indx == 3):
		print 'irritated'
		return irritated_ct
	elif (max_emotion_indx == 4):
		print 'appreciative'
		return appreciative_ct
	else:
		print 'none'
		return 0

		
if __name__ == "__main__":
	main()






            


# TODO: check for emoticons, !, caps



