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
renderView1.ViewSize = [353, 330]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 0.0, 3.2903743041222895]
renderView1.CameraParallelScale = 0.8516115354228021
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

# create a new 'Sphere'
sphere1 = Sphere()

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sphere1
sphere1Display = Show(sphere1, renderView1)

# trace defaults for the display properties.
sphere1Display.Representation = 'Surface'
sphere1Display.ColorArrayName = [None, '']
sphere1Display.EdgeColor = [0.7529411764705882, 0.7647058823529411, 0.6862745098039216]
sphere1Display.OSPRayScaleArray = 'Normals'
sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
sphere1Display.SelectOrientationVectors = 'None'
sphere1Display.ScaleFactor = 0.1
sphere1Display.SelectScaleArray = 'None'
sphere1Display.GlyphType = 'Arrow'
sphere1Display.GlyphTableIndexArray = 'None'
sphere1Display.GaussianRadius = 0.005
sphere1Display.SetScaleArray = ['POINTS', 'Normals']
sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
sphere1Display.OpacityArray = ['POINTS', 'Normals']
sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
sphere1Display.DataAxesGrid = 'GridAxesRepresentation'
sphere1Display.SelectionCellLabelFontFile = ''
sphere1Display.SelectionPointLabelFontFile = ''
sphere1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
sphere1Display.DataAxesGrid.XTitleFontFile = ''
sphere1Display.DataAxesGrid.YTitleFontFile = ''
sphere1Display.DataAxesGrid.ZTitleFontFile = ''
sphere1Display.DataAxesGrid.XLabelFontFile = ''
sphere1Display.DataAxesGrid.YLabelFontFile = ''
sphere1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
sphere1Display.PolarAxes.PolarAxisTitleFontFile = ''
sphere1Display.PolarAxes.PolarAxisLabelFontFile = ''
sphere1Display.PolarAxes.LastRadialAxisTextFontFile = ''
sphere1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(sphere1)
# ----------------------------------------------------------------