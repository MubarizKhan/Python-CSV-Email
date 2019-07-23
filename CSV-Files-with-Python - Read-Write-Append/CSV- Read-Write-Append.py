import csv

with open("data.csv","w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title","Description"])
    writer.writerow(["row 1","Descript"])
    writer.writerow(["row 2","Description"])
    writer.writerow(["row 3","Descript"])

# "a" Append to a file--- add to the very end
# "w" writes to the file, w+ overwrites to the file
# "r" read only
# "r+" read & write
# "rb" read in binary form

with open("data.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


with open("data.csv","a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["hi", "my name is","johnny doe"])
    writer.writerow(["hi", "my name is","johnny doe"])
    writer.writerow(["hi", "my name is","johnny doe"])
    writer.writerow(["hi", "my name is","johnny doe"])

with open("data.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in csv.DictReader(csvfile):
        print(row)


