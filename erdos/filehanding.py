def generate(filename):
	myfile = open(filename, "w")
	myfile.write("line 1\n")
	myfile.write("line 2\n")
	myfile.write("line 3\n")
	myfile.write("line 4\n")
	myfile.close()

#generate("hello.txt")

def write_line_numbers(infilename, outfilename):
	infile = open(infilename, "r")
	outfile = open(outfilename, "w")
	counter = 1 

	while True:                            # Keep reading forever
		theline = infile.readline() 	  # Try to read next line
		if len(theline) == 0:              # If there are no more lines
			break                          #     leave the loop

		# Now process the line we've just read
		outfile.write('{num:05d}: {line}'.format(num=counter, line=theline))
		counter += 1
	infile.close()
	outfile.close()

def remove_line_numbers(linedfilename, outfilename):
	infile = open(linedfilename, "r")
	outfile = open(outfilename, "w")

	while True:                            # Keep reading forever
		theline = infile.readline() 	  # Try to read next line
		if len(theline) == 0:              # If there are no more lines
			break                          #     leave the loop

		colon = theline.find(":")
		outfile.write(theline[colon+2:])

	infile.close()
	outfile.close()

#write_line_numbers("hello.txt", "lined.txt")
remove_line_numbers("lined.txt", "unlined.txt")
