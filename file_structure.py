 
import os

# Define root directory
root_dir = './real-time-data-processing/'

# Create root directory
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

# Create sub-directories
data_dir = os.path.join(root_dir, 'data')
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

results_dir = os.path.join(root_dir, 'results')
if not os.path.exists(results_dir):
    os.mkdir(results_dir)

# Create empty files in sub-directories
data_file = os.path.join(data_dir, 'data.csv')
if not os.path.exists(data_file):
    open(data_file, 'a').close()

results_file = os.path.join(results_dir, 'results.csv')
if not os.path.exists(results_file):
    open(results_file, 'a').close()

# Display success message
print('File structure created successfully.')
