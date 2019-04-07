# We will use numpy to read the csv file.
# Refer to numpy documentation for genfromtxt() for details on
# customizing the CSV file parsing.

import numpy as np
import os

#%% Settings
sim_dir = '/home/ema/simulazioni/sims_pluto/dens_real/1.3e5Pa/'


cols_chosen = (0,1)  # Columns to chose
cols_names = ('time_index', 'time')

#%% Load data with numpy
data_path = os.path.join(sim_dir, 'out', 'vtk.out')
data = np.genfromtxt(data_path, dtype=None,
                     usecols=cols_chosen, names=cols_names,
                     delimiter=' ', autostrip=True)

#%% Get time info
outInfo = self.GetOutputInformation(0)
if outInfo.Has(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_TIME_STEP()):
  time = outInfo.Get(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_TIME_STEP())
else:
  time = 0

#%% Convert/output to vtkTable
for name in data.dtype.names:
    array = data[name]
    output.RowData.append(array, name)
