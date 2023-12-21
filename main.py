import networkx as nx
import matplotlib.pyplot as plt

class TVShowGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_tv_show(self, show_name):
        if show_name not in self.graph.nodes:
            self.graph.add_node(show_name)
            print(f"TV show '{show_name}' added successfully.")
        else:
            print(f"TV show '{show_name}' already exists.")

    def add_crossover(self, show1, show2):
        if show1 in self.graph.nodes and show2 in self.graph.nodes:
            self.graph.add_edge(show1, show2)
            print(f"Crossover between '{show1}' and '{show2}' added successfully.")
        else:
            print("Invalid TV show names. Make sure both shows exist.")

    def display_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_color='skyblue', font_size=8)
        plt.show()

def main():
    tv_show_graph = TVShowGraph()

    while True:
        print("\nTV Show Crossover App")
        print("1. Add TV Show")
        print("2. Add Crossover")
        print("3. Display Crossovers Graph")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_name = input("Enter the TV show name: ")
            tv_show_graph.add_tv_show(show_name)

        elif choice == '2':
            show1 = input("Enter the first TV show: ")
            show2 = input("Enter the second TV show: ")
            tv_show_graph.add_crossover(show1, show2)

        elif choice == '3':
            tv_show_graph.display_graph()

        elif choice == '4':
            print("Exiting the TV Show Crossover App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
