
    
import csv
from gremlin_python import statics
from gremlin_python import *
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier

graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin','g'))


def delete_all_data():
    # delete all the data in graph g
    g.V().drop().iterate()
   
    # Check if any data is there
    print(g.V().has('v_id','6').count().toList()[0])
    
def load_csv_data(filename ):

    # Load the csv file 
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        # toList to convert to python list
        # next required as g is an iterator 
        for row in csv_reader:
                 if g.V().has('v_id',row[0]).count().toList()[0] == 0:
                     #create the vertex if no vertex exists and add edge
                     u = g.addV().property('v_id',row[0]).next()
                 else:
                     u = g.V().has('v_id',row[0]).next()
    
                 if g.V().has('v_id',row[1]).count().toList()[0] == 0:
                     #create the vertex if no vertex exists and add edge
                     v = g.addV().property('v_id',row[1]).next()    
                 else:
                     v = g.V().has('v_id',row[1]).next()
    
                 #Add a new edge between u and v
                 g.V(u).addE('trust').to(__.V(v)).property('rating',row[2]).property('time',row[3]).next()
             
                 line_count += 1
                 print("Processed "+str(line_count)+" lines.")

def get_actors_worked_together(n):
    for actor in g.V().not_(__.hasLabel('Movie','Person::User','')):
        actor_name = g.V(actor).values("name").toList()[0]
        print("###########\n")
        print("actor name:"+actor_name)
        print("----------\n")
        dict_actors = g.V(actor).out().in_().groupCount().by('name').next()
        for key, value in dict_actors.items():
            if(value == n and key != actor_name):
                print(key +" : "+str(value))
        print("#############\n")

get_actors_worked_together(3)
