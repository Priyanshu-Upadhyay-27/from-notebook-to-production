def insert_patient_data(name, age):
    print(name, age)
    print("Inserted into database")

# A junior developer might incorrectly pass age as a string:
insert_patient_data("Nitish", "30")

def insert_patient_data(name: str, age: int):
    print(name, age)
    print("Inserted into database")

# This still runs without any errors despite the type hints!
insert_patient_data("Nitish", "30")

def insert_patient_data(name: str, age: int):
    # 1. Type Validation
    if type(name) == str and type(age) == int:
        
        # 2. Data Validation
        if age < 0:
            raise ValueError("Age can't be negative")
        else:
            print(name, age)
            print("Inserted into database")
            
    else:
        raise TypeError("Incorrect data type")

insert_patient_data("Nitish", "30") # Now this properly throws an error