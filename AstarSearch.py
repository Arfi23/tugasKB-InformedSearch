import heapq

# print("hello dunia")


# class untuk priority queue, berisikan beberapa fungsi yang diperlukan
class priorityQueue:
    def __init__(self):
        self.perkotaan = []
    def push(self, kota, cost):
        heapq.heappush(self.perkotaan, (cost, kota))
    def pop(self):
        return heapq.heappop(self.perkotaan)[1]
    def isEmpty(self):
        if(self.perkotaan == []):
            return True
        else:
            return False

# class node untuk kota
class kotaNode:
    def __init__(self, kota, jarak):
        self.kota = str(kota)
        self.jarak = str(jarak)

# dictionary untuk menampung semua jalur antarkota di Jawa Timur (peta)
jtm = {}

def petajtm():
    content = """Magetan,Ngawi,32
Magetan,Madiun,22
Magetan,Ponorogo,34
Ngawi,Bojonegoro,44
Ngawi,Madiun,30
Ponorogo,Madiun,29
Madiun,Nganjuk,48
Bojonegoro,Nganjuk,33
Nganjuk,Jombang,40
Bojonegoro,Jombang,70
Bojonegoro,Lamongan,42
Jombang,Surabaya,72
Lamongan,Gresik,14
Gresik,Surabaya,12
Surabaya,Sidoarjo,25
Surabaya,Bangkalan,44
Sidoarjo,Probolinggo,78
Bangkalan,Sampang,52
Sampang,Pamekasan,31
Pamekasan,Sumenep,54
Probolinggo,Situbondo,99"""

    for string in content.split('\n'):
        line = string.split(',')
        ktfrom = line[0]
        ktto = line[1]
        jar = int(line[2])
        jtm.setdefault(ktfrom,[]).append(kotaNode(ktto,jar))
        jtm.setdefault(ktto,[]).append(kotaNode(ktfrom,jar))

# dictionary untuk menampung semua nilai heuristik kota di Jawa Timur
def hdict():
    h = {"Magetan": 162, "Surabaya": 0, "Ngawi": 130, "Ponorogo": 128,
         "Madiun": 126, "Bojonegoro": 60, "Nganjuk": 70, "Jombang": 36,
         "Lamongan": 36, "Gresik": 12, "Sidoarjo": 22, "Probolinggo": 70,
         "Situbondo": 146, "Bangkalan": 140, "Sampang": 90, "Pamekasan": 104, 
         "Sumenep": 150}
    return h

def heuristic(node, values):
    return values[node]

# fungsi pencarian A*
def Astar(start,goal):
    jalan = {}
    jarak = {}
    q = priorityQueue()
    h = hdict()
    q.push(start, 0)
    jarak[start] = 0
    jalan[start] = None
    expList = []
    
    
    while(q.isEmpty() == False):
        curr = q.pop()
        expList.append(curr)
        if(curr == goal):
            break
        for ttg in jtm[curr]:
            g_cost = jarak[curr] + int(ttg.jarak)
            if(ttg.kota not in jarak or g_cost < jarak[ttg.kota]):
                jarak[ttg.kota] = g_cost
                f_cost = g_cost + heuristic(ttg.kota, h)
                q.push(ttg.kota, f_cost)
                jalan[ttg.kota] = curr
    
    res = []
    i = goal
    while(jalan.get(i) != None):
        res.append(i)
        i = jalan[i]
    res.append(start)
    res.reverse()
    
    print("\nPerjalanan Magetan menuju Surabaya")
    print("\nKota yang dilalui : " + str(res))
    #print("\nkota yang ditempuh yaitu sebanyak : ", str(len(res)),"kota")
    print("\ndengan total jarak tempuh yaitu " + str(jarak[goal]))
    print("\n")

def main():
    asal = "Magetan"
    tujuan = "Surabaya"
    petajtm()
    Astar(asal,tujuan)

if __name__ == "__main__":
    main()

# catat waktu selesai eksekusi code

# print("Lama eksekusi : ", end_time - str_time)



