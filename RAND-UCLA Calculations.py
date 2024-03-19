#RAND/UCLA Calculations
#A script to calculate statistics to determine the agreement of an expert panel following the RAND/UCLA Methodology
#Dr. Edgar Ramírez, Aequitas Medica, 2024
#Last Update: 2024-03-19

#Import necessary libraries
import numpy as np

#Determine the file where the captured data is:
CalculationsInput = open("input_route","r")
CalculationsInputLines = CalculationsInput.readlines()

#Determine the outputfile:
CalculationsOutput = open("output_route","w")

#Calculate Median, Lower IPR, Upper IPR, IPR, IPRCP, Asymmetry index, IPRAS, and DI for each line
for CalculationsInputLine in CalculationsInputLines:
	numbers = []
	line = CalculationsInputLine.replace("\n","").split("\t")
	print (line)
	for character in line:
		try:
			char = int(character)
			numbers.append(char)
		except:
			None
	array = np.array(numbers)

	#median
	lmedian = float(np.median(array))
	print (lmedian)

	#LowerIPR
	lLIPR = float(np.percentile(array,10))
	print (lLIPR)

	#UpperIPR
	lUIPR = float(np.percentile(array,90))
	print (lUIPR)

	#IPR
	lIPR = float(lUIPR - lLIPR)
	print (lIPR)

	#IPRCP
	lIPRCP = float((lLIPR + lUIPR)/2)
	print (lIPRCP)

	#Asymmetry index
	lAI = float(abs(5-lIPRCP))
	print (lAI)

	#IPRAS
	lIPRAS = float(2.35 + (1.5 * lAI))
	print (lIPRAS)

	#DI
	lDI = float(lIPR/lIPRAS)
	print (lDI)

	CalculationsOutput.write(CalculationsInputLine.replace("\n","") + "\t" + str(lmedian) + "\t" + str(lLIPR)  + "\t" + str(lUIPR) + "\t" + str(lIPRCP) + str(lAI)  + "\t" + str(lDI)  + "\n")
