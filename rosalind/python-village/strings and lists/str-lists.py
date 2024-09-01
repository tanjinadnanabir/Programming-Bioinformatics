with open('rosalind_ini3.txt') as input_data:
	s, points = [line.strip() for line in input_data.readlines()]
	a,b,c,d = map(int, points.split())

slices = [s[a:b+1], s[c:d+1]]

print (' '.join(slices))
with open('Python_INI3.txt', "w") as output_data:
	output_data.write(' '.join(slices))