class Agency:
    def __init__(self, name):
        self.name = name
        self.resources = []

    def add_resource(self, resource):
        self.resources.append(resource)

    def display_resources(self):
        print(f"{self.name}'s Resources:")
        for resource in self.resources:
            print(f"- {resource.type}: {resource.quantity}")

class Resource:
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

class Request:
    def __init__(self, agency_name, resource_type, quantity):
        self.agency_name = agency_name
        self.resource_type = resource_type
        self.quantity = quantity

# Creating an instance of Agency
agency1 = Agency("Disaster Response Team")

# Adding resources to the agency
agency1.add_resource(Resource("Food", 1000))
agency1.add_resource(Resource("Water", 500))

# Displaying the resources added to the agency
agency1.display_resources()

# Creating a request
request = Request("Disaster Response Team", "Food", 200)

# Printing the request details
print(f"\nRequest Details:\nAgency Name: {request.agency_name}\nResource Type: {request.resource_type}\nQuantity: {request.quantity}")