#!/usr/bin/python

weightpounds = 0
weightkg = 0
lengthin = 0
lengthcm = 0

def pounds_to_kg(weightpounds):
	weightkg = round(weightpounds*0.4535924, 3)
	return weightkg
	
def in_to_cm(lengthin):
	lengthcm = round(lengthin*2.54, 3)
	return lengthcm
	
print(pounds_to_kg(5))

print(in_to_cm(7))
