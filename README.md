# Paranuara

## Build


To build the project, alias python=python3 if the python3.6 needs to be run as python3 on the machine.

Goto root/ directory and run sh prepare.sh to build.

`* make sure the port 8000 is not using`
```
>> sh run.sh
```
Alternatively, you may use the makefile under root directory to build by running
```
>> make
```

## External Libraries

External libraries are specified inrequirements.txt 


## Run

After building the project, to run as DEVELOPMENT, run `sh run.sh` which will startup a development server on http://localhost:8000/api/

## APIs
### List all the employees belong to specific company
- http://127.0.0.1:8000/v1/api/employees/{company_index}
- permission: any
- method: `GET`
- header fields: `None`
- body fields: `None`
- index: `company index`
- return: `{"index": company index,
    "company": "comapny name",
    "employees": [...]}`  
    `HTTP 404` or `HTTP 200`


### Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
http://127.0.0.1:8000/v1/api/samefriends/{people_index1}/{people_index2}/
- permission: any
- method: `GET`
- header fields: `None`
- body fields: `None`
- index: `two people index`
- return: `{"people1": {"name": "Decker Mckenzie", "age": 60, "address": "492 Stockton Street, Lawrence, Guam, 4854", "phone": "+1 (893) 587-3311"}, "people2": {"name": "Bonnie Bass", "age": 54, "address": "455 Dictum Court, Nadine, Mississippi, 6499", "phone": "+1 (823) 428-3710"}, "same_friends": [{"name": "Decker Mckenzie", "age": 60, "address": "492 Stockton Street, Lawrence, Guam, 4854", "phone": "+1 (893) 587-3311"}]}`  
`HTTP 404` or `HTTP 200`

### Given 1 people, provide a list of fruits and vegetables they like.
http://127.0.0.1:8000/v1/api/fruit_and_vegetable/{people_index}/
- permission: any
- method: `GET`
- header fields: `None`
- body fields: `None`
- index: `company index`
- return: `{"username": "Rosemary Hayes", "age": 30, "fruits": ["orange", "apple"], "vegatables": ["carrot", "celery"]}`  
    `HTTP 404` or `HTTP 200`


