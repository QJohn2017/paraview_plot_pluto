# We will use numpy to read the csv file.
# Refer to numpy documentation for genfromtxt() for details on
# customizing the CSV file parsing.

timeSteps = range(100)

outInfo = self.GetOutputInformation(0)

timeRange = [timeSteps[0], timeSteps[-1]]
outInfo.Set(vtk.vtkStreamingDemandDrivenPipeline.TIME_RANGE(), timeRange, 2)
outInfo.Set(vtk.vtkStreamingDemandDrivenPipeline.TIME_STEPS(), timeSteps, len(timeSteps))
