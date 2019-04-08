# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [490, 330]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 0.0, 6.6921304299024635]
renderView1.CameraParallelScale = 1.7320508075688772
renderView1.Background = [0.09411764705882353, 0.10196078431372549, 0.12941176470588237]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Programmable Source'
programmableSource1 = ProgrammableSource()
programmableSource1.Script = """
import vtk

outInfo = self.GetOutputInformation(0)
if outInfo.Has(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_TIME_STEP()):
  time = outInfo.Get(vtk.vtkStreamingDemandDrivenPipeline.UPDATE_TIME_STEP())
else:
  time = 0

radius = math.sin(time * 2 * math.pi / 100) + 1.0
sphere = vtk.vtkSphereSource()
sphere.SetRadius(radius)
sphere.Update()

pd = self.GetPolyDataOutput()
pd.ShallowCopy(sphere.GetOutput())
"""

programmableSource1.ScriptRequestInformation = """
timeSteps = range(100)

outInfo = self.GetOutputInformation(0)

timeRange = [timeSteps[0], timeSteps[-1]]
outInfo.Set(vtk.vtkStreamingDemandDrivenPipeline.TIME_RANGE(), timeRange, 2)
outInfo.Set(vtk.vtkStreamingDemandDrivenPipeline.TIME_STEPS(), timeSteps, len(timeSteps))
"""

programmableSource1.PythonPath = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from programmableSource1
programmableSource1Display = Show(programmableSource1, renderView1)

# trace defaults for the display properties.
programmableSource1Display.Representation = 'Surface'
programmableSource1Display.ColorArrayName = [None, '']
programmableSource1Display.EdgeColor = [0.7529411764705882, 0.7647058823529411, 0.6862745098039216]
programmableSource1Display.OSPRayScaleArray = 'Normals'
programmableSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableSource1Display.SelectOrientationVectors = 'None'
programmableSource1Display.ScaleFactor = -2.0000000000000002e+298
programmableSource1Display.SelectScaleArray = 'None'
programmableSource1Display.GlyphType = 'Arrow'
programmableSource1Display.GlyphTableIndexArray = 'None'
programmableSource1Display.GaussianRadius = -1e+297
programmableSource1Display.SetScaleArray = [None, 'Normals']
programmableSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableSource1Display.OpacityArray = [None, 'Normals']
programmableSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableSource1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableSource1Display.SelectionCellLabelFontFile = ''
programmableSource1Display.SelectionPointLabelFontFile = ''
programmableSource1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
programmableSource1Display.DataAxesGrid.XTitleFontFile = ''
programmableSource1Display.DataAxesGrid.YTitleFontFile = ''
programmableSource1Display.DataAxesGrid.ZTitleFontFile = ''
programmableSource1Display.DataAxesGrid.XLabelFontFile = ''
programmableSource1Display.DataAxesGrid.YLabelFontFile = ''
programmableSource1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
programmableSource1Display.PolarAxes.PolarAxisTitleFontFile = ''
programmableSource1Display.PolarAxes.PolarAxisLabelFontFile = ''
programmableSource1Display.PolarAxes.LastRadialAxisTextFontFile = ''
programmableSource1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(programmableSource1)
# ----------------------------------------------------------------
