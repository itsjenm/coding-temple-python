total_students = 30
rows = 5

students_per_row = total_students // rows

for row in range(1, rows + 1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row - 1) * students_per_row + seat
        print(f"Row {row} - Seat {seat}: Student {seat_number}")