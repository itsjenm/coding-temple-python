'''
Python City Planning Simulator


Task 3: File Handling for Building Records

Problem Statement: Implement a system to handle building records using file operations. 
Create a Building class and write a script to save and load building details to and from a file

'''

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    # Methods to save to file and load from file
    def save_to_file(self, filename):
        # Saves the building details to a file in JSON format.
        with open(filename, 'w') as file:
            file.write(f"{self.name}\n")
            file.write(f"{self.floors}\n")

    @classmethod
    def load_from_file(cls, filename):
        """Loads the building details from a file and returns a Building object."""
        with open(filename, 'r') as file:
            name = file.readline().strip()
            floors = int(file.readline().strip())
            return cls(name, floors)
    
    def __str__(self):
        # Returns a string representation of the building.
        return f"Building: {self.name}, Floors: {self.floors}"


building = Building("Skyscraper", 50)
building.save_to_file("building_record.txt")
loaded_building = Building.load_from_file("building_record.txt")
print(loaded_building)
