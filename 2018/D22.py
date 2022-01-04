from functools import cache
import heapq


d = 6084
tx = 14
ty = 709

# d = 510
# tx = 10
# ty = 10
@cache
def get_geologic_index(x, y):
    if x == 0 and y == 0:
        return 0
    if x == tx and y == ty:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    xgi = get_erosion_level(x-1, y)
    ygi = get_erosion_level(x, y-1)
    ngi = xgi * ygi
    return  ngi

@cache
def get_erosion_level(x, y):
   gi = get_geologic_index(x, y)
   el = ((gi + d) % 20183)
   return el

@cache
def get_type(x, y):
   return get_erosion_level(x, y) % 3

def part1():
    risk = 0
    for y in range(ty + 1):
        line = ''
        for x in range(tx + 1):
            el = get_erosion_level(x, y) % 3
            risk += el
            if el == 0:
                line += '.'
            elif el == 1:
                line += '='
            elif el == 2:
                line += '|'
        print(line)
    print(risk)

class Node(object):
    def __init__(self, x, y, tool, terrain, time, history):
        self.x = x
        self.y = y
        self.tool = tool
        self.terrain = terrain
        if terrain == 0:
            self.print = '.'
        elif terrain == 1:
            self.print = '='
        else:
            self.print = '|'
        self.time = time
        self.history = history

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return True

    def __cmp__(self, other):
        return cmp((self.time, self.x, self.y), (other.time, other.x, other.y))

    def __repr__(self):
        return "%s %s" % (self.x, self.y)

# tool 0 = neither  (Wet-1 or narrow-2)
# tool 1 = Climbing gear (Wet-1 or rocky-0)
# tool 2 = torch (rocky-0 or narrow-2)
# terrain 0 = rocky  (torch-2 or climbing gear-1)
# terrain 1 = wet (nether-0 or climbing gear-1)
# terrain 2 = narrow (neither-0 or torch-2)
def part2():
    stack = []
    visited = []
    start = Node(0, 0, 2, 0, 0, 'Start w torch-')
    heapq.heappush(stack, (0, start))
    while stack:
        smallest = heapq.heappop(stack)
        time = smallest[0]
        px = smallest[1].x
        py = smallest[1].y
        tool = smallest[1].tool
        terrain = get_type(px, py)
        pter = smallest[1].print
        history = smallest[1].history
        if (px, py, tool) in visited:
            continue
        else:
            visited.append((px, py, tool))
        if px > 50:
            continue
        if px == tx and py == ty and tool == 2:
            print('MADE IT')
            print(time, history)
            return time
        if py % 100 == 0 and px % 10 == 0:
            print(len(stack), time, px, py, tool, terrain, pter)
        if terrain == 0:
            if tool == 2:
                node = Node(px, py, 1, terrain, time + 7, history + '-Climbing-')
                heapq.heappush(stack, (node.time, node))
            elif tool == 1:
                node = Node(px, py, 2, terrain, time + 7, history + '-Torch-')
                heapq.heappush(stack, (node.time, node))
        if terrain == 1:
            if tool == 0:
                node = Node(px, py, 1, terrain, time + 7, history + '-Climbing-')
                heapq.heappush(stack, (node.time, node))
            elif tool == 1:
                node = Node(px, py, 0, terrain, time + 7, history + '-Neither-')
                heapq.heappush(stack, (node.time, node))
        if terrain == 2:
            if tool == 0:
                node = Node(px, py, 2, terrain, time + 7, history + '-Torch-')
                heapq.heappush(stack, (node.time, node))
            elif tool == 2:
                node = Node(px, py, 0, terrain, time + 7, history + '-Neither-')
                heapq.heappush(stack, (node.time, node))

        n = get_type(px + 1, py)
        if ((n == 0 and tool in (1, 2)) or (n == 1 and tool in (0, 1)) or (n == 2 and tool in (0, 2))):
            node = Node(px + 1, py, tool, n, time + 1, history + pter + 'E')
            heapq.heappush(stack, (node.time, node))

        n = get_type(px, py + 1)
        if ((n == 0 and tool in (1, 2)) or (n == 1 and tool in (0, 1)) or (n == 2 and tool in (0, 2))):
            node = Node(px, py + 1, tool, n, time + 1, history + pter + 'S')
            heapq.heappush(stack, (node.time, node))

        if py > 0:
            n = get_type(px, py - 1)
            if ((n == 0 and tool in (1, 2)) or (n == 1 and tool in (0, 1)) or (n == 2 and tool in (0, 2))):
                node = Node(px, py - 1, tool, n, time + 1, history + pter + 'S')
                heapq.heappush(stack, (node.time, node))

        if px > 0:
            n = get_type(px - 1, py)
            if ((n == 0 and tool in (1, 2)) or (n == 1 and tool in (0, 1)) or (n == 2 and tool in (0, 2))):
                node = Node(px - 1 , py, tool, n, time + 1, history + pter + 'S')
                heapq.heappush(stack, (node.time, node))

        # Swap tool
        # terrain = get_type(smallest[1]['x'])
        # if x > 0:
        #     heapq.heappush(stack, get_next(smallest, x-1, y))
        # if y > 0:
        #     heapq.heappush(stack, get_next(smallest, x, y-1))
        # heapq.heappush(stack, get_next(smallest, x+1, y))
        # heapq.heappush(stack, get_next(smallest, x, y+1))







if __name__ == '__main__':
    # unittest.main()

    part2()
    # part1()

#
# Start w torch-SE-Climbing-E-Torch-ESEESESESESSSS-Climbing-SEE
# M=.|=.|.|=.|=|=.
# .|=|=|||..|.=...
# .==|....||=..|==
# =.|....|.==.|==.
# =|..==...=.|==..
# =||.=.=||=|=..|=
# |.=.===|||..=..|
# |..==||=.|==|===
# .=..===..=|.|||.
# .======|||=|=.|=
# .===|=|===X===||
# =|||...|==..|=.|
# =.=|=.=..=.||==|
# ||=|=...|==.=|==
# |=.=||===.|||===
# ||.|==.|.|.||=||
