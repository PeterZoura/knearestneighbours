import sys

'''
python3 knn.py <testDataFilename.csv> <k> <num_of_test_points>

K nearest neighbours
1.1 store attribute names in list
1.2 store data instances in list, store them as strings with string[0] being the first attribute's char and string[21] being the last attribute's char
#1.3 sort them, i'll skip this for now
1.4 store test data in list from file

loop through strings
	use hamming distance to compare string similarity
	pick k nearest hamming distance strings

end loop
take majority class that those k follow
assign that class to data point

compare test data point with k nearest 

1.5 output ratio of success

'''


#1.1 store attribute names
iF = open('Mushies_modified.csv', 'r')
str = iF.readline()
attributes = ['']
j = 0
for chr in str:
	match chr:
		case '"':
			continue
		case '\n':
			continue
		case ',':
			j += 1
			attributes.append('')
		case _:
			attributes[j] += chr
attributes.pop(0)
print(len(attributes))

#1.2 store data point as string
trainInput = []
trainCorrect = []
#i = 0

for x in range(5000):
	skipFirstAttribute = False
	str = iF.readline()
	trainInput.append('')
	trainCorrect.append('')
	for chr in str:
		match chr:
			case '"':
				continue
			case '\n':
				break
			case ',':
				continue
			case _:
				if not skipFirstAttribute:
					skipFirstAttribute = True
					trainCorrect[x] += chr
					continue #the purpose of this is to skip the first attribute in the list, which is whether it is poisonous or edible
				trainInput[x] += chr



#1.3 sorting
def hamming_distance(chaine1, chaine2): #directly copy pasted from stackoverflow.com post.
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))


#1.4 storing test data
testInput = []
testCorrect = []
iT = open(sys.argv[1])

for x in range(int(sys.argv[3])):
	firstAttribute = True
	str = iT.readline()
	testInput.append('')
	testCorrect.append('')
	for chr in str:
		match chr:
			case '"':
				continue
			case '\n':
				break
			case ',':
				continue
			case _:
				if firstAttribute:
					firstAttribute = False
					testCorrect[x] += chr
					continue #the purpose of this is to skip the first attribute in the list, which is whether it is poisonous or edible
				testInput[x] += chr


#1.5 compare

k = int(sys.argv[2])

'''
Comparisons is a list of lists.
example: comparisons[i]
i is an index referring to one of the testing data points.
comparisons[i] is a list of pairs (x,y)
x is an index referring to the training data points
y is the hamming distance from the testing data point i to the training data point x
'''

comparisons = []
for i in range(len(testInput)):
	comparisons.append([])
	for j in range(len(trainInput)):
		comparisons[i].append( (j, hamming_distance(trainInput[j], testInput[i]) ) )


'''
selection sort is used to sort the pairs in each list so that they are in ascending order
according to their hamming distances
'''

#this is where the algorithm takes a long time
n = 0
for lst in comparisons:
	if n%20==0:
		print(f'Comparing for {n}')
	n +=1
	for i in range(len(lst)):
		low = i
		for j in range(i+1, len(lst)):
			if lst[j][1] < lst[low][1]:
				low = j
		lst[i], lst[low] = lst[low], lst[i]

'''
#print code for debugging
print('Here are the k nearest neighbours for each test input, in the format of (index, nearness) poison/edible')
for x in comparisons:
	for y in range(k):
		print(x[y], trainCorrect[x[y][0]], end=', ')
	print('')

'''
'''
Now that I have compared testing data point i to every training data point, I can select
the k nearest ones, that will be the first k items in comparisons[i]

'''



results = []
for i in range(len(comparisons)):
	sumPositive = 0
	for n in range(k):
		if(trainCorrect[comparisons[i][n][0]] == 'p'):
			sumPositive += 1
	if sumPositive > k/2:
		results.append('p')
	else:
		results.append('e')

#number of successes
numS = 0

for x in range(len(results)):
	if results[x] == testCorrect[x]:
		numS += 1
tempvalue = numS/len(results)
print(f'Ratio of success: {tempvalue}')

iT.close()
iF.close()

