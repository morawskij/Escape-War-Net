import matplotlib.pyplot as plt
from queue import PriorityQueue
import math


#without saving f_score

directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))



class Node:
    def __init__(self, x, y, attribute=1):
        self.x = x
        self.y = y
        self.walkable = attribute #0-blocked 1-standard 2-shalter
        self.g_score = 0 #real cost
        self.parent = None  #to track path

    def __lt__(self, other):
        return self.g_score < other.g_score

class Grid:
    def __init__(self):
        self.coordinate_min_x=0
        self.coordinate_max_x=80
        self.coordinate_min_y=0
        self.coordinate_max_y=50
        self.node_size = 0.5

        self.coordinate_size_y = self.coordinate_max_y-self.coordinate_min_y
        self.coordinate_size_x=self.coordinate_max_x-self.coordinate_min_x

        self.size_x = int(self.coordinate_size_x/self.node_size) +1
        self.size_y = int(self.coordinate_size_y/self.node_size) +1

        self.matrix = [[None for _ in range(self.size_y)] for _ in range(self.size_x)]
        for i in range (self.size_x):
            for j in range (self.size_y):
                self.matrix[i][j]=Node(self.coordinate_min_x+i*self.node_size,self.coordinate_min_y+j*self.node_size)
        
    def visualize(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                node = self.matrix[i][j]
                color = 'red' if not node.walkable else 'blue'
                plt.gca().add_patch(plt.Rectangle((i, j), 0.5, 0.5, color=color))
        plt.xlim(0, self.size_x)
        plt.ylim(0, self.size_y)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.show()

    def convert_coordinates_to_node(self,x,y): ##TODO edge cases (x >self.x_max etc)
        temp_x = x/self.node_size 
        rest_x=x-temp_x*self.node_size
        res_x = int((x-rest_x)/self.node_size)

        temp_y = y/self.node_size
        rest_y=y-temp_y*self.node_size
        res_y = int((y-rest_y)/self.node_size)

        return (res_x,res_y)

    def get_possible_moves(self, v):
        res = []
        (x_v,y_v) = self.convert_coordinates_to_node(v.x,v.y)
        for (x,y) in directions:
            if x+x_v >=0 and x+x_v<self.size_x and y+y_v>=0 and y+y_v<self.size_y:
                res.append(self.matrix[x+x_v][y+y_v]) ##or should matrix[x+x_v][y+y_v]
        return res
    
    def heura(self, v,u):
        return math.sqrt((v.x - u.x)*(v.x - u.x) + (v.y - u.y)*(v.y - u.y))

   
    def search(self, start, end):
        q = PriorityQueue()
        start.g_score = 0

        q.put((self.heura(start,end),start))
        checked = set()

        while not q.empty():
            (temp,curr_cheapest) = q.get()
            if curr_cheapest==end:
                path = self.reconstruct_path(curr_cheapest)
                return path

            checked.add(curr_cheapest)
            for neigh in self.get_possible_moves(curr_cheapest):
                if not neigh.walkable or neigh in checked: 
                    continue

                h_score = self.heura(neigh, end)
                g_score = curr_cheapest.g_score  +self.heura(curr_cheapest,neigh)##math.sqrt(self.node_size*self.node_size)
                f_score = g_score+ h_score
               
                if neigh not in checked or f_score < neigh.g_score:
                    neigh.g_score = g_score
                    neigh.parent = curr_cheapest##change
                    if neigh not in q.queue:
                      q.put((f_score,neigh))
            
        return None  

    def reconstruct_path(self, node):
        path = []
        while node is not None:
            path.append((node.x, node.y))
            node = node.parent
        return path
    
def visualize_path(grid, path):
        for i in range(grid.size_x):
            for j in range(grid.size_y):
                node = grid.matrix[i][j]
                color = 'blue' if not node.walkable else 'red'
                plt.gca().add_patch(plt.Rectangle((i, j), 1, 1, color=color))
        for x, y in path:
            plt.plot(x + 0.5, y+0.5,marker='o',color='black')
        plt.show()


grid = Grid()
start = grid.matrix[4][12]
end = grid.matrix[9][25]

path = grid.search(start, end)
if path:
    visualize_path(grid,path)
else:
    print("No track :(")
