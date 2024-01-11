import numpy as np
import matplotlib.pyplot as plt

def plot_graph(data_arrays, labels=None):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot each data array with a different color
    for i, data_array in enumerate(data_arrays):
        label = labels[i] if labels else f'Data {i + 1}'
        ax.plot(data_array, label=label)

    # Customize the plot (optional)
    ax.set_title('Graph from Multiple NumPy Arrays')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Show legend if labels are provided
    if labels:
        ax.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Example: Creating two NumPy arrays with sample data
    data1 = np.array([1, 4, 9, 16, 25])
    data2 = np.array([1, 8, 27, 64, 125])

    # Plot the graphs with labels
    plot_graph([data1, data2], labels=['Array 1', 'Array 2'])
