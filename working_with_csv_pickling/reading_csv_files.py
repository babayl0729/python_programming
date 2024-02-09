# Reading CSV Files
# CSV files are common file format for tabular data.
# We can read CSV files just like other text files.
# Python has a built-in CSV module to read/write CSVs more easily.

# CSV Module
# reader - lets you iterate over rows of the CSV as list.
# DictReader - lets you iterate over rows of the CSV as OrderDicts.

# Other Delimiter
# Readers accept a delimeter kwarg in case your data isn't
# separated by commas.

# using reader
from csv import reader
from csv import DictReader

with open("fighters.csv") as file:
    # this where you call reader and passed in the file the you opened.
    csv_reader = reader(file)
    # if you don't want the headers.
    # you'll start after the headers.
    next(csv_reader)
    for fighter in csv_reader:
        #print(fighter)
        print(f"{fighter[0]} is from {fighter[1]}")

# to turn into list
with open("fighters.csv") as file2:
    csv_reader2 = reader(file2)
    data2 = list(csv_reader2)
    print(f"\n{data2}")

# using DictReader
with open("fighters.csv") as file3:
    csv_reader3 = DictReader(file3)
    for row in csv_reader3:
        #print(f"\n{row}")
        print(row["Name"])

# using Other Delimiter
with open("fighters2.csv") as file4:
    # you can do either reader or DictReader 
    csv_reader4 = reader(file4, delimiter="|")
    for row in csv_reader4:
        print(row)