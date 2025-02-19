import os
import time

def get_comm_no(community_id, community_dict):
    community_id = str(community_id)
    if community_id in community_dict:
        return community_dict[community_id]
    else:
        return 0

def edgeWeightBipartiteGraphGenerator(layer1CommunityFile, layer2CommunityFile, layer12InterEdgeFile, resultFile):
    layer1community_info = []
    layer1community_dict = {}

    layer2community_info = []
    layer2community_dict = {}

    layer1community_vertices = {}
    layer2community_vertices = {}

    start_time = time.time()    
    with open(layer1CommunityFile) as f:
        for line in f:
            line_data = line.split(' ')
            if (len(line_data) == 3):
                layer1community_dict[line_data[0]] = line_data[1]
                if line_data[1] not in layer1community_vertices:
                    layer1community_vertices[line_data[1]] = 1
                else:
                    layer1community_vertices[line_data[1]]+=1

    with open(layer2CommunityFile) as f:
        for line in f:
            line_data = line.split(' ')
            if (len(line_data) == 3):
                layer2community_dict[line_data[0]] = line_data[1]
                if line_data[1] not in layer2community_vertices:
                    layer2community_vertices[line_data[1]] = 1
                else:
                    layer2community_vertices[line_data[1]]+=1

    layer1layer2community_edges = {}
    with open(layer12InterEdgeFile) as b:
        for line in b:
            item = line.strip().split(',')
            comm1 = get_comm_no(item[0], layer1community_dict)
            comm2 = get_comm_no(item[1], layer2community_dict)
            if comm1 in layer1community_vertices:
                ver1 = layer1community_vertices[comm1]
            else:
                ver1 = 0
            if comm2 in layer2community_vertices:
                ver2 = layer2community_vertices[comm2]
            else:
                ver2 = 0
            if ver1 > 0 and ver2 > 0: # communities have at least one node
                if (comm1, comm2) not in layer1layer2community_edges:
                    layer1layer2community_edges[(comm1, comm2)] = 1
                else:
                    layer1layer2community_edges[(comm1, comm2)] += 1
    if not os.path.exists(os.path.dirname(resultFile)):
        os.makedirs(os.path.dirname(resultFile))
    fs = open(resultFile, "w")
    for k, v in layer1layer2community_edges.items():
        fs.write("{0},{1},{2},{3},{4}\n".format("1", k[0], "0", k[1], v, "\n"))
    print("-- CBG Generation Time (we) %s seconds ---" % (time.time() - start_time))