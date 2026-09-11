
look_up = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
replace_val = {"IV": 4, "IX":9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

def romanToInt(s: str) ->int:
	year = 0
	rep = ["IV", "IX", "XL", "XC", "CD", "CM" ]
	for i in rep:
		if i in s:
			year += replace_val[i]
			s = s.replace(i, "")
			print(s, year)
	for i in s:
		year += look_up[i]

	return year

print(romanToInt("MCMXCIV"))