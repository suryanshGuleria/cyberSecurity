def stringCase(string):
	count = {"Upper":0,"Lower":0}

	for c in string:
		if c.isupper():
			count["Upper"]+=1

		elif c.islower():
			count["Lower"]+=1

		else:
			pass

	print 'Upper case letters are ', count["Upper"]
	print 'Lower case letters are ', count["Lower"]


stringCase('Hello World Hope You are Doing Fine')
