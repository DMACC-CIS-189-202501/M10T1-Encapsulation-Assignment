# TODO 1: Delete this line and put your docstring

class Employee:
    """
    Employee class.
    """

    # TODO 2: __init__ method accepts two arguments: first_name and last_name.
    # Modify __init__ to also take an address (str), phone_number (str), salary (float), and start_date(str)
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        # TODO 3: don't forget to take your arugments and set them to a value on the object; eg:
        # self.last_name creates a last_name value on the object, then the '= last_name' assigns it to the value passed 
        # into the __init__ function

    def display(self):
        """
        Display employee information as:

            LAST_NAME, FIRST_NAME: <last name, first name here>
            PHONE_NUMBER: <phone number here>
            ADDRESS: <address here>
            START_DATE: <start date here>
            SALARY: <salary here>

        :return: string showing the above
        """

        # TODO 4: Complete the output string to match the above       
        output = (
            f"LAST_NAME, FIRST_NAME: {self.last_name}, {self.first_name}\n"
            #f"PHONE_NUMBER: {self.phone_number}\n"
        )
        
        return output

# Note: Because this main is unintended; it and the code all below it are not part of the Employee class/object
def main():

    person_list = [
        {"last_name": "VanRossum", "first_name": "Guido","address": "461 Ocean Blvd",
        "phone_number": "773-735-1849", "salary": 97500, "start_date": "1991-02-22"},

        {"last_name": "Haggard", "first_name": "Merle","address": "Bakersfield, CA",
        "phone_number": "484-765-2231", "salary": 72500, "start_date": "1967-11-08"},

        {"last_name": "Prine", "first_name": "John","address": "Paradise, KY",
        "phone_number": "743-435-8310", "salary": 88500, "start_date": "1995-07-31"},
        ]
    
    # TODO 5:
    # Iterate over person_list, and create a new Employee instance and call the 
    # display method for each.
    # for example, if you had
    # person = {"last_name": "VanRossum", "first_name": "Guido","address": "461 Ocean Blvd", "phone_number": "773-735-1849", "salary": 97500, "start_date": "1991-02-22"}
    # you could do employee = Employee(person.last_name, person.first_name, person.address, person.phone_number, person.salary, person.start_date)
    # then employee.display()

    ##### YOUR CODE HERE #####



if __name__ == "__main__":

    main()
