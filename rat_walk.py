from math import sqrt, pow


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
    def __str__(self):
        return f"{self.state} "

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node



class floor():
    def __init__(self, W, H , N, R, Xi ,Yi):
        self.height = H
        self.width = W
        self.no_of_holes = N
        self.radius = R
        self.sensor_locations = []
        
        self.resolution = 2

        for i in range(self.no_of_holes):
            self.sensor_locations.append(((Xi[i])*self.resolution-1, (Yi[i])*self.resolution-1))

        self.floor_map = []
        self.holes = [] 


        for y in range(self.height*self.resolution):
            row = []
            for x in range(self.width*self.resolution):
                if self.detect((x,y)):
                    row.append(False)
                else :
                    row.append(True)
            self.floor_map.append(row)

    def detect(self, A):
        x1, y1 = A
        min = max(self.width,self.height)*self.resolution
        for i in range(len(self.sensor_locations)):
            x2, y2 = self.sensor_locations[i]
            l = sqrt(pow((y1-y2),2) + pow((x1-x2),2))
            if l <= min:
                min = l
            #print(min, "::", l)
        return True if min <= self.radius else False


    def next_move(self, state):
        y, x = state
        candidates = [
            ("up", (x, y-1)),
            ("left", (x-1, y)),
            ("right", (x+1, y)),
            ("down", (x, y +1))
            
        ]

        result = []
        for action, (x, y) in candidates:
            if 0 <= x < (self.width*self.resolution)  and 1 <= y < (self.height*self.resolution) and self.floor_map[x][y]:
                result.append((action, (x, y)))
        #print("result: ", result)
        return result


    def print(self):
        print(self.sensor_locations)
        for line in self.floor_map:
            for i in line:
                print(i, end=" ")
            print("\n", end='')

    """def solve(self):
        # Keep track of number of states explored
        for i in range(len(self.floor_map[0])):
            if self.floor_map[0][i] == True:
                start = (i,0)
                self.num_explored = 0
                #print("Start: ", start)

                # Initialize frontier to just the starting position
                start = Node(state=start, parent=None, action=None)
                frontier = StackFrontier()
                frontier.add(start)

                # Initialize an empty explored set
                self.explored = set()

                # Keep looping until solution found
                count = 0
                while True:
                    #print(count)
                    count +=1
                    # If nothing left in frontier, then no path
                    if frontier.empty():
                        #print("break")
                        break

                    # Choose a node from the frontier
                    node = frontier.remove()
                    self.num_explored += 1

                    # Mark node as explored
                    self.explored.add(node.state)

                    # Add neighbors to frontier
                    #print("Node state : ", node.state)
                    for action, state in self.next_move(node.state):
                        #print(action,state)
                        if not frontier.contains_state(state) and state not in self.explored:
                            #print("Child added")
                            child = Node(state=state, parent=node, action=action)
                            x, y = child.state
                            if y == self.height*self.resolution - 1:
                                return "CAN"
                            frontier.add(child)"""    
    def solve(self):
        for i in range(len(self.floor_map[0])):
            if self.floor_map[0][i]:
                start = (i, 0)
                self.num_explored = 0
                start_node = Node(state=start, parent=None, action=None)
                frontier = StackFrontier()
                frontier.add(start_node)
                self.explored = set()
                while True:
                    if frontier.empty():
                        break
                    node = frontier.remove()
                    self.num_explored += 1
                    self.explored.add(node.state)
                    for action, state in self.next_move(node.state):
                        if not frontier.contains_state(state) and state not in self.explored:
                            child = Node(state=state, parent=node, action=action)
                            x, y = child.state
                            if y == self.height * self.resolution - 1:
                                return "CAN"
                            frontier.add(child)
        return "CAN'T"           



'''def main(W, H, N, R, Xi, Yi):
    Floor = floor(W, H, N, R, Xi, Yi)
    #Floor.print()
    print(Floor.solve())




if __name__ == "__main__":
    T , W , H = map(int, input().rstrip().split())
    cases = []
    for i in range(T):
        N , R = map(int, input().rstrip().split())
        Xi = list(map(int, input().rstrip().split()))
        Yi = list(map(int, input().rstrip().split()))
        cases.append([N,R,Xi,Yi])
    for j in cases:
        main(W, H, j[0], j[1], j[2], j[3])'''


def main(W, H, N, R, Xi, Yi):
    Floor = floor(W, H, N, R, Xi, Yi)
    print(Floor.solve())

if __name__ == "__main__":
    T, W, H = map(int, input().rstrip().split())
    cases = []
    for i in range(T):
        N, R = map(int, input().rstrip().split())
        Xi = list(map(int, input().rstrip().split()))
        Yi = list(map(int, input().rstrip().split()))
        cases.append([N, R, Xi, Yi])
    for j in cases:
        main(W, H, j[0], j[1], j[2], j[3])