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
renderView1.ViewSize = [716, 330]
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

# create a new 'Text'
text1 = Text()
text1.Text = 'Ciao!'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from text1
text1Display = Show(text1, renderView1)

# trace defaults for the display properties.
text1Display.FontFile = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(text1)
# ----------------------------------------------------------------