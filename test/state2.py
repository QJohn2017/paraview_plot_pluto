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
renderView1.ViewSize = [986, 198]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [200.0, 1000.0, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [195.91129606895933, 1108.666546292415, 10000.0]
renderView1.CameraFocalPoint = [195.91129606895933, 1108.666546292415, 0.0]
renderView1.CameraViewUp = [-1.0, 2.220446049250313e-16, 0.0]
renderView1.CameraParallelScale = 268.54624084911296
renderView1.Background = [0.09411764705882353, 0.10196078431372549, 0.12941176470588237]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [986, 198]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [200.0, 1000.0, 0.0]
renderView2.StereoType = 0
renderView2.CameraPosition = [206.75946807491718, 1099.5202088295666, 3940.2197095449555]
renderView2.CameraFocalPoint = [206.75946807491718, 1099.5202088295666, 0.0]
renderView2.CameraViewUp = [-1.0, 2.220446049250313e-16, 0.0]
renderView2.CameraParallelScale = 268.54624084911296
renderView2.Background = [0.09411764705882353, 0.10196078431372549, 0.12941176470588237]
renderView2.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
data0 = LegacyVTKReader(FileNames=['/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0000.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0001.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0002.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0003.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0004.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0005.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0006.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0007.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0008.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0009.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0010.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0011.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0012.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0013.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0014.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0015.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0016.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0017.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0018.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0019.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0020.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0021.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0022.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0023.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0024.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0025.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0026.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0027.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0028.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0029.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0030.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0031.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0032.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0033.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0034.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0035.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0036.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0037.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0038.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0039.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0040.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0041.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0042.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0043.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0044.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0045.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0046.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0047.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0048.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0049.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0050.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0051.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0052.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0053.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0054.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0055.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0056.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0057.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0058.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0059.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0060.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0061.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0062.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0063.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0064.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0065.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0066.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0067.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0068.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0069.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0070.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0071.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0072.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0073.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0074.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0075.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0076.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0077.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0078.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0079.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0080.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0081.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0082.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0083.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0084.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0085.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0086.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0087.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0088.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0089.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0090.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0091.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0092.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0093.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0094.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0095.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0096.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0097.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0098.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0099.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0100.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0101.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0102.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0103.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0104.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0105.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0106.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0107.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0108.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0109.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0110.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0111.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0112.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0113.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0114.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0115.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0116.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0117.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0118.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0119.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0120.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0121.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0122.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0123.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0124.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0125.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0126.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0127.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0128.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0129.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0130.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0131.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0132.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0133.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0134.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0135.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0136.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0137.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0138.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0139.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0140.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0141.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0142.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0143.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0144.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0145.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0146.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0147.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0148.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0149.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0150.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0151.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0152.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0153.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0154.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0155.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0156.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0157.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0158.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0159.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0160.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0161.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0162.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0163.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0164.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0165.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0166.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0167.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0168.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0169.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0170.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0171.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0172.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0173.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0174.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0175.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0176.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0177.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0178.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0179.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0180.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0181.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0182.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0183.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0184.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0185.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0186.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0187.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0188.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0189.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0190.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0191.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0192.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0193.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0194.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0195.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0196.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0197.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0198.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0199.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0200.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0201.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0202.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0203.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0204.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0205.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0206.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0207.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0208.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0209.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0210.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0211.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0212.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0213.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0214.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0215.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0216.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0217.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0218.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0219.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0220.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0221.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0222.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0223.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0224.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0225.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0226.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0227.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0228.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0229.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0230.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0231.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0232.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0233.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0234.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0235.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0236.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0237.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0238.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0239.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0240.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0241.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0242.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0243.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0244.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0245.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0246.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0247.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0248.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0249.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0250.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0251.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0252.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0253.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0254.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0255.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0256.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0257.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0258.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0259.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0260.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0261.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0262.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0263.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0264.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0265.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0266.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0267.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0268.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0269.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0270.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0271.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0272.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0273.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0274.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0275.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0276.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0277.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0278.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0279.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0280.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0281.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0282.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0283.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0284.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0285.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0286.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0287.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0288.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0289.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0290.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0291.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0292.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0293.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0294.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0295.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0296.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0297.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0298.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0299.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0300.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0301.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0302.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0303.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0304.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0305.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0306.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0307.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0308.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0309.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0310.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0311.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0312.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0313.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0314.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0315.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0316.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0317.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0318.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0319.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0320.vtk'])

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from data0
data0Display = Show(data0, renderView1)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [2.4999999292951713e-10, 0.231373, 0.298039, 0.752941, 5.487959824218569e-07, 0.865003, 0.865003, 0.865003, 1.0973419648507843e-06, 0.705882, 0.0156863, 0.14902]
rhoLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
data0Display.Representation = 'Surface'
data0Display.ColorArrayName = ['CELLS', 'rho']
data0Display.LookupTable = rhoLUT
data0Display.EdgeColor = [0.7529411764705882, 0.7647058823529411, 0.6862745098039216]
data0Display.OSPRayScaleFunction = 'PiecewiseFunction'
data0Display.SelectOrientationVectors = 'None'
data0Display.ScaleFactor = 200.0
data0Display.SelectScaleArray = 'rho'
data0Display.GlyphType = 'Arrow'
data0Display.GlyphTableIndexArray = 'rho'
data0Display.GaussianRadius = 10.0
data0Display.SetScaleArray = [None, '']
data0Display.ScaleTransferFunction = 'PiecewiseFunction'
data0Display.OpacityArray = [None, '']
data0Display.OpacityTransferFunction = 'PiecewiseFunction'
data0Display.DataAxesGrid = 'GridAxesRepresentation'
data0Display.SelectionCellLabelFontFile = ''
data0Display.SelectionPointLabelFontFile = ''
data0Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
data0Display.DataAxesGrid.XTitleFontFile = ''
data0Display.DataAxesGrid.YTitleFontFile = ''
data0Display.DataAxesGrid.ZTitleFontFile = ''
data0Display.DataAxesGrid.XLabelFontFile = ''
data0Display.DataAxesGrid.YLabelFontFile = ''
data0Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
data0Display.PolarAxes.PolarAxisTitleFontFile = ''
data0Display.PolarAxes.PolarAxisLabelFontFile = ''
data0Display.PolarAxes.LastRadialAxisTextFontFile = ''
data0Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for rhoLUT in view renderView1
rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
rhoLUTColorBar.Title = 'rho'
rhoLUTColorBar.ComponentTitle = ''
rhoLUTColorBar.TitleFontFile = ''
rhoLUTColorBar.LabelFontFile = ''

# set color bar visibility
rhoLUTColorBar.Visibility = 1

# show color legend
data0Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from data0
data0Display_1 = Show(data0, renderView2)

# trace defaults for the display properties.
data0Display_1.Representation = 'Surface'
data0Display_1.ColorArrayName = ['CELLS', 'rho']
data0Display_1.LookupTable = rhoLUT
data0Display_1.EdgeColor = [0.7529411764705882, 0.7647058823529411, 0.6862745098039216]
data0Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
data0Display_1.SelectOrientationVectors = 'None'
data0Display_1.ScaleFactor = 200.0
data0Display_1.SelectScaleArray = 'rho'
data0Display_1.GlyphType = 'Arrow'
data0Display_1.GlyphTableIndexArray = 'rho'
data0Display_1.GaussianRadius = 10.0
data0Display_1.SetScaleArray = [None, '']
data0Display_1.ScaleTransferFunction = 'PiecewiseFunction'
data0Display_1.OpacityArray = [None, '']
data0Display_1.OpacityTransferFunction = 'PiecewiseFunction'
data0Display_1.DataAxesGrid = 'GridAxesRepresentation'
data0Display_1.SelectionCellLabelFontFile = ''
data0Display_1.SelectionPointLabelFontFile = ''
data0Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
data0Display_1.DataAxesGrid.XTitleFontFile = ''
data0Display_1.DataAxesGrid.YTitleFontFile = ''
data0Display_1.DataAxesGrid.ZTitleFontFile = ''
data0Display_1.DataAxesGrid.XLabelFontFile = ''
data0Display_1.DataAxesGrid.YLabelFontFile = ''
data0Display_1.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
data0Display_1.PolarAxes.PolarAxisTitleFontFile = ''
data0Display_1.PolarAxes.PolarAxisLabelFontFile = ''
data0Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
data0Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for rhoLUT in view renderView2
rhoLUTColorBar_1 = GetScalarBar(rhoLUT, renderView2)
rhoLUTColorBar_1.Position = [0.8874239350912779, 0.06060606060606061]
rhoLUTColorBar_1.Title = 'rho'
rhoLUTColorBar_1.ComponentTitle = ''
rhoLUTColorBar_1.TitleFontFile = ''
rhoLUTColorBar_1.LabelFontFile = ''

# set color bar visibility
rhoLUTColorBar_1.Visibility = 1

# show color legend
data0Display_1.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [2.4999999292951713e-10, 0.0, 0.5, 0.0, 1.0973419648507843e-06, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(data0)
# ----------------------------------------------------------------