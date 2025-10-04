import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Box dimensions
box_width = 10
box_height = 10

# Ball properties
ball_radius = 0.2
position = np.array([5.0, 5.0])  # Starting in the center
velocity = np.array([0.1, 0.15])  # Initial speed

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, box_width)
ax.set_ylim(0, box_height)
ball, = ax.plot([], [], 'o', markersize=20)

def init():
    ball.set_data(position[0], position[1])
    return ball,

def update(frame):
    global position, velocity

    # Update position
    position += velocity

    # Bounce off the walls
    if position[0] - ball_radius <= 0 or position[0] + ball_radius >= box_width:
        velocity[0] *= -1
    if position[1] - ball_radius <= 0 or position[1] + ball_radius >= box_height:
        velocity[1] *= -1

    ball.set_data(position[0], position[1])
    return ball,

# Create animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=300, interval=20, blit=True)

plt.title("Bouncing Ball Simulation")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
