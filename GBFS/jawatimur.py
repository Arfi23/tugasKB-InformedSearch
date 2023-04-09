
import heapq
map = {}


class PriorityQueue:
    def __init__(self) -> None:
        self.cities = []

    def isEmpty(self):
        if self.cities == []:
            return True
        return False

    def check(self):
        print(self.cities)

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    
    def pop(self):
        return heapq.heappop(self.cities)[1]


class CityNode:
  def __init__(self, city, distance) -> None:
    self.city = str(city)
    self.distance = str(distance)

def makeDict():
    file = open("Jalan.txt", 'r')
    for str in file:
        delimeter = str.split(',')
        city1 = delimeter[0]
        city2 = delimeter[1]
        dist = delimeter[2]
        map.setdefault(city1, []).append(CityNode(city2, dist))
        map.setdefault(city2, []).append(CityNode(city1, dist))
        
   
def makeHeuristicDict():
    h = {}
    file = open("Heuristic.txt", 'r')
    for str in file:
        delimeter = str.strip().split(',')
        node = delimeter[0].strip()
        sld  = int(delimeter[1].strip())
        h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

def greedyBFS(start, end):

    path = {}
    q = PriorityQueue()
    h = makeHeuristicDict()

    q.push(start, 0)
    path[start] = None
    expandList = []

    while q.isEmpty() == False:
        curr = q.pop()
        expandList.append(curr)

        if curr == end:
            break
        
        for new in map[curr]:
            if new.city not in path:
                f_cost = heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = curr

    printOutputgBFS(start, end, path, expandList)

def printOutputgBFS(start, end, path, expandList):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("kota yang dilewati (GBFS) : "  + str(finalpath))
 

def printOutputAstar(start, end, path, distance):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("kota yang dilewati (A star) : " + str(finalpath))
    print("Total Jarak yang ditempuh \t\t: " + str(distance[end]))

def main():
    src = "Magetan"
    dst = "Surabaya"
    makeDict()
    print("Magetan => Surabaya")
    # aStar(src, dst)
    greedyBFS(src, dst)


if __name__ == "__main__":
    main()

