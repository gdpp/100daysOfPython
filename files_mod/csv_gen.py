import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Summoner Name", "Trophies"])
    writer.writerow(["Faker", "5"])
    writer.writerow(["Oner", "5"])
    writer.writerow(["Gumayusi", "5"])
    writer.writerow(["Keria", "4"])
    writer.writerow(["Doran", "3"])
    writer.writerow(["Chovy", "2"])
    writer.writerow(["Showmaker", "1"])
    

with open("data.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    
    for row in reader:
        print(row)