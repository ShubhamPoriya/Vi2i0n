
#SNELLEN_CHART = {row#:[list of items in row#]}
SNELLEN_CHART = {0 : ['E'], 1 : ['F','P'], 2 : ['T','O','Z'], 3 : ['L','P','E','D'], 4 : ['P','E','C','F','D'], 5 : ['E','D','F','C','Z','P'], 6 : ['F','E','L','O','P','Z','D'], 7 : ['D','E','F','P','O','T','E','C'], 8 : ['L','E','F','O','D','P','C','T'], 9 : ['F','D','P','L','T','C','E','O'], 10 : ['P','E','Z','O','L','C','F','T','D']}


def check_row(row_n, user_input):
	'''
	Checks if user input for a given row is in the list of letters in that row on the Snellen chart
	inputs: row number (number 0-10)
			user reading (letter)
	output: boolean
	'''

	row_values = SNELLEN_CHART[row_n] #get values for row_n from Snellen chart

	if user_input.capitalize() in row_values: #check if input is in row
		return True

	return False