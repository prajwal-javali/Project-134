import csv
import plotly.express as pe

rows = []

with open ("data.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        rows.append(row)


headers = rows[0]
planet_data_rows = rows[1:]

# print(headers)
# print(planet_data_rows[0])


headers[0] = "row_num" 


solar_system_planet_count = {}

for planet_data in planet_data_rows:
    if solar_system_planet_count.get(planet_data[11]) :
        solar_system_planet_count[planet_data[11]] += 1
    else:
        solar_system_planet_count[planet_data[11]] = 1

max_ss = max(solar_system_planet_count, key = solar_system_planet_count.get) 

print("The solar system " , max_ss , ", has maximun planets -" , solar_system_planet_count[max_ss]) 


temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[3]
    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
        planet_data[3] = planet_mass_value

    planet_radius = planet_data[7]
    if planet_radius.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
    if planet_radius_ref == "Jupiter":
        planet_radius_value = float(planet_radius_value) * 11.2
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))


# 19.4 Jupiters

# 1.08 x Jupiter

# ---------------------------------------------------- c 132 ----------------------------------------------------------

hd_10180_planets = []
for planet_data in planet_data_rows:
  if max_ss == planet_data[11]:
    hd_10180_planets.append(planet_data)

print(len(hd_10180_planets))
print(hd_10180_planets)


hd_10180_planet_masses = []

hd_10180_planet_names = []

for p in hd_10180_planets:
    hd_10180_planet_masses.append(p[3])     
    hd_10180_planet_names.append(p[1])     


hd_10180_planet_masses.append(1)
hd_10180_planet_names.append(['earth'])     

fig = pe.bar(x=hd_10180_planet_names , y=hd_10180_planet_masses)
# fig.show()


# The Value of G (Gravitational Constant) is 6.674e-11

# Mass of Earth = 5.972e+24

# Radius of Earth = 6371000


temp_planet_data_rows = list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []

planet_radius = []

planet_names = []

for p in planet_data_rows:
    planet_masses.append(p[3])
    planet_radius.append(p[7])
    planet_names.append(p[1])

planet_gravity = []
for index, name in enumerate(planet_names):
    # g = G + MassofEarth/radius*radius
    gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radius[index])*float(planet_radius[index])*6371000*6371000) * 6.674e-11
    planet_gravity.append(gravity)

fig = pe.scatter(x=planet_radius, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
# fig.show()

low_gravity_planets = []

for index , gravity in enumerate(planet_gravity):
    if gravity < 100:
        low_gravity_planets.append(planet_data_rows[index])
    
print(len(low_gravity_planets))

planet_type_values = []
for planet_data in planet_data_rows:
  planet_type_values.append(planet_data[6])

print(list(set(planet_type_values)))


# ----------------------------------------------- c133 ------------------------------------------------

planet_mass = []
planet_radius = []

for i in low_gravity_planets:
    planet_mass.append(i[3]) 
    planet_radius.append(i[7]) 


fig = pe.scatter(x=planet_radius, y=planet_mass)
fig.show()


planet_mass = []
planet_radius = []
planet_type = [] 

for i in low_gravity_planets:
    planet_mass.append(i[3]) 
    planet_radius.append(i[7]) 
    planet_type.append(i[6])


fig = pe.scatter(x=planet_radius, y=planet_mass , color = planet_type)
fig.show()


suitable_planets = []

for i in low_gravity_planets:
    if i[6].lower()=="terrestrial" or  i[6].lower()=="super earth":
        suitable_planets.append(i) 

print(len(suitable_planets))

# ----------------------------------------------------------------------------------------
# ["9 years"] --> ["9" , "years"]

temp_suitable_planets = list(suitable_planets)
for planet_data in temp_suitable_planets:
  if planet_data[8].lower() == "unknown":
    suitable_planets.remove(planet_data)

for planet_data in suitable_planets:
  if planet_data[9].split(" ")[1].lower() == "days":
    planet_data[9] = float(planet_data[9].split(" ")[0]) #Days
  else:
    planet_data[9] = float(planet_data[9].split(" ")[0])*365 #Years
  planet_data[8] = float(planet_data[8].split(" ")[0])

orbital_radiuses = []
orbital_periods = []
for planet_data in suitable_planets:
  orbital_radiuses.append(planet_data[8])
  orbital_periods.append(planet_data[9])

fig = pe.scatter(x=orbital_radiuses, y=orbital_periods)
fig.show()

# ------------------------------------------------------------------------------------------------------------------------------------------
planet_masses = []
planet_radiuses = []
planet_types = []

for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_types.append(planet_data[6])


fig = pe.scatter(x=planet_radiuses, y=planet_masses, color=planet_types)
fig.show()

# --------------------------------------------------------- c134 --------------------------------------------------------------

goldilock_planets = list(suitable_planets)

temp_goldilock_planets = list(suitable_planets) 
for planet_data in temp_goldilock_planets:
  if planet_data[8] < 0.38 or planet_data[8] > 2:
    goldilock_planets.remove(planet_data)

print(len(suitable_planets))
print(len(goldilock_planets))


# ----------------------------------------------------------------------------
planet_speed = []

for i in suitable_planets:
  distance = 2 * 3.14 * (planet_data[8] * 1.496e+9)
  time = planet_data[9] * 86400
  speed = distance / time
  planet_speed.append(speed)

speed_supporting_planets = list(suitable_planets)


temp_speed_supporting_planets = list(suitable_planets)
for index, planet_data in enumerate(temp_speed_supporting_planets):
  if planet_speed[index] > 200:
    speed_supporting_planets.remove(planet_data)

print(len(speed_supporting_planets))

# Mercury - 3.7m/s
# Venus - 8.87m/s
# Earth - 9.8m/s
# Mars - 3.8m/s

# Mercury - 0.4AU
# Venus - 0.7AU
# Earth - 1AU
# Mars - 1.5AU

goldilock_planets = list(suitable_planets) #We will leave suitable planet list as it is

temp_goldilock_planets = list(suitable_planets) 
for planet_data in temp_goldilock_planets:
  if planet_data[8] < 0.38 or planet_data[8] > 2:
    goldilock_planets.remove(planet_data)

print(len(suitable_planets))
print(len(goldilock_planets))


planet_speeds = []
for planet_data in suitable_planets:
  distance = 2 * 3.14 * (planet_data[8] * 1.496e+9)
  time = planet_data[9] * 86400
  speed = distance / time
  planet_speeds.append(speed)

speed_supporting_planets = list(suitable_planets) #We will leave suitable planet list as it is

temp_speed_supporting_planets = list(suitable_planets)
for index, planet_data in enumerate(temp_speed_supporting_planets):
  if planet_speeds[index] > 200:
    speed_supporting_planets.remove(planet_data)

print(len(speed_supporting_planets))


# ---------------------------------------------------------------------------

habitable_planets = []
for planet in speed_supporting_planets:
  if planet in goldilock_planets:
    habitable_planets.append(planet)

print("---------------------------------------")
print(len(habitable_planets))

# ---------------------------------------------------------------------------

final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
  features_list = []
  gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
  except: pass
  try:
    if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
      features_list.append("planet_type")
  except: pass
  try:
    if planet_data[8] > 0.38 or planet_data[8] < 2:
      features_list.append("goldilock")
  except: pass
  try:
    distance = 2 * 3.14 * (planet_data[8] * 1.496e+9)
    time = planet_data[9] * 86400
    speed = distance / time
    if speed < 200:
      features_list.append("speed")
  except: pass
  final_dict[index] = features_list

print("---------------------------------------")
# print(final_dict)

# --------------------------------------------------------------
gravity_planet_count = 0
for key, value in final_dict.items():
  if "gravity" in value:
    gravity_planet_count += 1

print("---------------------------------------")
print(gravity_planet_count)

# --------------------------------------------------------------

type_planet_count = 0

for i,value in final_dict.items():
  if "planet_type"  in value:
    type_planet_count += 1


print("---------------------------------------")
print(type_planet_count)

# ----------------------------------------------------------------------------------------
planet_not_gravity_support = []
for planet_data in planet_data_rows:
  if planet_data not in low_gravity_planets:
    planet_not_gravity_support.append(planet_data)

type_no_gravity_planet_count = 0
for planet_data in planet_not_gravity_support:
  if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
    type_no_gravity_planet_count += 1

print("---------------------------------------")
print(type_no_gravity_planet_count)
print(type_planet_count - type_no_gravity_planet_count)


# --------------------------------------------------------------

goldilock_planet_count = 0

for i,value in final_dict.items():
  if "goldilock"  in value:
    goldilock_planet_count += 1


print("---------------------------------------")
print(goldilock_planet_count)



# --------------------------------------------------------------

speed_planet_count = 0

for i,value in final_dict.items():
  if "speed"  in value:
    speed_planet_count += 1


print("---------------------------------------")
print(speed_planet_count)












# speed_planet_count = 0
# for key, value in final_dict.items():
#   if "speed" in value:
#     speed_planet_count += 1

# print("---------------------------------------")
# print(speed_planet_count)













