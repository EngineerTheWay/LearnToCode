# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Far to Cel
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

# Cel to Far
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Calculate Force
def get_force(mass, acceleration):
  return mass * acceleration

# Calculate Force of the theoretical train
train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies", train_force, "Newtons of force.")

# Get energy of a theoretical bomb
def get_energy(mass, c=3*10**8):
  return mass * c

bomb_energy = get_energy(bomb_mass)
print("A 1kb bomb supplies", bomb_energy, "Joules.")

# Calculate Work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

# Calculate work of the train
train_work = get_work(train_mass, train_acceleration, train_distance)

# Output for the train work calculation
print("The GE train does", str(train_work), "Joules of work over", str(train_distance), "meters.")



