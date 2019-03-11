'''
Configuration settings for csv parsing.

Assumes there may be multiple glowsuits defined in one csv file.
Relative ordering of suit settings must be consistent and contiguous.

If suit 1's setting is defined as:
Col #		5				6			    7					 n
		PRESET_NAME		LEFT_LEG		RIGHT_LEG 	...		SOME_SETTING

Then suit 2's settings must be organized as:
Col #		n+1				n+2			   n+3					n+n
		PRESET_NAME		 LEFT_LEG		RIGHT_LEG	...		SOME_SETTING


And so forth for any additional suits.
'''

# Forever (in milliseconds). Used in place on infinite delay.
FOREVER = 500000

# Column number of 'absolute time' in csv file
TIME_ABS_COL = 1
# Column number of 'diff time' in csv file
TIME_DIFF_COL = 2
# Preset column (1st one if multiple)
PRESET_COL = 5

# Ordering of light bool values (distance from respective preset column)
LA = 1
RA = 2
LL = 3
RL = 4
HB = 5
WB = 6
YP = 7
RP = 8

# Number of columns dedicated to non-lighting information (e.g. time, comments)
NUM_HEADER = 5
# Number of columns dedicated to glowsuit settings (e.g. preset, lighting bools)
# (PER GLOWSUIT IF MULTIPLE SUITS)
NUM_SETTINGS = 9
