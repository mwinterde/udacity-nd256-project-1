"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
area_codes = []

for call in calls:
    if call[0][:5] == "(080)":
        # fixed line number
        if call[1][0] == "(":
            i = 1
            area_code = ""
            while True:
                if call[1][i] == ")":
                    break
                else:
                    area_code += call[1][i]
                    i += 1
        # mobile number
        elif " " in call[1]:
            area_code = call[1][:3]
        # telemarketer number
        elif call[1][:2] == "140":
            area_code = "140"
        # unexpected input
        else:
            raise ValueError("Unexpected form of answering number")

        # append
        if area_code not in area_codes:
            area_codes.append(area_code)

print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(area_codes):
    print(area_code)


# Part B
counter_condition = 0
counter_total = 0

for call in calls:
    if call[0][:5] == "(080)":
        counter_total += 1
        if call[1][:5] == "(080)":
            counter_condition += 1

perc = counter_condition / counter_total
print(f"{perc*100:.2f} percent of calls from fixed lines in Bangalore are "
      f"calls to other fixed lines in Bangalore.")