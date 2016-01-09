## Copyright 
Written by Zhen Feng of Tsinghua University
Copyright GPLv2
The code is written for the simulation experiment of my research papers.
Dataset is from Rocketfuel

## File description
### 1. ShortestPath.py
Define two algorithms to calculate the shortest path: Dijkstra and Floyd.
### 2. ReadEdges.py
Use the split function of regular expression to parse PoP names in the dateset
### 3. PreprocessTopology.py
Record the PoP information of various ASes we care for, including topology, PoP name to id mapping, and external links, and store them into the pickle files.
### 4. Zipf.py
The class of a zifp generater.
### 5. SimMain
The main simulation procedure.
Generate request number, distribution, cache size, cache ratio, and etc.
It will output the path length and profit of the two different algorithms (shortest or no-valley) for ASes you care for.
### 8. Fixed bugs:
TBD
## Note
Test every function before use it. Make sure it works right, especially for some particular parameters. For example, whether the first step and last step nodes is the same as we expected.




