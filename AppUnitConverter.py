#!/usr/bin/python

weightpounds = 0
weightkg = 0
lengthin = 0
lengthcm = 0

def pounds_to_kg(weightpounds):
	weightkg = weightpounds*0.4535924
	return weightkg
	
def in_to_cm(lengthin):
	lengthcm = lengthin*2.54
	return lengthcm
	
print(pounds_to_kg(5))

print(in_to_cm(7))
