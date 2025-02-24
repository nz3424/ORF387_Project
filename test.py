import utils

connection = utils.connectToDB()
cDict = utils.getCountriesDict(connection)
seasons = ['1', '2', '3']
seasonsString = ','.join(seasons)
leagues = ["1", "2", "3"]
filename = "PlayerNet.adj"
utils.createPlayerEdgeListFromDB(filename, seasons, leagues)
utils.createClubEdgeListFromDB("ClubNet.adj", seasons, leagues)
graph1, nodeData1 = utils.createWeightedGraphFromEdgeList(filename)
graph2, nodeData2 = utils.createWeightedGraphFromEdgeList("ClubNet.adj")

print(graph1)
ranking = utils.calculatePageRank(graph1)
print(nodeData1[max(ranking, key = ranking.get)])

ranking2 = utils.calculatePageRank(graph2)
print(nodeData2[max(ranking2, key = ranking2.get)])