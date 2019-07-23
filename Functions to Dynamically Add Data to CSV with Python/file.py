import csv

with open("data.csv","w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title","Description"])

def get_length(file_path):
    with open("data.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path,name,email):
    fieldnames = ['id','name','email']
    user_id = get_length(file_path)
    with open(file_path,"a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow(
            {
                "id": user_id,
                "name": name,
                "email": email,

            })

append_data("data.csv","Shamoon","hello@hgmail.com")
append_data("data.csv","Shamoon","hello@hgmail.com")
append_data("data.csv","Shamoon","hello@hgmail.com")
append_data("data.csv","Shamoon","hello@hgmail.com")