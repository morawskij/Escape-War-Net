import matplotlib.pyplot as plt
from queue import PriorityQueue
import math

directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

class Node:
    def __init__(self, x, y, walkable=True):
        self.x = x
        self.y = y
        self.walkable = walkable
        self.f_score = 0
        self.parent = None  #to track path

    def __lt__(self, other):
        return self.f_score < other.f_score

class Grid:
    def __init__(self):
        self.n = 100 #squares vertically 
        self.m = 100 #squares horizontally
        
        #alternatively max and min coordinates that the grid is covering 
        #and also size of each square
        #then just create grid depending on those parameters    
        self.coordinate_min_x=0
        self.coordinate_max_x=100
        self.coordinate_min_y=0
        self.coordinate_max_y=100
        """
        self.coordinate_size_y = self.coordinate_max_y-self.coordinate_min_y
        self_coordinate_x=self.coordinate_max_x-self.coordinate_min_x
        self.node_size = 
        self.size_x = self.coordinate_size_x/self.node_size
        self.size_y = self.coordinate_size_x/self.node_size

        """
        self.matrix = [[Node(i,j) for i in range(self.n)] for j in range(self.m)]
        self.matrix[10][0].walkable=False
        self.matrix[10][1].walkable=False
        self.matrix[10][2].walkable=False
        self.matrix[10][3].walkable=False
        self.matrix[10][4].walkable=False
        self.matrix[10][5].walkable=False
        self.matrix[10][6].walkable=False
        self.matrix[10][7].walkable=False
        self.matrix[10][8].walkable=False
        self.matrix[10][9].walkable=False
        self.matrix[10][10].walkable=False
        self.matrix[10][11].walkable=False
        self.matrix[10][12].walkable=False
        self.matrix[10][13].walkable=False

    def visualize(self):
        for i in range(self.n):
            for j in range(self.m):
                node = self.matrix[i][j]
                color = 'black' if not node.walkable else 'blue'
                plt.gca().add_patch(plt.Rectangle((i, j), 1, 1, color=color))
        plt.xlim(0, self.n)
        plt.ylim(0, self.m)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.show()

 

    def convert_coordinates_to_node(self,x,y):
        pass
    
    def get_possible_moves(self, v):
        res = []
        (x_v,y_v) = (v.x,v.y)
        for (x,y) in directions:
            if x+x_v >self.coordinate_min_x and x+x_v<self.coordinate_max_x and y+y_v>self.coordinate_min_y and y+y_v<self.coordinate_max_y:
                res.append((x+x_v,y+y_v)) ##or should matrix[x+x_v][y+y_v]
        return res
    
    def heura(self, v,u):
        (x_u,y_u) = u 
        (x_v,y_v) = v 
        return math.sqrt((x_v-x_u)*(x_v-x_u) + (y_u-y_v)*(y_u-y_v))

   

    def search(self, start, end):
        q = PriorityQueue()
        start.f_score = self.heura((start.x, start.y), (end.x, end.y))
        q.put(start)

        checked = set()

        while not q.empty():
            curr_cheapest = q.get()
          #  print(f'{curr_cheapest.x},{curr_cheapest.y}')
            if curr_cheapest == end:
                path = self.reconstruct_path(curr_cheapest)
                return path

            checked.add(curr_cheapest)

            for neigh_x, neigh_y in self.get_possible_moves(curr_cheapest):
                neigh = self.matrix[neigh_y][neigh_x]
                if not neigh.walkable or neigh in checked:
                    continue

                h_score = self.heura((neigh.x, neigh.y), (end.x, end.y))
                f_score = curr_cheapest.f_score + h_score

                if (f_score, neigh) not in q.queue: 
                    neigh.f_score = f_score
                    neigh.parent=curr_cheapest
                    q.put(neigh)

        return None  

    def reconstruct_path(self, node):
        path = []
        while node is not None:
            path.append((node.x, node.y))
            node = node.parent
        return path
    
def visualize_path(grid, path):
        for i in range(grid.n):
            for j in range(grid.m):
                node = grid.matrix[j][i]
                color = 'black' if not node.walkable else 'blue'
                plt.gca().add_patch(plt.Rectangle((i, j), 1, 1, color=color))
        
        for x, y in path:
            plt.plot(x + 0.5, y+0.5,marker='o',color='red')

        plt.xlim(0,grid.n)
        plt.ylim(0, grid.m)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.show()
grid = Grid()

start = grid.matrix[3][3]
end = grid.matrix[21][4]

path = grid.search(start, end)
print(path)

path = grid.search(start, end)
if path:
    visualize_path(grid,path)
else:
    print("No track :(")