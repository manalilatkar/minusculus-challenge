
keyboard_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g', 43: 'h', 44: 'i', 45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q', 53: 'r', 54: 's', 55: 't', 56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z', 62: '.', 63: ',', 64: '?', 65: '!', 66: "'", 67: '"', 68: ' '}
keyboard_reverse_map = {'!': 65, ' ': 68, '"': 67, "'": 66, ',': 63, '.': 62, '1': 1, '0': 0, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8, '?': 64, 'A': 10, 'C': 12, 'B': 11, 'E': 14, 'D': 13, 'G': 16, 'F': 15, 'I': 18, 'H': 17, 'K': 20, 'J': 19, 'M': 22, 'L': 21, 'O': 24, 'N': 23, 'Q': 26, 'P': 25, 'S': 28, 'R': 27, 'U': 30, 'T': 29, 'W': 32, 'V': 31, 'Y': 34, 'X': 33, 'Z': 35, 'a': 36, 'c': 38, 'b': 37, 'e': 40, 'd': 39, 'g': 42, 'f': 41, 'i': 44, 'h': 43, 'k': 46, 'j': 45, 'm': 48, 'l': 47, 'o': 50, 'n': 49, 'q': 52, 'p': 51, 's': 54, 'r': 53, 'u': 56, 't': 55, 'w': 58, 'v': 57, 'y': 60, 'x': 59, 'z': 61}

def put_request(q_url, answer):
    return requests.put(q_url, data=json.dumps(answer))

    
#=======================================================
#first question


def first_wheel_convert(key_in, wheel_setting):
    return [keyboard_map[(keyboard_reverse_map[k]+wheel_setting)%69] for k in key_in]

# answer = ''.join(first_wheel_convert('Strong NE Winds!',6))


#=======================================================
#second question

def second_wheel_convert(key_in, wheel_setting):
	return [keyboard_map[(keyboard_reverse_map[k]-2*wheel_setting)%69] for k in key_in]


# JX - J3 
#34+2*19%69 = 3, 31+33*2%69 = 28, 59+30*2%69 = 50
#second question final command
# answer = ''.join(second_wheel_convert(first_wheel_convert('The Desert Fox will move 30 tanks to Calais at dawn', 9),3))

#=======================================================
#third question

def third_wheel_convert(key_in, orig_data):
	prev_char_index = 0
	prev_char = 0
	decoded_string=[]
	for k in key_in:
		ind = keyboard_reverse_map[k]
		new_ind = (ind+2*prev_char)%69
		prev_char = keyboard_reverse_map[orig_data[prev_char_index]]
		prev_char_index = prev_char_index + 1
		decoded_string.append(keyboard_map[new_ind])
	return ''.join(decoded_string)

input_message = 'The white cliffs of Alghero are visible at night'

# first_level_answer = ''.join(second_wheel_convert(first_wheel_convert(input_message, 4),7)) 
#print third_wheel_convert(list(first_level_answer), list(input_message))



#=======================================================
#fourth question

enc_message = list("WZyDsL3u\'0TfxP06RtSSF \'DbzhdyFIAu2 zF f5KE\"SOQTNA8A\"NCKPOKG5D9GSQE\'M86IGFMKE6\'K4pEVPK!bv83I")

def decrypt_mark_four(enc_message, wheel_setting_one, wheel_setting_two):
	print enc_message
	third_wheel_position = 0
	decoded_string = []
	for m in enc_message:
		ind = keyboard_reverse_map[m]
		new_ind = ind - 2*third_wheel_position
		new_ind = (new_ind + 2*wheel_setting_two - wheel_setting_one)
		print new_ind
		new_ind = new_ind%69
		decoded_string.append(keyboard_map[new_ind])
		third_wheel_position = new_ind
    
	return decoded_string


#print ''.join(decrypt_mark_four(enc_message,7,2))



#=======================================================
#fifth question


json = list("QT4e8MJYVhkls.27BL9,.MSqYSi\'IUpAJKWg9Ul9p4o8oUoGy\'ITd4d0AJVsLQp4kKJB2rz4dxfahwUa\"Wa.MS!k4hs2yY3k8ymnla.MOTxJ6wBM7sC0srXmyAAMl9t\"Wk4hs2yYTtH0vwUZp4a\"WhB2u,o6.!8Zt\"Wf,,eh5tk8WXv9UoM99w2Vr4!.xqA,5MSpWl9p4kJ2oUg\'6evkEiQhC\'d5d4k0qA\'24nEqhtAQmy37il9p4o8vdoVr!xWSkEDn?,iZpw24kF\"fhGJZMI8nkI")

def decrypt_mark_four_unknown_wheel_settings(enc_message, wheel_setting_total):
	third_wheel_position = 0
	decoded_string = []
	for m in enc_message:
		ind = keyboard_reverse_map[m]
		new_ind = ind - 2*third_wheel_position
		new_ind = (new_ind + wheel_setting_total)
		new_ind = new_ind%69
		decoded_string.append(keyboard_map[new_ind])
		third_wheel_position = new_ind
    
	return decoded_string

# the following loop will print out all the 69 inputs that could have resulted from any of the 69 wheel settings, identify the right one.
k = 0
for x in range(0,70):
	#print k
	#print ''.join(decrypt_mark_four_unknown_wheel_settings(json, k))
	k = k+1

















