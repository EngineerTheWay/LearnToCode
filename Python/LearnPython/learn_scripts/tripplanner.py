def trip_planner_welcome(name):
  print("Welcome to TripPlanner v1.0", name + "!")
trip_planner_welcome("Caleb")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(7)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in", origin, "and you are traveling to", destination + ".", "You will be traveling by", mode_of_transport + ".", "It will take approximately", str(estimated_time), "hours.")

destination_setup("Atlanta", "Athens", estimate, "Plane")

#Output
# Welcome to TripPlanner v1.0 Caleb!
# Your trip starts off in Atlanta and you are traveling to Athens. You will be traveling by Plane. It will take approximately 7 hours.