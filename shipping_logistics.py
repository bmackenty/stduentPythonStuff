import os
import random
from ports import port_names
os.system("clear")

# Today, our fleet of around 740 ships call 343 ports and terminals in 121 
# countries; on average, a Maersk container ship call a port every six minutes – 
# somewhere in the world. Moving world trade, from end to end, 24/7. On any given day, 
# four Maersk vessels transit the Suez Canal, moving goods to the world market

ships = 740
ports = 343

class ship():
    def __init__(self, ship, port):
        self.ship = ship
        self.port = port
        self.status = 'Active'
        self.location = 'At sea'
        self.destination = 'Unknown'
        self.cargo = []
        self.cargo_mass = 0
        
    def move_ship(self, location, destination):
        self.location = location
        self.destination = destination
        print(f'{self.ship} is moving from {self.location} to {self.destination}')


class port():
    def __init__(self, port, origin_x, origin_y):
        self.port = port
        self.status = 'Active'
        self.ships = []
        self.origin_x = origin_x
        self.origin_y = origin_y

class shipping_request():
    def __init__(self, destination, origin, cargo_mass):
        self.destination = destination
        self.origin = origin
        self.cargo_mass = cargo_mass
        self.status = 'Pending'

def calculate_distance(port1, port2):
    x1 = port1.origin_x
    y1 = port1.origin_y
    x2 = port2.origin_x
    y2 = port2.origin_y
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance



# this creates a list of port objects
ports = [] 
for i in port_names:
    port1 = port(i[1], float(i[2]), float(i[3]))
    ports.append(port1)

print(f'{len(ports)} ports created')
print(ports[0].port, ports[0].origin_x, ports[0].origin_y)
