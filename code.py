
a = []
b = []

def filelist():
	file = open("anagramlist.txt", "r")
	for line in file:
		a.append(line.strip())
		b.append(line.strip())

def is_anagram(test, original):
  return sorted(list(test.lower())) == sorted(list(original.lower()))



filelist()

summ = 0

for i in range(len(a)):
	for x in range(len(b)):
		if a[i] != b[x]:
			if is_anagram(a[i],b[x]):
				print a[i], b[x]
				summ += 1

print summ

