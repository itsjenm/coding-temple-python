
room_temperatures = [22, 24, 19, 21]
room_names = ["living", "kitchen", "bedroom", "bathroom"]

warmest_temp = max(room_temperatures)
coolest_temp = min(room_temperatures)

# use indexes to get the warmest and coolest 
warmest_room_index = room_temperatures.index(warmest_temp)
coolest_room_index = room_temperatures.index(coolest_temp)

print(warmest_room_index, coolest_room_index)
warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]

print(f"The warmest room is {warmest_room} at this celsius {warmest_temp}")
print(f"The coolest room is {coolest_room} at this celsius {coolest_temp}")