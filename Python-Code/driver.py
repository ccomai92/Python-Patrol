from map import Map 
#import visualize

m = Map()
def update():
    for car in m.car_map:
        car.update()
"""
Start the clock
"""
print("finish constructing map")
ts = 0

# check this one 
while m.car_map[0].current_position != m.car_map[0].destination:
    m.car_map[0].update()
    #visualize.drawMap(m.node_map, m.edge_map)
    ts+=1

print("time", ts)

    






    
