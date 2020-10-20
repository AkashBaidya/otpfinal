import random
import string


class Random:

	def randomStringDigits(stringLength=6):
    	lettersAndDigits = string.ascii_letters + string.digits
    	return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))