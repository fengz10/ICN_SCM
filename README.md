## Copyright 
Written by Zhen Feng of Tsinghua University
Copyright GPLv2
The code is written for the simulation experiment of my research papers.
Dataset is from Rocketfuel.

## File description
### 1. ShortestPath.py
Define two algorithms to calculate the shortest path: Dijkstra and Floyd.
### 2. ReadEdges.py
Use the split function of regular expression to parse PoP names in the dateset.
### 3. PreprocessTopology.py
Record the PoP information of various ASes we care for, including topology, PoP name to id mapping, and external links, and store them into the pickle files.
### 4 AddTreeTopology.py
Add trees to the points of PoP, and all requests will originate from the leaves of the trees.
### 5. Zipf.py
The class of a zifp generater.
### 6. SimMain.py
The main simulation procedure.
Generate request number, distribution, cache size, cache ratio, and etc.
It will output the path length and profit of the two different algorithms (shortest or no-valley) for ASes you care for.
### 7. CalResults.py
Calculate costs of various scenarios

### 8. Programs in resultsPlot direction
Plot the results.

### 9. Fixed bugs:
In the edges.lat data of 3566:3566, there is a line of '3356:Manchester, MA -> 3356:Boston, MA 100000'. The delay of 100000ms is a false value, and we did not omit it for the first hand. Similar false data includes:
./Rocketfuel/maps-n-paths/7018:7018/edges.lat  7018Los Angeles, CA  7018Gardena, CA 100000
./Rocketfuel/maps-n-paths/1221:4637/edges.lat  1221Palo Alto, CA  4637hhts 100000
./Rocketfuel/maps-n-paths/1221:4637/edges.lat  1221Palo Alto, CA  4637tmhs 100000
./Rocketfuel/maps-n-paths/3356:3356/edges.lat  3356Boston, MA  3356Manchester, MA 100000
./Rocketfuel/maps-n-paths/3356:3356/edges.lat  3356Manchester, MA  3356Boston, MA 100000
./Rocketfuel/maps-n-paths/7018:7018/edges.lat  7018Gardena, CA  7018Los Angeles, CA 100000
./Rocketfuel/maps-n-paths/7018:7018/edges.lat  7018Los Angeles, CA  7018Gardena, CA 100000 

## Note
Test every function before use it. Make sure it works right, especially for some particular parameters. For example, whether the first step and last step nodes is the same as we expected.




