
# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
data0 = LegacyVTKReader(FileNames=['/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0000.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0001.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0002.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0003.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0004.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0005.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0006.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0007.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0008.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0009.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0010.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0011.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0012.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0013.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0014.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0015.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0016.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0017.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0018.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0019.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0020.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0021.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0022.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0023.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0024.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0025.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0026.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0027.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0028.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0029.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0030.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0031.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0032.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0033.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0034.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0035.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0036.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0037.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0038.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0039.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0040.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0041.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0042.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0043.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0044.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0045.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0046.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0047.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0048.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0049.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0050.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0051.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0052.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0053.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0054.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0055.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0056.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0057.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0058.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0059.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0060.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0061.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0062.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0063.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0064.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0065.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0066.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0067.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0068.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0069.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0070.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0071.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0072.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0073.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0074.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0075.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0076.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0077.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0078.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0079.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0080.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0081.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0082.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0083.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0084.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0085.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0086.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0087.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0088.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0089.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0090.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0091.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0092.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0093.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0094.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0095.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0096.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0097.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0098.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0099.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0100.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0101.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0102.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0103.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0104.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0105.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0106.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0107.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0108.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0109.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0110.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0111.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0112.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0113.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0114.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0115.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0116.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0117.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0118.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0119.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0120.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0121.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0122.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0123.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0124.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0125.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0126.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0127.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0128.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0129.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0130.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0131.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0132.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0133.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0134.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0135.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0136.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0137.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0138.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0139.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0140.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0141.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0142.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0143.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0144.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0145.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0146.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0147.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0148.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0149.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0150.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0151.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0152.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0153.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0154.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0155.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0156.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0157.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0158.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0159.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0160.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0161.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0162.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0163.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0164.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0165.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0166.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0167.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0168.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0169.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0170.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0171.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0172.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0173.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0174.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0175.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0176.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0177.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0178.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0179.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0180.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0181.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0182.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0183.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0184.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0185.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0186.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0187.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0188.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0189.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0190.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0191.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0192.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0193.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0194.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0195.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0196.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0197.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0198.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0199.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0200.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0201.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0202.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0203.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0204.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0205.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0206.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0207.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0208.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0209.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0210.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0211.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0212.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0213.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0214.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0215.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0216.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0217.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0218.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0219.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0220.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0221.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0222.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0223.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0224.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0225.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0226.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0227.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0228.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0229.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0230.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0231.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0232.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0233.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0234.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0235.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0236.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0237.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0238.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0239.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0240.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0241.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0242.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0243.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0244.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0245.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0246.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0247.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0248.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0249.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0250.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0251.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0252.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0253.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0254.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0255.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0256.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0257.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0258.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0259.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0260.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0261.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0262.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0263.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0264.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0265.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0266.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0267.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0268.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0269.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0270.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0271.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0272.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0273.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0274.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0275.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0276.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0277.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0278.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0279.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0280.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0281.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0282.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0283.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0284.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0285.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0286.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0287.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0288.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0289.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0290.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0291.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0292.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0293.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0294.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0295.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0296.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0297.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0298.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0299.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0300.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0301.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0302.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0303.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0304.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0305.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0306.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0307.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0308.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0309.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0310.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0311.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0312.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0313.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0314.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0315.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0316.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0317.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0318.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0319.vtk', '/home/ema/simulazioni/sims_pluto/dens_real/1e5Pa/out/data.0320.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [986, 426]

# show data in view
data0Display = Show(data0, renderView1)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
rhoLUT.InterpretValuesAsCategories = 0
rhoLUT.AnnotationsInitialized = 0
rhoLUT.ShowCategoricalColorsinDataRangeOnly = 0
rhoLUT.RescaleOnVisibilityChange = 0
rhoLUT.EnableOpacityMapping = 0
rhoLUT.RGBPoints = [2.4999999292951713e-10, 0.231373, 0.298039, 0.752941, 5.487959824218569e-07, 0.865003, 0.865003, 0.865003, 1.0973419648507843e-06, 0.705882, 0.0156863, 0.14902]
rhoLUT.UseLogScale = 0
rhoLUT.ColorSpace = 'Diverging'
rhoLUT.UseBelowRangeColor = 0
rhoLUT.BelowRangeColor = [0.0, 0.0, 0.0]
rhoLUT.UseAboveRangeColor = 0
rhoLUT.AboveRangeColor = [0.5, 0.5, 0.5]
rhoLUT.NanColor = [1.0, 1.0, 0.0]
rhoLUT.NanOpacity = 1.0
rhoLUT.Discretize = 1
rhoLUT.NumberOfTableValues = 256
rhoLUT.ScalarRangeInitialized = 1.0
rhoLUT.HSVWrap = 0
rhoLUT.VectorComponent = 0
rhoLUT.VectorMode = 'Magnitude'
rhoLUT.AllowDuplicateScalars = 1
rhoLUT.Annotations = []
rhoLUT.ActiveAnnotatedValues = []
rhoLUT.IndexedColors = []
rhoLUT.IndexedOpacities = []

# trace defaults for the display properties.
data0Display.Representation = 'Surface'
data0Display.AmbientColor = [1.0, 1.0, 1.0]
data0Display.ColorArrayName = ['CELLS', 'rho']
data0Display.DiffuseColor = [1.0, 1.0, 1.0]
data0Display.LookupTable = rhoLUT
data0Display.MapScalars = 1
data0Display.MultiComponentsMapping = 0
data0Display.InterpolateScalarsBeforeMapping = 1
data0Display.Opacity = 1.0
data0Display.PointSize = 2.0
data0Display.LineWidth = 1.0
data0Display.RenderLinesAsTubes = 0
data0Display.RenderPointsAsSpheres = 0
data0Display.Interpolation = 'Gouraud'
data0Display.Specular = 0.0
data0Display.SpecularColor = [1.0, 1.0, 1.0]
data0Display.SpecularPower = 100.0
data0Display.Luminosity = 0.0
data0Display.Ambient = 0.0
data0Display.Diffuse = 1.0
data0Display.EdgeColor = [0.7529411764705882, 0.7647058823529411, 0.6862745098039216]
data0Display.BackfaceRepresentation = 'Follow Frontface'
data0Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
data0Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
data0Display.BackfaceOpacity = 1.0
data0Display.Position = [0.0, 0.0, 0.0]
data0Display.Scale = [1.0, 1.0, 1.0]
data0Display.Orientation = [0.0, 0.0, 0.0]
data0Display.Origin = [0.0, 0.0, 0.0]
data0Display.Pickable = 1
data0Display.Texture = None
data0Display.Triangulate = 0
data0Display.UseShaderReplacements = 0
data0Display.ShaderReplacements = ''
data0Display.NonlinearSubdivisionLevel = 1
data0Display.UseDataPartitions = 0
data0Display.OSPRayUseScaleArray = 0
data0Display.OSPRayScaleArray = ''
data0Display.OSPRayScaleFunction = 'PiecewiseFunction'
data0Display.OSPRayMaterial = 'None'
data0Display.Orient = 0
data0Display.OrientationMode = 'Direction'
data0Display.SelectOrientationVectors = 'None'
data0Display.Scaling = 0
data0Display.ScaleMode = 'No Data Scaling Off'
data0Display.ScaleFactor = 200.0
data0Display.SelectScaleArray = 'rho'
data0Display.GlyphType = 'Arrow'
data0Display.UseGlyphTable = 0
data0Display.GlyphTableIndexArray = 'rho'
data0Display.UseCompositeGlyphTable = 0
data0Display.UseGlyphCullingAndLOD = 0
data0Display.LODValues = []
data0Display.ColorByLODIndex = 0
data0Display.GaussianRadius = 10.0
data0Display.ShaderPreset = 'Sphere'
data0Display.CustomTriangleScale = 3
data0Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
data0Display.Emissive = 0
data0Display.ScaleByArray = 0
data0Display.SetScaleArray = [None, '']
data0Display.ScaleArrayComponent = 0
data0Display.UseScaleFunction = 1
data0Display.ScaleTransferFunction = 'PiecewiseFunction'
data0Display.OpacityByArray = 0
data0Display.OpacityArray = [None, '']
data0Display.OpacityArrayComponent = 0
data0Display.OpacityTransferFunction = 'PiecewiseFunction'
data0Display.DataAxesGrid = 'GridAxesRepresentation'
data0Display.SelectionCellLabelBold = 0
data0Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
data0Display.SelectionCellLabelFontFamily = 'Arial'
data0Display.SelectionCellLabelFontFile = ''
data0Display.SelectionCellLabelFontSize = 18
data0Display.SelectionCellLabelItalic = 0
data0Display.SelectionCellLabelJustification = 'Left'
data0Display.SelectionCellLabelOpacity = 1.0
data0Display.SelectionCellLabelShadow = 0
data0Display.SelectionPointLabelBold = 0
data0Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
data0Display.SelectionPointLabelFontFamily = 'Arial'
data0Display.SelectionPointLabelFontFile = ''
data0Display.SelectionPointLabelFontSize = 18
data0Display.SelectionPointLabelItalic = 0
data0Display.SelectionPointLabelJustification = 'Left'
data0Display.SelectionPointLabelOpacity = 1.0
data0Display.SelectionPointLabelShadow = 0
data0Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
data0Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
data0Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
data0Display.GlyphType.TipResolution = 6
data0Display.GlyphType.TipRadius = 0.1
data0Display.GlyphType.TipLength = 0.35
data0Display.GlyphType.ShaftResolution = 6
data0Display.GlyphType.ShaftRadius = 0.03
data0Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
data0Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
data0Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
data0Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
data0Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
data0Display.DataAxesGrid.XTitle = 'X Axis'
data0Display.DataAxesGrid.YTitle = 'Y Axis'
data0Display.DataAxesGrid.ZTitle = 'Z Axis'
data0Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.XTitleFontFamily = 'Arial'
data0Display.DataAxesGrid.XTitleFontFile = ''
data0Display.DataAxesGrid.XTitleBold = 0
data0Display.DataAxesGrid.XTitleItalic = 0
data0Display.DataAxesGrid.XTitleFontSize = 12
data0Display.DataAxesGrid.XTitleShadow = 0
data0Display.DataAxesGrid.XTitleOpacity = 1.0
data0Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.YTitleFontFamily = 'Arial'
data0Display.DataAxesGrid.YTitleFontFile = ''
data0Display.DataAxesGrid.YTitleBold = 0
data0Display.DataAxesGrid.YTitleItalic = 0
data0Display.DataAxesGrid.YTitleFontSize = 12
data0Display.DataAxesGrid.YTitleShadow = 0
data0Display.DataAxesGrid.YTitleOpacity = 1.0
data0Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
data0Display.DataAxesGrid.ZTitleFontFile = ''
data0Display.DataAxesGrid.ZTitleBold = 0
data0Display.DataAxesGrid.ZTitleItalic = 0
data0Display.DataAxesGrid.ZTitleFontSize = 12
data0Display.DataAxesGrid.ZTitleShadow = 0
data0Display.DataAxesGrid.ZTitleOpacity = 1.0
data0Display.DataAxesGrid.FacesToRender = 63
data0Display.DataAxesGrid.CullBackface = 0
data0Display.DataAxesGrid.CullFrontface = 1
data0Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.ShowGrid = 0
data0Display.DataAxesGrid.ShowEdges = 1
data0Display.DataAxesGrid.ShowTicks = 1
data0Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
data0Display.DataAxesGrid.AxesToLabel = 63
data0Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.XLabelFontFamily = 'Arial'
data0Display.DataAxesGrid.XLabelFontFile = ''
data0Display.DataAxesGrid.XLabelBold = 0
data0Display.DataAxesGrid.XLabelItalic = 0
data0Display.DataAxesGrid.XLabelFontSize = 12
data0Display.DataAxesGrid.XLabelShadow = 0
data0Display.DataAxesGrid.XLabelOpacity = 1.0
data0Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.YLabelFontFamily = 'Arial'
data0Display.DataAxesGrid.YLabelFontFile = ''
data0Display.DataAxesGrid.YLabelBold = 0
data0Display.DataAxesGrid.YLabelItalic = 0
data0Display.DataAxesGrid.YLabelFontSize = 12
data0Display.DataAxesGrid.YLabelShadow = 0
data0Display.DataAxesGrid.YLabelOpacity = 1.0
data0Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
data0Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
data0Display.DataAxesGrid.ZLabelFontFile = ''
data0Display.DataAxesGrid.ZLabelBold = 0
data0Display.DataAxesGrid.ZLabelItalic = 0
data0Display.DataAxesGrid.ZLabelFontSize = 12
data0Display.DataAxesGrid.ZLabelShadow = 0
data0Display.DataAxesGrid.ZLabelOpacity = 1.0
data0Display.DataAxesGrid.XAxisNotation = 'Mixed'
data0Display.DataAxesGrid.XAxisPrecision = 2
data0Display.DataAxesGrid.XAxisUseCustomLabels = 0
data0Display.DataAxesGrid.XAxisLabels = []
data0Display.DataAxesGrid.YAxisNotation = 'Mixed'
data0Display.DataAxesGrid.YAxisPrecision = 2
data0Display.DataAxesGrid.YAxisUseCustomLabels = 0
data0Display.DataAxesGrid.YAxisLabels = []
data0Display.DataAxesGrid.ZAxisNotation = 'Mixed'
data0Display.DataAxesGrid.ZAxisPrecision = 2
data0Display.DataAxesGrid.ZAxisUseCustomLabels = 0
data0Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
data0Display.PolarAxes.Visibility = 0
data0Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
data0Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
data0Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
data0Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
data0Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
data0Display.PolarAxes.EnableCustomRange = 0
data0Display.PolarAxes.CustomRange = [0.0, 1.0]
data0Display.PolarAxes.PolarAxisVisibility = 1
data0Display.PolarAxes.RadialAxesVisibility = 1
data0Display.PolarAxes.DrawRadialGridlines = 1
data0Display.PolarAxes.PolarArcsVisibility = 1
data0Display.PolarAxes.DrawPolarArcsGridlines = 1
data0Display.PolarAxes.NumberOfRadialAxes = 0
data0Display.PolarAxes.AutoSubdividePolarAxis = 1
data0Display.PolarAxes.NumberOfPolarAxis = 0
data0Display.PolarAxes.MinimumRadius = 0.0
data0Display.PolarAxes.MinimumAngle = 0.0
data0Display.PolarAxes.MaximumAngle = 90.0
data0Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
data0Display.PolarAxes.Ratio = 1.0
data0Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.PolarAxisTitleVisibility = 1
data0Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
data0Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
data0Display.PolarAxes.PolarLabelVisibility = 1
data0Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
data0Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
data0Display.PolarAxes.RadialLabelVisibility = 1
data0Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
data0Display.PolarAxes.RadialLabelLocation = 'Bottom'
data0Display.PolarAxes.RadialUnitsVisibility = 1
data0Display.PolarAxes.ScreenSize = 10.0
data0Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.PolarAxisTitleOpacity = 1.0
data0Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
data0Display.PolarAxes.PolarAxisTitleFontFile = ''
data0Display.PolarAxes.PolarAxisTitleBold = 0
data0Display.PolarAxes.PolarAxisTitleItalic = 0
data0Display.PolarAxes.PolarAxisTitleShadow = 0
data0Display.PolarAxes.PolarAxisTitleFontSize = 12
data0Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.PolarAxisLabelOpacity = 1.0
data0Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
data0Display.PolarAxes.PolarAxisLabelFontFile = ''
data0Display.PolarAxes.PolarAxisLabelBold = 0
data0Display.PolarAxes.PolarAxisLabelItalic = 0
data0Display.PolarAxes.PolarAxisLabelShadow = 0
data0Display.PolarAxes.PolarAxisLabelFontSize = 12
data0Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
data0Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
data0Display.PolarAxes.LastRadialAxisTextFontFile = ''
data0Display.PolarAxes.LastRadialAxisTextBold = 0
data0Display.PolarAxes.LastRadialAxisTextItalic = 0
data0Display.PolarAxes.LastRadialAxisTextShadow = 0
data0Display.PolarAxes.LastRadialAxisTextFontSize = 12
data0Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
data0Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
data0Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
data0Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
data0Display.PolarAxes.SecondaryRadialAxesTextBold = 0
data0Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
data0Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
data0Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
data0Display.PolarAxes.EnableDistanceLOD = 1
data0Display.PolarAxes.DistanceLODThreshold = 0.7
data0Display.PolarAxes.EnableViewAngleLOD = 1
data0Display.PolarAxes.ViewAngleLODThreshold = 0.7
data0Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
data0Display.PolarAxes.PolarTicksVisibility = 1
data0Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
data0Display.PolarAxes.TickLocation = 'Both'
data0Display.PolarAxes.AxisTickVisibility = 1
data0Display.PolarAxes.AxisMinorTickVisibility = 0
data0Display.PolarAxes.ArcTickVisibility = 1
data0Display.PolarAxes.ArcMinorTickVisibility = 0
data0Display.PolarAxes.DeltaAngleMajor = 10.0
data0Display.PolarAxes.DeltaAngleMinor = 5.0
data0Display.PolarAxes.PolarAxisMajorTickSize = 0.0
data0Display.PolarAxes.PolarAxisTickRatioSize = 0.3
data0Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
data0Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
data0Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
data0Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
data0Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
data0Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
data0Display.PolarAxes.ArcMajorTickSize = 0.0
data0Display.PolarAxes.ArcTickRatioSize = 0.3
data0Display.PolarAxes.ArcMajorTickThickness = 1.0
data0Display.PolarAxes.ArcTickRatioThickness = 0.5
data0Display.PolarAxes.Use2DMode = 0
data0Display.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [200.0, 1000.0, 10000.0]
renderView1.CameraFocalPoint = [200.0, 1000.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
data0Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [2.4999999292951713e-10, 0.0, 0.5, 0.0, 1.0973419648507843e-06, 1.0, 0.5, 0.0]
rhoPWF.AllowDuplicateScalars = 1
rhoPWF.UseLogScale = 0
rhoPWF.ScalarRangeInitialized = 1

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitVertical(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.UseCache = 0
renderView2.ViewSize = [986, 198]
renderView2.AnnotationColor = [1.0, 1.0, 1.0]
renderView2.UseInteractiveRenderingForScreenshots = 0
renderView2.InteractionMode = '3D'
renderView2.CollectGeometryThreshold = 100.0
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterAxesVisibility = 0
renderView2.OrientationAxesVisibility = 1
renderView2.OrientationAxesInteractivity = 0
renderView2.OrientationAxesLabelColor = [1.0, 1.0, 1.0]
renderView2.OrientationAxesOutlineColor = [1.0, 1.0, 1.0]
renderView2.CenterOfRotation = [0.0, 0.0, 0.0]
renderView2.RotationFactor = 1.0
renderView2.EnableRenderOnInteraction = 1
renderView2.UseLight = 1
renderView2.KeyLightWarmth = 0.6
renderView2.KeyLightIntensity = 0.75
renderView2.KeyLightElevation = 50.0
renderView2.KeyLightAzimuth = 10.0
renderView2.FillLightWarmth = 0.4
renderView2.FillLightKFRatio = 3.0
renderView2.FillLightElevation = -75.0
renderView2.FillLightAzimuth = -10.0
renderView2.BackLightWarmth = 0.5
renderView2.BackLightKBRatio = 3.5
renderView2.BackLightElevation = 0.0
renderView2.BackLightAzimuth = 110.0
renderView2.HeadLightWarmth = 0.5
renderView2.HeadLightKHRatio = 3.0
renderView2.MaintainLuminance = 0
renderView2.HiddenLineRemoval = 0
renderView2.StereoRender = 0
renderView2.StereoType = 0
renderView2.ServerStereoType = 'Same As Client'
renderView2.MultiSamples = 0
renderView2.AlphaBitPlanes = 1
renderView2.StencilCapable = 1
renderView2.CameraPosition = [0.0, 0.0, 6.69]
renderView2.CameraFocalPoint = [0.0, 0.0, 0.0]
renderView2.CameraViewUp = [0.0, 1.0, 0.0]
renderView2.CameraViewAngle = 30.0
renderView2.CameraParallelScale = 1.73
renderView2.EyeAngle = 2.0
renderView2.CameraParallelProjection = 0
renderView2.Background = [0.09411764705882353, 0.10196078431372549, 0.12941176470588237]
renderView2.Background2 = [0.0, 0.0, 0.165]
renderView2.UseGradientBackground = 0
renderView2.UseTexturedBackground = 0
renderView2.BackgroundTexture = None
renderView2.MaxClipBounds = [0.0, -1.0, 0.0, -1.0, 0.0, -1.0]
renderView2.LockBounds = 0
renderView2.DrawCells = 0
renderView2.ArrayNameToDraw = ''
renderView2.ArrayNumberToDraw = 0
renderView2.ValueRenderingMode = 1
renderView2.ArrayComponentToDraw = 0
renderView2.ScalarRange = [0.0, -1.0]
renderView2.EnableOSPRay = 0
renderView2.Shadows = 0
renderView2.OSPRayRenderer = 'scivis'
renderView2.AmbientSamples = 0
renderView2.SamplesPerPixel = 1
renderView2.ProgressivePasses = 1
renderView2.LightScale = 1.0
renderView2.TemporalCacheSize = 0
renderView2.BackgroundNorth = [1.0, 0.0, 0.0]
renderView2.BackgroundEast = [0.0, 1.0, 0.0]
renderView2.AdditionalLights = None
renderView2.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView2.AxesGrid.Visibility = 0
renderView2.AxesGrid.XTitle = 'X Axis'
renderView2.AxesGrid.YTitle = 'Y Axis'
renderView2.AxesGrid.ZTitle = 'Z Axis'
renderView2.AxesGrid.XTitleColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.XTitleOpacity = 1.0
renderView2.AxesGrid.XTitleFontFamily = 'Arial'
renderView2.AxesGrid.XTitleFontFile = ''
renderView2.AxesGrid.XTitleBold = 0
renderView2.AxesGrid.XTitleItalic = 0
renderView2.AxesGrid.XTitleShadow = 0
renderView2.AxesGrid.XTitleFontSize = 12
renderView2.AxesGrid.YTitleColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.YTitleOpacity = 1.0
renderView2.AxesGrid.YTitleFontFamily = 'Arial'
renderView2.AxesGrid.YTitleFontFile = ''
renderView2.AxesGrid.YTitleBold = 0
renderView2.AxesGrid.YTitleItalic = 0
renderView2.AxesGrid.YTitleShadow = 0
renderView2.AxesGrid.YTitleFontSize = 12
renderView2.AxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.ZTitleOpacity = 1.0
renderView2.AxesGrid.ZTitleFontFamily = 'Arial'
renderView2.AxesGrid.ZTitleFontFile = ''
renderView2.AxesGrid.ZTitleBold = 0
renderView2.AxesGrid.ZTitleItalic = 0
renderView2.AxesGrid.ZTitleShadow = 0
renderView2.AxesGrid.ZTitleFontSize = 12
renderView2.AxesGrid.FacesToRender = 63
renderView2.AxesGrid.CullBackface = 0
renderView2.AxesGrid.CullFrontface = 1
renderView2.AxesGrid.GridColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.ShowGrid = 0
renderView2.AxesGrid.ShowEdges = 1
renderView2.AxesGrid.ShowTicks = 1
renderView2.AxesGrid.AxesToLabel = 63
renderView2.AxesGrid.LabelUniqueEdgesOnly = 1
renderView2.AxesGrid.XLabelColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.XLabelOpacity = 1.0
renderView2.AxesGrid.XLabelFontFamily = 'Arial'
renderView2.AxesGrid.XLabelFontFile = ''
renderView2.AxesGrid.XLabelBold = 0
renderView2.AxesGrid.XLabelItalic = 0
renderView2.AxesGrid.XLabelShadow = 0
renderView2.AxesGrid.XLabelFontSize = 12
renderView2.AxesGrid.YLabelColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.YLabelOpacity = 1.0
renderView2.AxesGrid.YLabelFontFamily = 'Arial'
renderView2.AxesGrid.YLabelFontFile = ''
renderView2.AxesGrid.YLabelBold = 0
renderView2.AxesGrid.YLabelItalic = 0
renderView2.AxesGrid.YLabelShadow = 0
renderView2.AxesGrid.YLabelFontSize = 12
renderView2.AxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
renderView2.AxesGrid.ZLabelOpacity = 1.0
renderView2.AxesGrid.ZLabelFontFamily = 'Arial'
renderView2.AxesGrid.ZLabelFontFile = ''
renderView2.AxesGrid.ZLabelBold = 0
renderView2.AxesGrid.ZLabelItalic = 0
renderView2.AxesGrid.ZLabelShadow = 0
renderView2.AxesGrid.ZLabelFontSize = 12
renderView2.AxesGrid.XAxisNotation = 'Mixed'
renderView2.AxesGrid.XAxisPrecision = 2
renderView2.AxesGrid.XAxisUseCustomLabels = 0
renderView2.AxesGrid.XAxisLabels = []
renderView2.AxesGrid.YAxisNotation = 'Mixed'
renderView2.AxesGrid.YAxisPrecision = 2
renderView2.AxesGrid.YAxisUseCustomLabels = 0
renderView2.AxesGrid.YAxisLabels = []
renderView2.AxesGrid.ZAxisNotation = 'Mixed'
renderView2.AxesGrid.ZAxisPrecision = 2
renderView2.AxesGrid.ZAxisUseCustomLabels = 0
renderView2.AxesGrid.ZAxisLabels = []
renderView2.AxesGrid.DataScale = [1.0, 1.0, 1.0]
renderView2.AxesGrid.DataPosition = [0.0, 0.0, 0.0]
renderView2.AxesGrid.DataBoundsScaleFactor = 1.0008
renderView2.AxesGrid.ModelTransformMatrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
renderView2.AxesGrid.ModelBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
renderView2.AxesGrid.UseModelTransform = 0

# place view in the layout
layout1.AssignView(2, renderView2)

# set active source
SetActiveSource(data0)

# show data in view
data0Display_1 = Show(data0, renderView2)

# trace defaults for the display properties.
data0Display_1.Representation = 'Surface'
data0Display_1.AmbientColor = [1.0, 1.0, 1.0]
data0Display_1.ColorArrayName = ['CELLS', 'rho']
data0Display_1.DiffuseColor = [1.0, 1.0, 1.0]
data0Display_1.LookupTable = rhoLUT
data0Display_1.MapScalars = 1
data0Display_1.MultiComponentsMapping = 0
data0Display_1.InterpolateScalarsBeforeMapping = 1
data0Display_1.Opacity = 1.0
data0Display_1.PointSize = 2.0
data0Display_1.LineWidth = 1.0
data0Display_1.RenderLinesAsTubes = 0
data0Display_1.RenderPointsAsSpheres = 0
data0Display_1.Interpolation = 'Gouraud'
data0Display_1.Specular = 0.0
data0Display_1.SpecularColor = [1.0, 1.0, 1.0]
data0Display_1.SpecularPower = 100.0
data0Display_1.Luminosity = 0.0
data0Display_1.Ambient = 0.0
data0Display_1.Diffuse = 1.0
data0Display_1.EdgeColor = [0.7529411764705882, 0.7647058823529411, 0.6862745098039216]
data0Display_1.BackfaceRepresentation = 'Follow Frontface'
data0Display_1.BackfaceAmbientColor = [1.0, 1.0, 1.0]
data0Display_1.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
data0Display_1.BackfaceOpacity = 1.0
data0Display_1.Position = [0.0, 0.0, 0.0]
data0Display_1.Scale = [1.0, 1.0, 1.0]
data0Display_1.Orientation = [0.0, 0.0, 0.0]
data0Display_1.Origin = [0.0, 0.0, 0.0]
data0Display_1.Pickable = 1
data0Display_1.Texture = None
data0Display_1.Triangulate = 0
data0Display_1.UseShaderReplacements = 0
data0Display_1.ShaderReplacements = ''
data0Display_1.NonlinearSubdivisionLevel = 1
data0Display_1.UseDataPartitions = 0
data0Display_1.OSPRayUseScaleArray = 0
data0Display_1.OSPRayScaleArray = ''
data0Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
data0Display_1.OSPRayMaterial = 'None'
data0Display_1.Orient = 0
data0Display_1.OrientationMode = 'Direction'
data0Display_1.SelectOrientationVectors = 'None'
data0Display_1.Scaling = 0
data0Display_1.ScaleMode = 'No Data Scaling Off'
data0Display_1.ScaleFactor = 200.0
data0Display_1.SelectScaleArray = 'rho'
data0Display_1.GlyphType = 'Arrow'
data0Display_1.UseGlyphTable = 0
data0Display_1.GlyphTableIndexArray = 'rho'
data0Display_1.UseCompositeGlyphTable = 0
data0Display_1.UseGlyphCullingAndLOD = 0
data0Display_1.LODValues = []
data0Display_1.ColorByLODIndex = 0
data0Display_1.GaussianRadius = 10.0
data0Display_1.ShaderPreset = 'Sphere'
data0Display_1.CustomTriangleScale = 3
data0Display_1.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
data0Display_1.Emissive = 0
data0Display_1.ScaleByArray = 0
data0Display_1.SetScaleArray = [None, '']
data0Display_1.ScaleArrayComponent = 0
data0Display_1.UseScaleFunction = 1
data0Display_1.ScaleTransferFunction = 'PiecewiseFunction'
data0Display_1.OpacityByArray = 0
data0Display_1.OpacityArray = [None, '']
data0Display_1.OpacityArrayComponent = 0
data0Display_1.OpacityTransferFunction = 'PiecewiseFunction'
data0Display_1.DataAxesGrid = 'GridAxesRepresentation'
data0Display_1.SelectionCellLabelBold = 0
data0Display_1.SelectionCellLabelColor = [0.0, 1.0, 0.0]
data0Display_1.SelectionCellLabelFontFamily = 'Arial'
data0Display_1.SelectionCellLabelFontFile = ''
data0Display_1.SelectionCellLabelFontSize = 18
data0Display_1.SelectionCellLabelItalic = 0
data0Display_1.SelectionCellLabelJustification = 'Left'
data0Display_1.SelectionCellLabelOpacity = 1.0
data0Display_1.SelectionCellLabelShadow = 0
data0Display_1.SelectionPointLabelBold = 0
data0Display_1.SelectionPointLabelColor = [1.0, 1.0, 0.0]
data0Display_1.SelectionPointLabelFontFamily = 'Arial'
data0Display_1.SelectionPointLabelFontFile = ''
data0Display_1.SelectionPointLabelFontSize = 18
data0Display_1.SelectionPointLabelItalic = 0
data0Display_1.SelectionPointLabelJustification = 'Left'
data0Display_1.SelectionPointLabelOpacity = 1.0
data0Display_1.SelectionPointLabelShadow = 0
data0Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
data0Display_1.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
data0Display_1.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
data0Display_1.GlyphType.TipResolution = 6
data0Display_1.GlyphType.TipRadius = 0.1
data0Display_1.GlyphType.TipLength = 0.35
data0Display_1.GlyphType.ShaftResolution = 6
data0Display_1.GlyphType.ShaftRadius = 0.03
data0Display_1.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
data0Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
data0Display_1.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
data0Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
data0Display_1.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
data0Display_1.DataAxesGrid.XTitle = 'X Axis'
data0Display_1.DataAxesGrid.YTitle = 'Y Axis'
data0Display_1.DataAxesGrid.ZTitle = 'Z Axis'
data0Display_1.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.XTitleFontFamily = 'Arial'
data0Display_1.DataAxesGrid.XTitleFontFile = ''
data0Display_1.DataAxesGrid.XTitleBold = 0
data0Display_1.DataAxesGrid.XTitleItalic = 0
data0Display_1.DataAxesGrid.XTitleFontSize = 12
data0Display_1.DataAxesGrid.XTitleShadow = 0
data0Display_1.DataAxesGrid.XTitleOpacity = 1.0
data0Display_1.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.YTitleFontFamily = 'Arial'
data0Display_1.DataAxesGrid.YTitleFontFile = ''
data0Display_1.DataAxesGrid.YTitleBold = 0
data0Display_1.DataAxesGrid.YTitleItalic = 0
data0Display_1.DataAxesGrid.YTitleFontSize = 12
data0Display_1.DataAxesGrid.YTitleShadow = 0
data0Display_1.DataAxesGrid.YTitleOpacity = 1.0
data0Display_1.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.ZTitleFontFamily = 'Arial'
data0Display_1.DataAxesGrid.ZTitleFontFile = ''
data0Display_1.DataAxesGrid.ZTitleBold = 0
data0Display_1.DataAxesGrid.ZTitleItalic = 0
data0Display_1.DataAxesGrid.ZTitleFontSize = 12
data0Display_1.DataAxesGrid.ZTitleShadow = 0
data0Display_1.DataAxesGrid.ZTitleOpacity = 1.0
data0Display_1.DataAxesGrid.FacesToRender = 63
data0Display_1.DataAxesGrid.CullBackface = 0
data0Display_1.DataAxesGrid.CullFrontface = 1
data0Display_1.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.ShowGrid = 0
data0Display_1.DataAxesGrid.ShowEdges = 1
data0Display_1.DataAxesGrid.ShowTicks = 1
data0Display_1.DataAxesGrid.LabelUniqueEdgesOnly = 1
data0Display_1.DataAxesGrid.AxesToLabel = 63
data0Display_1.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.XLabelFontFamily = 'Arial'
data0Display_1.DataAxesGrid.XLabelFontFile = ''
data0Display_1.DataAxesGrid.XLabelBold = 0
data0Display_1.DataAxesGrid.XLabelItalic = 0
data0Display_1.DataAxesGrid.XLabelFontSize = 12
data0Display_1.DataAxesGrid.XLabelShadow = 0
data0Display_1.DataAxesGrid.XLabelOpacity = 1.0
data0Display_1.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.YLabelFontFamily = 'Arial'
data0Display_1.DataAxesGrid.YLabelFontFile = ''
data0Display_1.DataAxesGrid.YLabelBold = 0
data0Display_1.DataAxesGrid.YLabelItalic = 0
data0Display_1.DataAxesGrid.YLabelFontSize = 12
data0Display_1.DataAxesGrid.YLabelShadow = 0
data0Display_1.DataAxesGrid.YLabelOpacity = 1.0
data0Display_1.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
data0Display_1.DataAxesGrid.ZLabelFontFamily = 'Arial'
data0Display_1.DataAxesGrid.ZLabelFontFile = ''
data0Display_1.DataAxesGrid.ZLabelBold = 0
data0Display_1.DataAxesGrid.ZLabelItalic = 0
data0Display_1.DataAxesGrid.ZLabelFontSize = 12
data0Display_1.DataAxesGrid.ZLabelShadow = 0
data0Display_1.DataAxesGrid.ZLabelOpacity = 1.0
data0Display_1.DataAxesGrid.XAxisNotation = 'Mixed'
data0Display_1.DataAxesGrid.XAxisPrecision = 2
data0Display_1.DataAxesGrid.XAxisUseCustomLabels = 0
data0Display_1.DataAxesGrid.XAxisLabels = []
data0Display_1.DataAxesGrid.YAxisNotation = 'Mixed'
data0Display_1.DataAxesGrid.YAxisPrecision = 2
data0Display_1.DataAxesGrid.YAxisUseCustomLabels = 0
data0Display_1.DataAxesGrid.YAxisLabels = []
data0Display_1.DataAxesGrid.ZAxisNotation = 'Mixed'
data0Display_1.DataAxesGrid.ZAxisPrecision = 2
data0Display_1.DataAxesGrid.ZAxisUseCustomLabels = 0
data0Display_1.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
data0Display_1.PolarAxes.Visibility = 0
data0Display_1.PolarAxes.Translation = [0.0, 0.0, 0.0]
data0Display_1.PolarAxes.Scale = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.Orientation = [0.0, 0.0, 0.0]
data0Display_1.PolarAxes.EnableCustomBounds = [0, 0, 0]
data0Display_1.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
data0Display_1.PolarAxes.EnableCustomRange = 0
data0Display_1.PolarAxes.CustomRange = [0.0, 1.0]
data0Display_1.PolarAxes.PolarAxisVisibility = 1
data0Display_1.PolarAxes.RadialAxesVisibility = 1
data0Display_1.PolarAxes.DrawRadialGridlines = 1
data0Display_1.PolarAxes.PolarArcsVisibility = 1
data0Display_1.PolarAxes.DrawPolarArcsGridlines = 1
data0Display_1.PolarAxes.NumberOfRadialAxes = 0
data0Display_1.PolarAxes.AutoSubdividePolarAxis = 1
data0Display_1.PolarAxes.NumberOfPolarAxis = 0
data0Display_1.PolarAxes.MinimumRadius = 0.0
data0Display_1.PolarAxes.MinimumAngle = 0.0
data0Display_1.PolarAxes.MaximumAngle = 90.0
data0Display_1.PolarAxes.RadialAxesOriginToPolarAxis = 1
data0Display_1.PolarAxes.Ratio = 1.0
data0Display_1.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.PolarAxisTitleVisibility = 1
data0Display_1.PolarAxes.PolarAxisTitle = 'Radial Distance'
data0Display_1.PolarAxes.PolarAxisTitleLocation = 'Bottom'
data0Display_1.PolarAxes.PolarLabelVisibility = 1
data0Display_1.PolarAxes.PolarLabelFormat = '%-#6.3g'
data0Display_1.PolarAxes.PolarLabelExponentLocation = 'Labels'
data0Display_1.PolarAxes.RadialLabelVisibility = 1
data0Display_1.PolarAxes.RadialLabelFormat = '%-#3.1f'
data0Display_1.PolarAxes.RadialLabelLocation = 'Bottom'
data0Display_1.PolarAxes.RadialUnitsVisibility = 1
data0Display_1.PolarAxes.ScreenSize = 10.0
data0Display_1.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.PolarAxisTitleOpacity = 1.0
data0Display_1.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
data0Display_1.PolarAxes.PolarAxisTitleFontFile = ''
data0Display_1.PolarAxes.PolarAxisTitleBold = 0
data0Display_1.PolarAxes.PolarAxisTitleItalic = 0
data0Display_1.PolarAxes.PolarAxisTitleShadow = 0
data0Display_1.PolarAxes.PolarAxisTitleFontSize = 12
data0Display_1.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.PolarAxisLabelOpacity = 1.0
data0Display_1.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
data0Display_1.PolarAxes.PolarAxisLabelFontFile = ''
data0Display_1.PolarAxes.PolarAxisLabelBold = 0
data0Display_1.PolarAxes.PolarAxisLabelItalic = 0
data0Display_1.PolarAxes.PolarAxisLabelShadow = 0
data0Display_1.PolarAxes.PolarAxisLabelFontSize = 12
data0Display_1.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.LastRadialAxisTextOpacity = 1.0
data0Display_1.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
data0Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
data0Display_1.PolarAxes.LastRadialAxisTextBold = 0
data0Display_1.PolarAxes.LastRadialAxisTextItalic = 0
data0Display_1.PolarAxes.LastRadialAxisTextShadow = 0
data0Display_1.PolarAxes.LastRadialAxisTextFontSize = 12
data0Display_1.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
data0Display_1.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
data0Display_1.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
data0Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''
data0Display_1.PolarAxes.SecondaryRadialAxesTextBold = 0
data0Display_1.PolarAxes.SecondaryRadialAxesTextItalic = 0
data0Display_1.PolarAxes.SecondaryRadialAxesTextShadow = 0
data0Display_1.PolarAxes.SecondaryRadialAxesTextFontSize = 12
data0Display_1.PolarAxes.EnableDistanceLOD = 1
data0Display_1.PolarAxes.DistanceLODThreshold = 0.7
data0Display_1.PolarAxes.EnableViewAngleLOD = 1
data0Display_1.PolarAxes.ViewAngleLODThreshold = 0.7
data0Display_1.PolarAxes.SmallestVisiblePolarAngle = 0.5
data0Display_1.PolarAxes.PolarTicksVisibility = 1
data0Display_1.PolarAxes.ArcTicksOriginToPolarAxis = 1
data0Display_1.PolarAxes.TickLocation = 'Both'
data0Display_1.PolarAxes.AxisTickVisibility = 1
data0Display_1.PolarAxes.AxisMinorTickVisibility = 0
data0Display_1.PolarAxes.ArcTickVisibility = 1
data0Display_1.PolarAxes.ArcMinorTickVisibility = 0
data0Display_1.PolarAxes.DeltaAngleMajor = 10.0
data0Display_1.PolarAxes.DeltaAngleMinor = 5.0
data0Display_1.PolarAxes.PolarAxisMajorTickSize = 0.0
data0Display_1.PolarAxes.PolarAxisTickRatioSize = 0.3
data0Display_1.PolarAxes.PolarAxisMajorTickThickness = 1.0
data0Display_1.PolarAxes.PolarAxisTickRatioThickness = 0.5
data0Display_1.PolarAxes.LastRadialAxisMajorTickSize = 0.0
data0Display_1.PolarAxes.LastRadialAxisTickRatioSize = 0.3
data0Display_1.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
data0Display_1.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
data0Display_1.PolarAxes.ArcMajorTickSize = 0.0
data0Display_1.PolarAxes.ArcTickRatioSize = 0.3
data0Display_1.PolarAxes.ArcMajorTickThickness = 1.0
data0Display_1.PolarAxes.ArcTickRatioThickness = 0.5
data0Display_1.PolarAxes.Use2DMode = 0
data0Display_1.PolarAxes.UseLogAxis = 0

# show color bar/color legend
data0Display_1.SetScalarBarVisibility(renderView2, True)

# reset view to fit data
renderView2.ResetCamera()

# set scalar coloring
ColorBy(data0Display_1, ('CELLS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(rhoLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
data0Display_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
data0Display_1.SetScalarBarVisibility(renderView2, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')
tLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
tLUT.InterpretValuesAsCategories = 0
tLUT.AnnotationsInitialized = 0
tLUT.ShowCategoricalColorsinDataRangeOnly = 0
tLUT.RescaleOnVisibilityChange = 0
tLUT.EnableOpacityMapping = 0
tLUT.RGBPoints = [3400.0, 0.231373, 0.298039, 0.752941, 3400.25, 0.865003, 0.865003, 0.865003, 3400.5, 0.705882, 0.0156863, 0.14902]
tLUT.UseLogScale = 0
tLUT.ColorSpace = 'Diverging'
tLUT.UseBelowRangeColor = 0
tLUT.BelowRangeColor = [0.0, 0.0, 0.0]
tLUT.UseAboveRangeColor = 0
tLUT.AboveRangeColor = [0.5, 0.5, 0.5]
tLUT.NanColor = [1.0, 1.0, 0.0]
tLUT.NanOpacity = 1.0
tLUT.Discretize = 1
tLUT.NumberOfTableValues = 256
tLUT.ScalarRangeInitialized = 1.0
tLUT.HSVWrap = 0
tLUT.VectorComponent = 0
tLUT.VectorMode = 'Magnitude'
tLUT.AllowDuplicateScalars = 1
tLUT.Annotations = []
tLUT.ActiveAnnotatedValues = []
tLUT.IndexedColors = []
tLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')
tPWF.Points = [3400.0, 0.0, 0.5, 0.0, 3400.5, 1.0, 0.5, 0.0]
tPWF.AllowDuplicateScalars = 1
tPWF.UseLogScale = 0
tPWF.ScalarRangeInitialized = 1

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

#change interaction mode for render view
renderView2.InteractionMode = '2D'

#change interaction mode for render view
renderView2.InteractionMode = '3D'

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

#change interaction mode for render view
renderView2.InteractionMode = '2D'

# set active view
SetActiveView(renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [195.91129606895933, 1108.666546292415, 10000.0]
renderView1.CameraFocalPoint = [195.91129606895933, 1108.666546292415, 0.0]
renderView1.CameraViewUp = [-1.0, 2.220446049250313e-16, 0.0]
renderView1.CameraParallelScale = 268.54624084911296

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [206.75946807491718, 1099.5202088295666, 3940.2197095449555]
renderView2.CameraFocalPoint = [206.75946807491718, 1099.5202088295666, 0.0]
renderView2.CameraViewUp = [-1.0, 2.220446049250313e-16, 0.0]
renderView2.CameraParallelScale = 268.54624084911296

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
