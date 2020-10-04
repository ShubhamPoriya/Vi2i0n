from snellen_chart import * #tkinter file
from Snellen_Chart_Check import *

VISUAL_ACUITY = {1 : '20/200', 2 : '20/100', 3 : '20/70', 4 : '20/50', 5 : '20/40', 6 : '20/30', 7 : '20/25', 8 : '20/20'}

def VisionAcuityApp():
	'''
	Driver code for the Visual Acuity App
	inputs: None
	output: visual acuity

	issues: problems connecting with tkinter file

	things to add: 
					1.replicate exam for more accurate results
					2.prompt to do right and left eye individually
					3.Use of Vision API
					4.different GUI (other than tkinter) 
	10/04/2020 By: Ada Del Cid & Subham Poriya
	'''
	break_out = False #True when user input is incorrect

	for row_n in range(1,8): #get row number
		if break_out == True:
			break

		for letter_index in range(row_n): #get letter index in row_n
			user_input = snellen_chart.forward(row_n) #returns user input

			if not check_row(row_n - 1, user_input): #boolean if user got correct entry
				acuity_level = row_n - 1
				break
	
	
	return VISUAL_ACUITY.get(acuity_level)

if __name__ == "__main__":
	VisionAcuityApp()