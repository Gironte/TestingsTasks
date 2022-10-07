from deikstra import deikstra_algorithm
from graph import Graph
import json
import sys

def find_shortest_path(previous_nodes, start_currency, target_currency):
    path = []
    node = target_currency

    while node != start_currency:
                try:
                    path.append([previous_nodes[node] + "/" + node])
                    node = previous_nodes[node]
                except:
                    raise Exception(f"Relevant path for exchange {start_currency} -> {target_currency} has not been found.")
    
    return list(reversed(path))

def fillGraph(config):
    nodes = []
    init_graph = {}

    for doubleCurrency in config.keys():
        for currency in doubleCurrency.split('/'): 
            if (currency not in nodes):
                nodes.append(currency)
                init_graph[currency] = {}
                for doubleCurrency in config.keys():
                    if doubleCurrency.split('/')[0] == currency:
                        init_graph[currency][doubleCurrency.split('/')[1]] = 1

    return Graph(nodes, init_graph)

def run(start_currency, target_currency, config):
    if (start_currency == target_currency):
        raise Exception(f"{start_currency} = {target_currency}")
    
    graph = fillGraph(config)

    if (not start_currency in graph.get_nodes() or not target_currency in graph.get_nodes()):
        raise Exception("Currency doesn't exist.")

    previous_currencies = deikstra_algorithm(graph, start_currency)

    if (previous_currencies == {}):
        raise Exception(f"Relevant path for exchange {start_currency} -> {target_currency} has not been found.")

    return find_shortest_path(previous_currencies, start_currency, target_currency)

if __name__== "__main__":
    with open("config.json", "r") as jsonfile:
        config = json.load(jsonfile)

    input = json.loads(sys.argv[1])

    print(run(input[0], input[1], config))