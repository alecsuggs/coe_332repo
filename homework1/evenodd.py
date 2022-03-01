
mynumbers = [2,4,6,88,22,100,99,45,10,77]

def evenodd(numbers):
	for i in range(10):
		if ( numbers[i]%2 == 1):
			print(numbers[i] , '- odd')
		elif( numbers[i]%2  == 0):
			print(numbers[i] , '- even')

evenodd(mynumbers)


			
