import numpy as np
import os

#%% Settings
# I use fromat string ('percent's) because this script will be read as a string, and I will susbstite
# 'percent's with the correct path. The "" are needed as this variable has to be a string (otherwise sintax error!)
sim_dir = "%s"
#
cols_chosen = (0,1)  # Columns to chose
cols_names = ('ti_pluto', 't_pluto')

#%% Load data with numpy
data_path = os.path.join(sim_dir, 'out', 'vtk.out')
data = np.genfromtxt(data_path, dtype=None,
                     usecols=cols_chosen, names=cols_names,
                     delimiter=' ', autostrip=True)

#%% Check which vtk files are actuall present
out_dir = os.path.join(sim_dir,'out')
root, dirs, out_files = next(os.walk(out_dir))
# Function for getting the file ordering label
file_order_label = lambda x : int(x.split('.')[-2])
t_index_pluto = []
for file in out_files:
    if file.endswith('.vtk'):
        t_index_pluto.append(file_order_label(file))
np.array(t_index_pluto)

#%% Convert/output to vtkTable
select = map(lambda x: x in t_index_pluto, data['ti_pluto'])
for name in data.dtype.names:
    array = data[name][select]
    output.RowData.append(array, name)

# Check consistency:  no files should exist with a label not present in vtk.out file (i.e.: data['ti_pluto'])
# (as it is a synthom that I took the wrong vtk.out file, instead, the opposite is ok,
# i.e. it is fine that some files are missing, since I might have skipped for instance
# for saving time in downloads or similiar..)
if set(t_index_pluto) - set(data['ti_pluto']) != set([]):
    raise Exception('Some vtk files are present with integer label not present in vtk.out')
