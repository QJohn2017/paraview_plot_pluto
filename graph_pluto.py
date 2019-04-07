#### import the simple module from the paraview
from paraview.simple import *
import os

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

#%% Some custom definitions
def make_standard_view(materialLibrary):
    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [832, 330]
    renderView1.InteractionMode = '2D'
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [200.0, 1000.0, 0.0]
    renderView1.StereoType = 0
    renderView1.CameraPosition = [200.0, 1000.0, 10000.0]
    renderView1.CameraFocalPoint = [200.0, 1000.0, 0.0]
    renderView1.CameraViewUp = [-1.0, 2.220446049250313e-16, 0.0]
    renderView1.CameraParallelScale = 1019.803902718557
    renderView1.Background = [0.09411764705882353, 0.10196078431372549, 0.12941176470588237]
    renderView1.OSPRayMaterialLibrary = materialLibrary

    # init the 'GridAxes3DActor' selected for 'AxesGrid'
    renderView1.AxesGrid.XTitleFontFile = ''
    renderView1.AxesGrid.YTitleFontFile = ''
    renderView1.AxesGrid.ZTitleFontFile = ''
    renderView1.AxesGrid.XLabelFontFile = ''
    renderView1.AxesGrid.YLabelFontFile = ''
    renderView1.AxesGrid.ZLabelFontFile = ''
    return renderView1

#%%
Aggiungi controllo che nel vtk.out siano segnati gli stessi vtk che ci sono in realta'.
Dire come eventuale messaggio di errore, che se non ci sono si puo implementare un
metodo che seleziona solo i file che che corrispondono alle righe presenti della tablella
(o analogamente al rovescio, seleziona solo certe righe della tabella..) e stampa un warning a video

#%% Make the view
# get the material library
materialLibrary1 = GetMaterialLibrary()
renderView1 = make_standard_view(materialLibrary1)
# renderView2 = make_standard_view(materialLibrary1)

#%% Read files
sim_dir = raw_input('Tell simulation abs path:\n')
print sim_dir
out_dir = os.path.join(sim_dir,'out')

root, dirs, out_files = next(os.walk(out_dir))
vtk_files = []
for file in out_files:
    if file.endswith('.vtk'):
        vtk_files.append(os.path.join(root, file))
# Sort the files based on file labels (alphabetical order is not ok!!)
file_order_label = lambda x : int(x.split('.')[-2])
vtk_files.sort(key=file_order_label)
# Read files
data0 = LegacyVTKReader(FileNames=vtk_files)

#%% Make current annotation
# create a new 'Extract Location'
extractLocation1 = ExtractLocation(Input=data0)
extractLocation1.Mode = 'Interpolate At Location'
# TODO:HERE WRITE THE LOCATION BASED ON THE SIMULATION DATA
rcap = float(raw_input('\nCapillary radius in code units:\n'))
print rcap
zcap = float(raw_input('\nCapillary half length in code units:\n'))
print zcap
z_location = zcap/4.
extractLocation1.Location = [rcap, z_location, 0.0]

# create a new 'Calculator'
calculator1 = Calculator(Input=extractLocation1)
calculator1.ResultArrayName = 'current'
calculator1.Function = '0.5e7*(1e-5*(%f))*(1e-4*bx3)' % rcap

# create a new 'Annotate Attribute Data'
annotateAttributeData1 = AnnotateAttributeData(Input=calculator1)
annotateAttributeData1.SelectInputArray = ['POINTS', 'current']
annotateAttributeData1.Prefix = 'current(A)='

#%% Create views with T, ne, B


#%% Visualize
# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------
# show data from data0
data0Display = Show(data0, renderView1)
# data1Display = Show(data0, renderView2)


#%% Final stuff
Render()
Show()

# raw_input('press enter to close')

#
# p = os.walk('/home/ema/simulazioni/sims_pluto/dens_real/1.3e5Pa')
# for root,dirs,files in p:
#     print '--- NEXT ITERATION ---'
#     print '--- root ---'
#     print root
#     print '--- dirs ---'
#     print dirs
#     print '--- files ---'
#     print files
