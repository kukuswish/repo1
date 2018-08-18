# Modules
import os
import csv
from glob import iglob

# Set path for file
csvpath = os.path.join("..", "Resources", "cereal.csv")

found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #header
    csv_header= next(csvfile)
    print(f"Header: {csv_header}")
    
    # next(csvreader, None)

    for row in csvreader:
        if(float(row[7]) >= 5):
        	print(row)

# unique_headers = set()

# with open(csvpath, newline="") as fin:
#     csvin = csv.reader(fin)
#     unique_headers.update(next(csvin, []))
# print(csvin)