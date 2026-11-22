with open("student_names.txt", "w+", encoding="utf-8") as file:
    file.write("omkar \n")
    file.write("anjali \n")
    file.write("rushabh \n")
    file.write("aniket \n")


with open("student_names.txt", "r", encoding="utf-8") as file:
    content=file.read()

print(content)


#csv file 

import csv

oilpaint = [
    {"colour": "yellow", "price": 126},
    {"colour": "white", "price": 380},
    {"colour":"blue", "price": 777},
]

with open("oilpaint.csv", "w", newline="", encoding="utf-8") as file:
    writer= csv.DictWriter(file, fieldnames=["colour","price"])
    writer.writeheader()
    writer.writerows(oilpaint)

print("Done")

with open("oilpaint.csv", "r",newline="", encoding="utf-8") as file:
    reader= csv.DictReader(file)

    for row in reader:
        print(row)
        print(row ["colour"], row["price"])


# json file

exam={
    "subject": "math",
      "total_marks": 100,
        "chapter":["add","subtract","multiply"]
    }

with open("exam.json", "w",newline="", encoding="utf-8") as file:
    json.dump(exam,file,indent=2)

print("exam_schedule")

with open("exam.json", "r",newline="", encoding="utf-8") as file:
    read_exam=json.load(file)

print(read_exam)
print(read_exam["total_marks"])
print(read_exam["chapter"])
