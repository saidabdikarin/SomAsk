import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time

def draw_clock():
    now = datetime.datetime.now()
    fig, ax = plt.subplots()
    
    # Set up the clock face
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Hour marks
    for deg in range(0, 360, 30):
        ax.plot([0.9 * np.sin(np.deg2rad(deg)), np.sin(np.deg2rad(deg))],
                [0.9 * np.cos(np.deg2rad(deg)), np.cos(np.deg2rad(deg))], 'k')
    
    # Hour hand
    hour_angle = (now.hour % 12 + now.minute / 60) * 30
    ax.plot([0, 0.5 * np.sin(np.deg2rad(hour_angle))],
            [0, 0.5 * np.cos(np.deg2rad(hour_angle))], 'r', linewidth=6)
    
    # Minute hand
    minute_angle = now.minute * 6
    ax.plot([0, 0.7 * np.sin(np.deg2rad(minute_angle))],
            [0, 0.7 * np.cos(np.deg2rad(minute_angle))], 'b', linewidth=4)
    
    # Second hand
    second_angle = now.second * 6
    ax.plot([0, 0.9 * np.sin(np.deg2rad(second_angle))],
            [0, 0.9 * np.cos(np.deg2rad(second_angle))], 'g', linewidth=2)

    return fig

def main():
    st.title('Analog Clock')
    clock_placeholder = st.empty()
    
    while True:
        fig = draw_clock()
        clock_placeholder.pyplot(fig)
        time.sleep(1)  # Update the clock every second
        plt.close(fig)  # Close the plot to free up memory

if __name__ == "__main__":
    main()
