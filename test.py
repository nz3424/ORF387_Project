import utils
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

connection = utils.connectToDB()
#seasons = ['1', '2', '3']
# leagues = ["1", "2", "3"]
filename = "ClubNet.adj"
seasons, leagues = 'all', 'all'

utils.createClubEdgeListFromDB(filename, weightedByClubImportance=True)
clubGraph, nodeData = utils.createWeightedGraphFromEdgeList(filename, directed = True)



betweenness = utils.calculateFastWeightedBetweennessCentrality(clubGraph)

betweennessnx = nx.betweenness_centrality(clubGraph, weight = "reciprocal")
betweennessnx = sorted(betweennessnx.items(), key = itemgetter(1), reverse = True)


outputFile = "WeightedBetweenness.txt"
file = open(outputFile, 'w')
for i in range(1, len(betweenness)):
    outputString = f"Node name: {nodeData[betweennessnx[i][0]]}, score: {betweennessnx[i][1]}"
    # print(outputString)
    file.write(outputString + '\n')
file.close()

# print("Best weighted betweeness: ", nodeData[min(WBC_ranking, key = WBC_ranking.get)])
# print("Nick Best weighted betweeness: ", nodeData[min(betweenness, key = betweenness.get)])

