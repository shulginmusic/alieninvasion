arguments_start_game = ['stats', 'screen', 'ai_settings', 'play_button',
	 'mouse_x', 'mouse_y', 'aliens_group', 'bullets_group', 'ship']
arguments_check_keydown = ['event',
 'ai_settings',
  'screen',
  'ship',
  'bullets']

for argument in arguments_start_game:
	if argument not in arguments_check_keydown:
		print(argument)
		arguments_check_keydown.append(argument)
print("\n")

print(arguments_check_keydown)
print("\n")

arguments_check_events = ['ai_settings',
'stats',
'screen',
'play_button',
'ship',
'bullets_group',
'aliens_group'
]

for argument in arguments_check_keydown:
	if argument not in arguments_check_events:
		print(argument)
		
