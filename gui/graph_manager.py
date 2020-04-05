from graph import graph
from graph.graph_exception import GraphException
import random

from gui import node_widget


class GraphManager:

    def __init__(self, isDirected, mainViewWidget):
        self.mainViewWidget = mainViewWidget
        self.graph = graph.Graph(isDirected)
        self.nodeWidgets = []
        self.isDirected = isDirected

    def parse_graph_data(self, data):
        """Data is a string in the format "node_1_Id node_2_Id" which holds all the necessary data for creating the graph."""

        edges = data.split()
        self.graph = graph.Graph(self.isDirected)
        self.nodeWidgets = []

        for source, dest in zip(edges[0::2], edges[1::2]):  # data[0::2] creates subset collection of elements with (index % 2 == 0)
                                                            # zip(x,y) creates a tuple collection
            try:
                source = int(source)
            except:
                raise GraphException('The source node id must be a positive integer.')
            try:
                dest = int(dest)
            except:
                raise GraphException('The dest node id must be a positive integer.')

            self.graph.addNode(source)
            # (random.randrange(30, 200), random.randrange(30, 200))
            node_widget.maxid += 1
            self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(node_widget.maxid, [random.randrange(30, 200), random.randrange(30, 200)]))
            self.graph.addNeighbourNode(source, dest)

        self.graph.printGraph()

    def addNodeFromDrawing(self, node):
        self.nodeWidgets.append(node)