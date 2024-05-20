import json
import networkx as nx
import matplotlib.pyplot as plt

def json_vers_nx(chemin):
    # Load JSON data
    with open(chemin, 'r') as f:
        data = json.load(f)

    # Create a directed graph
    G = nx.Graph()

    # Add nodes and edges to the graph
    for movie in data:
        # Add movie as node
        title = movie['title']
        G.add_node(title, type='movie')
        
        if 'year' in movie:
            G.nodes[title]['year'] = movie['year']

        # Add cast as nodes and edges
        for actor in movie['cast']:
            actor_name = actor.replace('[[', '').replace(']]', '').split('|')[-1]
            G.add_node(actor_name, type='actor')
            G.add_edge(title, actor_name)

        # Add directors as nodes and edges
        for director in movie.get('directors', []):
            director_name = director.replace('[[', '').replace(']]', '').split('|')[-1]
            G.add_node(director_name, type='director')
            G.add_edge(title, director_name)

        # Add producers as nodes and edges
        for producer in movie.get('producers', []):
            producer_name = producer.replace('[[', '').replace(']]', '').split('|')[-1]
            G.add_node(producer_name, type='producer')
            G.add_edge(title, producer_name)

        # Add companies as nodes and edges if available
        for company in movie.get('companies', []):
            company_name = company.replace('[[', '').replace(']]', '').split('|')[-1]
            G.add_node(company_name, type='company')
            G.add_edge(title, company_name)

    return G

# Example usage
graph = json_vers_nx('data_100.json')

plt.clf()
# Draw the graph
nx.draw(graph, with_labels=True)

# Show the plot
plt.show()

