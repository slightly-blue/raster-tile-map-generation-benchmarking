# rio tiler

At the low level, rio-tiler is just a wrapper around the rasterio and GDAL libraries.[1](https://github.com/cogeotiff/rio-tiler)

rio-tiler aims to be a lightweight plugin for rasterio to read slippy map tiles from a raster sources.


rio-tiler was initially designed to create slippy map tiles from large raster data sources and render these tiles dynamically on a web map. 

The purpose of rio-tiler is therefore to be used in a DYNAMIC context and only makes sense when comparing towards other server alternatives. ( for example titiler is built with rio-tiler)  

For dynamic use and specifically a package for use in a larger dynamic context 

```
pip install -U pip
pip install -U rio-tiler
```

The absolutely easiest way to generate tiles  

## Startup

```
docker run -v D:\VMs\docker:/data -t -i rio-tile-test:latest  bash
```
