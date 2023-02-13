# convert multiple .jp2 to tif
# (Retrospectively I realize this step could maybe have been skipped, have not tried it though)
import os
from osgeo import gdal

path = "C:/Users/<username>/Desktop/mml-data/orto"
arr = os.listdir(path)

for file in arr:
  print("transforming " + file)
  ds = gdal.Open("C:/Users/<username>/Desktop/mml-data/orto/" + file)
  ds = gdal.Translate("D:/cartography-project/" + file.removesuffix(".jp2") + ".tif", ds)
  ds = None 

# Build a virtual image file. (-addalpha prevents generation of black tiles further along the line)
os.system("gdalbuildvrt -addalpha D:/cartography-service/vrt/tile-src-alpha.vrt  D:/cartography-project/*.tif")

gdal.UseExceptions() 

# VRT KKJ to VRT WSG84 ESPG:3857
gdal.Warp("D:/cartography-service/vrt/warped-full-alpha.vrt", "D:/cartography-service/vrt/tile-src-alpha.vrt", dstSRS="EPSG:3857")

# Cut Municipality 
os.system("gdalwarp -cutline D:/cartography-service/cutout/borga.shp D:/cartography-service/vrt/warped-full-alpha.vrt  D:/cartography-service/vrt/warped-full-alpha-cut.vrt")

# Should automatically detect alpha and exclude those tiles
os.system("gdal2tiles.py -p mercator -s EPSG:3857 -z 8-18 --exclude -w none --xyz --tilesize=256 D:/cartography-service/vrt/warped-full-alpha-cut.vrt D:/cartography-service/version-2")
