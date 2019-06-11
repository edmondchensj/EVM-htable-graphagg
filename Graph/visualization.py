from graphviz import Digraph
from pprint import pprint
from Graph.GraphAggregator import GraphAggregator
import json
import os

def test():


    dot = Digraph(comment='The Round Table')

    dot.node('1','1')
    dot.node('2','2')
    dot.node('11','11')

    #dot.edges(['a1a2','a2a11'])
    dot.edge('1', '2', constraint='true')
    dot.edge('2', '11', constraint='true')


    dot.view()


def visualizeGraph(graph, output_fn):
    dot = Digraph(comment='Graph Aggregator')
    nodes = []
    
    for key in graph.keys():
        if key not in nodes:
            nodes.append(str(key))
        for sub_key in graph[key].keys():
            if sub_key not in nodes:
                nodes.append(str(sub_key))
            
    # for key in  graph.keys():
    #   for sub_key in graph[key].keys():
    #       if graph[key][sub_key]['constraint']:

    #           dot.node(str(sub_key), str(sub_key), xlabel=str(graph[key][sub_key]['constraint']))
    #           nodes.remove(str(sub_key))

    for i in nodes:
        dot.node(i, i)
    for key in graph.keys():
        for sub_key in graph[key].keys():
            if graph[key][sub_key]['constraint']:
                dot.edge(str(key),str(sub_key), constraint='true', label=str(graph[key][sub_key]['constraint']))
            else:
                dot.edge(str(key),str(sub_key), constraint='true')


    dot.render(output_fn, view=True)  

def main():
    folder = 'data/abnormal_traces/contract_folders'
    
    subfolders = [item for item in os.listdir(folder)
                if os.path.isdir(os.path.join(folder, item))]

    for subf in subfolders:
        subf_path = os.path.join(folder, subf)
        graph_file = os.path.join(subf_path, 'graph.json')

        with open(graph_file, 'r') as f:
            graph = json.load(f)

        visualizeGraph(graph, subf_path+'/graph')

if __name__ == '__main__':
    main()



