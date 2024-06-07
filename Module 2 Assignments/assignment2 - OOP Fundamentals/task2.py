'''
Task 2: Event Management System Enhancement

Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

'''

class Event:
    def __init__(self, name, date):
        self.participants = []
        self.count = 0
        self.name = name
        self.date = date

    def add_participant(self, participant):
        self.participants.append(participant)
        self.count += 1

    def get_participant_count(self):
        return self.count

    def __str__(self):
        # Returns a string representation of the event.
        return f"Event: {self.name}, Date: {self.date}, Participants: {self.count}"

    
event1 = Event("Python Workshop", "2024-07-15")
event1.add_participant("Alice")
event1.add_participant("Bob")
event1.add_participant("Charlie")

count = event1.get_participant_count()
print(f"Number of participants: {count}")

print(event1)