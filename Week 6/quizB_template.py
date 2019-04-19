# from quizB_others import sum_of_double_even_place, get_size, get_prefix
def is_valid(number):
	valid = (4,5,37,6)
	size = get_size(number)
	if size > 12 and size < 17:
		for i in valid:
			if get_prefix(number,i):
				tot = sum_of_odd_place(number) + sum_of_double_even_place(number)
				if tot%10 == 0:
					answer = True
				else:
					answer = False
				
			
			else:
				answer = False
	else: 
		answer = False
	
	return answer
	
print is_valid(4388576018402626) #F
print is_valid(4388576018410707) #T
print is_valid(371826291433349)  #T
print is_valid(5411045872559122) #T
print is_valid(6011432717792989) #T


def get_digit(number):
	total = 0
	if number<10:
		total = number
	else:
		number = str(number)
		ls = list(number)
		for i in range(len(ls)):
			temp = int(ls[i])
			total += temp
	
	return total
	
#print get_digit(1123)


def sum_of_odd_place(number):
	snumber = str(number)
	snumber = snumber[::-1]
	odd = snumber[0::2]
	lnumber = list(odd)
	total = 0
	for i in range(len(odd)):
		total += int(odd[i])

	return total
	
# print sum_of_odd_place (1234) # 4+2 = 6	
# print sum_of_odd_place(4388576018402626)#38



def prefix_matched(number, d):
	strd = str(d)
	ld = list(strd)
	length = len(ld)
	a = get_prefix(number, length)
	if d == a:
		ans = True
	else:
		ans = False
	return ans
	
# print prefix_matched(4388576018402626,4)
# print prefix_matched(4388576018402626,5)
# print prefix_matched(4388576018402626,43)


