import streamlit as st
import matplotlib.pyplot as plt
import datetime
import numpy as np

def draw_hand(ax, position, length, width, color):
    """Draws a hand on the plot."""
    x = [0, length * np.sin(np.deg2rad(position))]
    y = [0, length * np.cos(np.deg2rad(position))]
    ax.plot(x, y, color=color, lw=width)

def setup_circle(ax, radius, labels_count, label):
    """Creates circles with labels for days, months, or years."""
    circle = plt.Circle((0, 0), radius, fill=False, color='black', linewidth=1.5)
    ax.add_patch(circle)

    # Add labels
    for i in range(1, labels_count + 1):
        angle = 360 / labels_count * (i - 1)
        x = (radius + 10) * np.sin(np.deg2rad(angle))
        y = (radius + 10) * np.cos(np.deg2rad(angle))
        ax.text(x, y, str(i), ha='center', va='center')

def draw_date_analog():
    today = datetime.datetime.now()
    day = today.day
    month = today.month
    year = int(str(today.year)[-2:])  # Last two digits of the year

    fig, ax = plt.subplots()

    # Set up plot limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(-250, 250)
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw day, month, year circles
    setup_circle(ax, 100, 31, "Day")
    setup_circle(ax, 150, 12, "Month")
    setup_circle(ax, 200, 100, "Year")

    # Draw hands
    draw_hand(ax, 360 / 31 * (day - 1), 100, 4, 'blue')
    draw_hand(ax, 360 / 12 * (month - 1), 150, 6, 'green')
    draw_hand(ax, 360 / 100 * (year - 1), 200, 8, 'red')

    st.pyplot(fig)

st.title('Analog Date Clock')
draw_date_analog()
