import tkinter as tk
import math

# Parameters
planet_names = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
orbit_radii = [
    60,
    85,
    110,
    135,
    175,
    215,
    255,
    295,
]
orbital_speeds = [
    0.047,
    0.035,
    0.030,
    0.024,
    0.013,
    0.009,
    0.006,
    0.005,
]


planet_colors = [
    "grey",  # Mercury
    "orange",  # Venus
    "blue",  # Earth
    "red",  # Mars
    "brown",  # Jupiter
    "grey",  # Saturn
    "lightblue",  # Uranus
    "darkblue",  # Neptune
]

# Window setup
root = tk.Tk()
root.title("Solar System Animation")
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

# Drawing the Sun
center_x, center_y = 400, 300
canvas.create_oval(
    center_x - 20, center_y - 20, center_x + 20, center_y + 20, fill="yellow"
)

# Drawing orbits
for radius in orbit_radii:
    canvas.create_oval(
        center_x - radius,
        center_y - radius,
        center_x + radius,
        center_y + radius,
        outline="gray",
    )

# Initializing planets
planets = []
for i, name in enumerate(planet_names):
    x = center_x + orbit_radii[i] * math.cos(0)
    y = center_y + orbit_radii[i] * math.sin(0)
    planet = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=planet_colors[i])
    planets.append(
        (planet, 0)
    )  # stores the planet object and its current angular position


# Function to update the position of planets
def update():
    for i, (planet, theta) in enumerate(planets):
        x = center_x + orbit_radii[i] * math.cos(theta)
        y = center_y + orbit_radii[i] * math.sin(theta)
        canvas.coords(planet, x - 5, y - 5, x + 5, y + 5)
        planets[i] = (planet, theta + orbital_speeds[i])
    root.after(50, update)


update()

root.mainloop()
