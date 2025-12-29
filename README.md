# Sorting Algorithms Visualizer

## Description

This is a Python GUI application built with Tkinter to visualize and analyze various sorting algorithms. The application allows users to generate random lists of different sizes, select from a variety of sorting algorithms, and observe the sorting process in real-time through animated bar charts. It includes controls to adjust the visualization speed (slow, medium, fast), pause and resume the sorting execution, and a second tab for comparing algorithm performance using graphs of iteration counts and execution times.

The project demonstrates the following sorting algorithms:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Counting Sort
- Shell Sort
- Quick Sort
- Heap Sort
- Merge Sort
- Radix Sort
- Gnome Sort

## Features

- **Interactive GUI**: Built with Tkinter for easy user interaction.
- **Random List Generation**: Generate random integer lists of user-specified sizes.
- **Algorithm Selection**: Choose from 10 different sorting algorithms via a dropdown menu.
- **Visualization**: Real-time animated bar charts showing the sorting process using Matplotlib.
- **Speed Control**: Adjust the animation speed with radio buttons (Lenta/Slow, Media/Medium, Rápida/Fast).
- **Pause/Resume**: Buttons to pause and resume the sorting visualization.
- **Performance Comparison Tab**: A second window/tab that graphs the number of steps (Big O analysis) and execution times for all algorithms across different list sizes.
- **Cross-Platform**: Runs on any system with Python and required libraries installed.

## Requirements

- Python 3.x
- Tkinter (included with Python standard library)
- Matplotlib (for graphing and visualizations)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sorting-algorithms-visualizer.git
   cd sorting-algorithms-visualizer
   ```

2. Install dependencies:
   ```
   pip install matplotlib
   ```

## Usage

1. Run the main application:
   ```
   python MAIN.py
   ```

2. In the GUI:
   - Select a sorting algorithm from the dropdown.
   - Choose the visualization speed.
   - Enter the number of random numbers to generate and click "Generar".
   - The sorting will start automatically, with real-time bar chart updates.
   - Use "Pausar" to pause and "Reanudar" to resume.
   - Click "Pestaña 2" to open the performance comparison tab, which generates graphs and displays execution times.


## Code Structure

- `MAIN.py`: Entry point and main GUI logic.
- `Pestania2.py`: Logic for the performance comparison tab.
- Algorithm files (e.g., `bubble.py`, `selection.py`, etc.): Implementations of individual sorting algorithms with visualization callbacks.
- Other dependencies: Matplotlib for plotting, Tkinter for UI.

## Authors

- Fernando Salazaar
- Oscar Aguirre
