import argparse 
import pandas as pd
import matplotlib.pyplot as plt
import random as rdm
import numpy as np
trail = pd.DataFrame()
trail_matriz = []
data_list = []
plot_list = []
x_list = []
y_list = []
parser = argparse.ArgumentParser(description='random way point mobility model')

parser.add_argument('side_size', type=int, help='side length in meters' )
parser.add_argument('nodes_amount', type=int, help='nodes amount for this simulation')
parser.add_argument('time', type=int, help='duration of this simulation in seconds')
parser.add_argument('speed', type=int, help='nodes moviment speed in meters per second (m/s)')
parser.add_argument('randomness', type=int, help='moviment randomness in a scale of 1 - 10')
args = parser.parse_args()

moves = args.time // args.speed
args.side_size += 1
for i in range(args.nodes_amount -1, -1, -1):
    time_count = args.time
    while True:
        x = rdm.randrange(0, args.side_size)
        y = rdm.randrange(0, args.side_size)
        step = ((x**2)+(y**2)) ** (1/2)
        step_time = step / args.speed
        time_count -= step_time
        remaining = moves - step
        pause_time = 
        if time_count < 0:
            break
        move_dicionary = {'id':i+1, 'time' : time_count, 'x' : x, 'y' : y}
        data_list = [i, time_count, x, y]
        trail_matriz.append(data_list)
        trail = pd.concat([pd.DataFrame([move_dicionary]), trail])
    x0 = rdm.randrange(0, args.side_size)
    y0 = rdm.randrange(0, args.side_size)
    start_position= {'id':i+1, 'time' : '0.0', 'x' : x0, 'y' : y0}
    trail = pd.concat([pd.DataFrame([start_position]), trail])

print(trail)

for i in range(1, args.nodes_amount + 1):
    id_df = trail.loc[trail['id'] == i]
    print(id_df)
    plt.plot(id_df['x'], id_df['y'])
    plt.title(i)
    plt.show()
    