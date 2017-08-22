import networkx as nx

class WebGraph:

	def __init__(self):
		self.digraph = nx.DiGraph()


	def add_node(self, page):
		self.digraph.add_node(page)

	def add_edge(self, pair):
		pass

webGraph = WebGraph()



