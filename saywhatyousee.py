#	The goal of this exercise was to take a string of digits and turn them into words that you would say:
#	e.g. 	11 = "two 1's"
#			5551 = "three 5's, and one 1"
#			7711999 = "two 7's, two 1's, and three 9's"
#


def  say_what_you_see(input_strings):
	
	input_strings = str(input_strings)
	
	global my_list
	my_list = []
	final_list = []
	
	#create an iterable list of strings
	for each in input_strings:
		my_list.append(each)

	#get the counter for each item using the count_digits function
	for i in range(0,len(my_list)):
		counter = count_digits(i)

		#add only one item and its counter to final list
		if my_list[i] != my_list[i-1]:
			final_list.append([my_list[i],counter])
		
		#if there's nothing in the final_list yet, add the first item anyway.
		elif final_list == []:
			final_list.append([my_list[i], counter])

	#prepare final_string to return
	final_string = ""
	for each in range(len(final_list)):
		final_list[each][1] = numbertoword(final_list[each][1])
	
	for each in range(len(final_list)):
		#create base string for each item in format "word number"
		x = final_list[each][1] + " " + final_list[each][0]
		#if there's only one counter, don't add 's'
		if final_list[each][1] != "one":
			x += "'s"
		
		#if it's not the last on the list
		if each < len(final_list)-1:
			x += ", "
		
		#else if it's not the first on the list
		elif each == 0:
			pass


		else:
			x = "and " + x
		#if it's the last in the string, add 'and'

		final_string += x
		
	return final_string



def count_digits(index):
	#This function returns the number of times a particular digit my_list[index] appears in a row within my_list
	i = index
	counter = 0
	j = i
	
	while my_list[i] == my_list[j] and j < len(my_list)-1:
		counter += 1
		
		#check to see if it's the last round
		if j == len(my_list)-2 and my_list[i] == my_list[j+1]:
			counter +=1
		
		j += 1

	if counter == 0: counter = 1
	return counter


def numbertoword(num):
	#this is the dictionary used to turn numbers from digit to word form. It return the word of a number.
	worddict = {
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten"
	}

	word = worddict[num]
	
	return word
	
print say_what_you_see(1143555544)
print say_what_you_see(7762333)
print say_what_you_see(43341)


