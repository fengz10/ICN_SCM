def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 100000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest

def dijkstra(graph, start):
    # Using priority queue to keep track of minium distance from start
    # to a vertex.
    pqueue = {} # vertex: distance to start
    dist = {}   # vertex: distance to start
    pred = {}   # vertex: previous (predecesor) vertex in shortest path

    # initializing dictionaries
    for v in graph:
        dist[v] = 100000
        pred[v] = -1
    dist[start] = 0
    for v in graph:
        pqueue[v] = dist[v] # equivalent to push into queue

    while pqueue:
        u = popmin(pqueue) # for priority queues, pop will get the element with smallest value
        for v in graph[u].keys(): # for each neighbor of u
            w = graph[u][v] # distance u to v
            newdist = dist[u] + w
            if (newdist < dist[v]): # is new distance shorter than one in dist?
                # found new shorter distance. save it
                pqueue[v] = newdist
                dist[v] = newdist
                pred[v] = u

    return dist, pred


def floydwarshall(graph): 
    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal

    # I comment out the parameter of pred, since I do not care the route
    # And the memory is not enouph for AS relationship data
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        #pred[u] = {}
        for v in graph:
            dist[u][v] = 100000
        #    pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
        #    pred[u][neighbor] = u
 
    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
        #            pred[u][v] = pred[t][v] # route new path through t
 
    return dist, pred        
