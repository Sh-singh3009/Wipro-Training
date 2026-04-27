import csv
import os       #used only for file deletion

def write_csv(filename):
    data = [
        {'name':'shaurya', 'age':23},
        {'name':'ansh', 'age':22}
    ]
    columnnames = ['name','age']
    with open(filename, "w", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)
    print("CSV file written successfully")

def read_csv(filename):
    with open(filename, "r", newline="\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")

def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} file doesn't exist")

filename = "myfile.csv"
write_csv(filename)
print("Data read from CSV file")
read_csv(filename)
#don't delete it before creating it
#delete_csv(filename)