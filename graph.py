from enum import Enum
class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

from collections import OrderedDict
class Node:
    def __init__(self,num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()
        # key = node, val = weight
    def __str__(self):
        return str(self.num)

class Graph:
    def __init__(self):
        self.nodes = OrderedDict() #key = node_id, val = node
    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node
    def add_edge(self,source,dest,weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return f'{str(self.id)} connectedTo: {str([x.id for x in self.connectedTo])}'

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class GraphVertex:
    def __init__(self):
        self.vertList = {}
        self.numVertices=0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs1(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited


def dfs2(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start]-visited:
        dfs2(graph,nxt,visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path+[nxt]))

def bfs(graph,start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start,[start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next,path+[next]))

def shortest_path(graph,start,goal):
    try:
        return next(bfs_paths(graph,start,goal))
    except StopIteration:
        return None