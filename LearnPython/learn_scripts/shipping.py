#Shipping Cost Calculator

#Define global variables
weight = 41.5

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground shipping cost: $" + str(cost_ground))

#Premium Ground Shipping
cost_ground_p = 125
print("Premium Ground shipping cost: $" + str(cost_ground_p))

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.0
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.0
else:
  cost_drone = weight * 14.25
print("Drone shipping cost: $" + str(cost_drone))