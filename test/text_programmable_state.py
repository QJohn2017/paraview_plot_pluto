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
renderView1.ViewSize = [478, 330]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 0.0, 5.530686305704514]
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
programmableSource1 = ProgrammableSource(renderView1)
programmableSource1.Script = """import vtk
print('ciaooOOOO!')
print(input)
# colors = vtk.vtkNamedColors()
#
# Create a rendering window and renderer.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.SetWindowName("Text Actor")
renWin.AddRenderer(ren)

# Create a render window interactor.
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Create a text actor.
txt = vtk.vtkTextActor()
txt.SetInput("Hello World!")
txtprop = txt.GetTextProperty()
txtprop.SetFontFamilyToArial()
txtprop.BoldOn()
txtprop.SetFontSize(36)
txtprop.ShadowOn()
txtprop.SetShadowOffset(4, 4)
# txtprop.SetColor(colors.GetColor3d("Cornsilk"))
txt.SetDisplayPosition(20, 30)

# Assign actor to the renderer.
ren.AddActor(txt)
# ren.SetBackground(colors.GetColor3d("DarkGreen"))

# Enable user interface interactor.
iren.Initialize()
renWin.Render()
iren.Start()"""
programmableSource1.ScriptRequestInformation = ''
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
programmableSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableSource1Display.SelectOrientationVectors = 'None'
programmableSource1Display.ScaleFactor = -2.0000000000000002e+298
programmableSource1Display.SelectScaleArray = 'None'
programmableSource1Display.GlyphType = 'Arrow'
programmableSource1Display.GlyphTableIndexArray = 'None'
programmableSource1Display.GaussianRadius = -1e+297
programmableSource1Display.SetScaleArray = [None, '']
programmableSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableSource1Display.OpacityArray = [None, '']
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
