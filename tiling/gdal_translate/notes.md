# GDAL translate

## GDAL installation
- windows 64 bit builds are available via conda forge 
- Debian packages are now available on Debian Unstable
- it can also be built from source 
- nightly versions as docker images


### instructions

```
conda update -n base -c conda-forge conda
conda create --name gdal_master_env
conda activate gdal_master_env
conda install -c conda-forge mamba
mamba install -c gdal-master gdal
```



## Yo

```
docker run -v D:\VMs\docker:/data -t -i gdal-test:latest bash
```


```
mkdir /data/tiles 
hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'ctb-tile --output-format JPEG --profile mercator -o ./tiles ./source.tif'


cd data 
hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'gdal2tiles.py -p mercator -s EPSG:3857 -z 8-18 --exclude -w none --xyz --tilesize=256 ./source.tif ./tiles'
```

```
Benchmark 1: gdal2tiles.py -p mercator -s EPSG:3857 -z 8-18 --exclude -w none --xyz --tilesize=256 ./source.tif ./tiles
  Time (mean ± σ):     139.506 s ±  0.272 s    [User: 85.529 s, System: 5.485 s]
  Range (min … max):   139.193 s … 139.689 s    3 runs
```




gdal_translate in.tif out.tif -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW

Web Mercator TileMatrixSet (or a World CRS84 TileMatrixSet)

## Creating COG 
gdalwarp -t_srs "EPSG:3857" /data/source.tif /data/epsg-3857-source.tif
gdal_translate /data/epsg-3857-source.tif /data/cog-source.tif -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW