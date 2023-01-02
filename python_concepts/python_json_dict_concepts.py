data = {
   "employee": [

      {
         "id": "01",
         "name": "Amit",
         "department": "Sales"
      },

      {
         "id": "04",
         "name": "sunil",
         "department": "HR"
      }
   ]
}

print(type(data))

import json


# convert json string into dict object

employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
print(type(employee))
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))


# read json file and load in dict

with open("json_employee_file.json", "r") as employye_file:
   employye_file_dict = json.load(employye_file)
print(employye_file_dict)
print(type(employye_file_dict))


# convert dict object into json and dump it in a file

json_object = json.dumps(employye_file_dict)
print(json_object)
print(type(json_object))
with open("json_employee_file1.json", "w") as outfile:
   json.dump(employye_file_dict, outfile)


# append the json
append_data = {"name": "jane doe1", "salary": 90010, "skills": ["Raspbderry pi", "Machine Leadrning", "Web Devedlopment"], "email": "JaneDode@pynative.com"}
with open("json_employee_file2.json", "r+") as outfile:
   dict_object = json.load(outfile)
   dict_object["emp_details"].append(append_data)
   print(dict_object)
   outfile.seek(0)
   json.dump(dict_object, outfile, indent=4)






