        # Algorithm in Python for simulation carried out in SUMO (Simulation of Urban MObility)

import traci
import random
import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from shapely.geometry import Point
from geographiclib.geodesic import Geodesic

geod = Geodesic.WGS84
G = ox.graph_from_bbox(1.3763, 1.3007, 103.6492, 103.7840, network_type='drive')
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

projected_graph = ox.project_graph(G, to_crs="EPSG:3395")
Gc = ox.consolidate_intersections(projected_graph, dead_ends=True)
edges = ox.graph_to_gdfs(ox.get_undirected(Gc), nodes=False)

class IoVSecuritySystem:
    def __init__(self):
        self.sumoBinary = "sumo"
        self.configFile = "mySimulation.sumocfg"

    def collect_traffic_data(self):
        # Collecting vehicle traffic data from SUMO
        traffic_data = []
        currentTime = traci.simulation.getCurrentTime() / 1000  # In seconds
        traffic_data.append(currentTime)  # Add real logic here if needed
        return traffic_data

    def encrypt_data(self, raw_data):
        # Applying homomorphic encryption
        encrypted_data = []
        for value in raw_data:
            encrypted_value = value + random.random()
            encrypted_data.append(encrypted_value)
        return encrypted_data

    def detect_anomalies(self, encrypted_data):
        # Detecting anomalies in encrypted data
        for value in encrypted_data:
            if value < 0 or value > 50:
                return True  # Anomaly detected
        return False  # No anomalies detected

    def run_simulation(self):
        try:
            traci.start([self.sumoBinary, "-c", self.configFile])
            for step in range(1000):
                traci.simulationStep()

                traffic_data = self.collect_traffic_data()
                encrypted_data = self.encrypt_data(traffic_data)
                anomaly_detected = self.detect_anomalies(encrypted_data)

                if anomaly_detected:
                    print("Alert: Anomaly detected! Possible botnet intrusion attempt.")
                else:
                    print("No anomalies detected in vehicle network traffic data.")
                
                # Add OSMnx code to control vehicle movement
                animate(step)

            traci.close()
        except Exception as e:
            print("Error during simulation execution:", e)

def animate(i):
    # Iterate over all routes
    for j in range(n_routes):
        # Some routes are shorter than others
        # Therefore we need to use try except with continue construction
        try:
            # Try to plot a scatter plot
            x_j = route_coorindates[j][i][0]
            y_j = route_coorindates[j][i][1]
            scatter_list[j].set_offsets(np.c_[x_j, y_j])
        except:
            continue

if __name__ == "__main__":
    security_system = IoVSecuritySystem()
    
    vehnumber = 10
    routes = []
    route = []
    allAngleList = []
    direction = []
    all_route_roadnames = []
    all_route_speeds = []

    angleList = []
    direzione = []
    route_roadnames = []
    route_speed = []

    LEFT_SIG = ""
    STRAIGHT_SIG = ""
    RIGHT_SIG = ""

    columns = ['vehID', 'subroute', 'speed', 'turn', 'angle', 'lengthOfSubroute']
    data = []
    df = pd.DataFrame()

    for iroute in range(vehnumber):
        try:
            y0 = 0.0
            x0 = 0.0
            
            lat = round(random.uniform(1.3007, 1.3763), 5)
            lon = round(random.uniform(103.6492, 103.7840), 5)
            good_orig_node = ox.get_nearest_node(G, (lat, lon), method='euclidean')

            lat = round(random.uniform(1.3007, 1.3763), 5)
            lon = round(random.uniform(103.6492, 103.7840), 5)
            good_dest_node = ox.get_nearest_node(G, (lat, lon), method='euclidean')

            routep1 = nx.shortest_path(G, good_orig_node, good_dest_node)
            lengthOfRoute1 = nx.shortest_path_length(G, good_orig_node, good_dest_node, weight='length')

            lat = round(random.uniform(1.3007, 1.3763), 5)
            lon = round(random.uniform(103.6492, 103.7840), 5)
            next_dest_node = ox.get_nearest_node(G, (lat, lon), method='euclidean')

            routep2 = nx.shortest_path(G, good_dest_node, next_dest_node)
            lengthOfRoute2 = nx.shortest_path_length(G, good_dest_node, next_dest_node, weight='length')

            route = routep1 + routep2
            lengthOfRoute = lengthOfRoute1 + lengthOfRoute2
            
            lor = round(lengthOfRoute/1000.0, 2)
            
            angleList = []
            direzione = []
            route_roadnames = []
            route_speed = []

            ## iterate through roads (i.e. edges) in a route
            for irou in route:
                incident_edges = edges[(edges['u_original']==irou) | (edges['v_original']==irou)]
                for _, edge in incident_edges.fillna('').iterrows():
                    instantroad = edge['name']
                    instantspd = edge['speed_kph']
                    route_roadnames.append(edge['name'])
                    route_speed.append(edge['speed_kph'])
                    
                    latlat = G.nodes[irou]['y']
                    lonlon = G.nodes[irou]['x']

                    direzione.append("straight")
                    
                    TURN_SIG = "straight"
                    
                    turnAngle = geod.Inverse(latlat,lonlon,y0,x0)

                    if turnAngle['azi1'] > 45.0 and turnAngle['azi1'] < 135.0:
                        direzione.append("right")
                        TURN_SIG = "right"
                    if (turnAngle['azi1'] > -135.0 and turnAngle['azi1'] < -45.0):
                        direzione.append("left")
                        TURN_SIG = "left"
                    
                    y0 = latlat
                    x0 = lonlon
                    
                    angleList.append(turnAngle['azi1'])

                    values = [iroute, instantroad, instantspd, TURN_SIG, turnAngle['azi1'], edge.get('length', None)]
                    zipped = zip(columns, values)
                    a_dictionary = dict(zipped)
                    data.append(a_dictionary)

                df = df.append(data, True)
                
                my_dict = {i:round(direzione.count(i)/len(direzione)*100.0,1) for i in direzione}
                print("vehID: ", iroute, " Total route length: ", lor, " km. ", "TurnRatio: ", my_dict)

        except:
            pass

        routes.append(route)
        allAngleList.append(angleList)
        direction.append(direzione)
        all_route_roadnames.append(route_roadnames)
        all_route_speeds.append(route_speed)

    route_coorindates = []

    for rou in routes:
        points = []
        for node_id in rou:
            x = projected_graph.nodes[node_id]['x']
            y = projected_graph.nodes[node_id]['y']
            points.append([x, y])

        route_coorindates.append(points)

    n_routes = len(route_coorindates)

    print("No. of Vehicles/Routes: ", len(routes))
    print("Extracted routes: ", n_routes)
    max_route_len = max([len(x) for x in route_coorindates])

    fig, ax = ox.plot_graph(projected_graph, node_size=0, edge_linewidth=1.5, edge_color='#2C2E2C', show=False, close=False, bgcolor='#12830E')

    scatter_list = []

    # Plot the first scatter plot (starting nodes = initial car locations)
    for j in range(n_routes):
        scatter_list.append(ax.scatter(route_coorindates[j][0][0], route_coorindates[j][0][1], label=f'car {j}', alpha=.75))

    line_ani = animation.FuncAnimation(fig, animate, interval=1)

    security_system.run_simulation()
