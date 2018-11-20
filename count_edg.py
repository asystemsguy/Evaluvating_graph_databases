
    
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
    # delete all the data in graph 
    #g.V().drop().iterate()
   
    # Check if any data is there
    print(g.V().has('v_id','6').count().toList()[0])

def count_edges():
    i =  g.E().count().next()
    print(i)
    
#get_actors_worked_together(3)
count_edges()
