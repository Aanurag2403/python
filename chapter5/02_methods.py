marks = {
    "harry": 100,
    "shubham":56,
    "rohan":43
}

#items
print(marks.items())

#keys
print(marks.keys())

#values
print(marks.values())

#update
marks.update({"harry": 99, "renuka":100})
print(marks)

#get
print(marks.get("harry")) #returns an error if having an unknown value

#clear
marks.clear()
print(marks)

#length
a= len(marks) 