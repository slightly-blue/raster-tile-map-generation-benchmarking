# CTB-TILE
## Cesium terrain builder 

[docs](https://github.com/geo-data/cesium-terrain-builder)



# Installation & Requirements 
Ensure GDAL >= 2.0.0 is installed


- A. build from source
- B. [use docker](https://registry.hub.docker.com/r/homme/cesium-terrain-builder)

# features / input
- Mainly meant for creating Digital Elevation Model (DEM)


Command line tools:
- ctb-tile: create gzipped terrain tiles from a GDAL raster
- ctb-info : provides various information on a terrain tile, mainly useful for debugging purposes.
- ctb-export:  exports a terrain tile to GeoTiff format
- ctb-extents: outputs json files for each zoom level with the extents that ctb tile would produce  




// docker start  --output-format JPEG --profile mercator \ --output-dir ./jpeg-tiles  'D:\cartography-project\L4321G.tif' ctb-tile
// 
// docker run --rm homme/cesium-terrain-builder --output-format JPEG --profile mercator \ --output-dir ./jpeg-tiles 'D:\cartography-project\L4321G.tif'


[docker docs for ctb-tiles](https://github.com/geo-data/cesium-terrain-builder/tree/master/docker)

```
docker pull homme/cesium-terrain-builder:latest
```

```
docker run -v D:\VMs\docker:/data -t -i homme/cesium-terrain-builder:latest bash
```
```

mkdir /data/tiles && ctb-tile --output-format JPEG --profile mercator -o ./tiles ./source.tif
```


create a docker container based on the original & add hyperfine.
gdal docker is based on ubuntu trusty 



## my docker 
created the image with ` docker build -t ctb-tile-test:latest .`
And the docker file in this folder 

```
docker run -v D:\VMs\docker:/data -t -i ctb-tile-test:latest bash
```


```
mkdir /data/tiles 
hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'ctb-tile --output-format JPEG --profile mercator -o ./tiles ./source.tif'
```

```
Benchmark 1: ctb-tile --output-format JPEG --profile mercator -o ./tiles ./source.tif
  Time (mean ± σ):     314.404 s ±  1.128 s    [User: 827.048 s, System: 1829.855 s]
  Range (min … max):   313.510 s … 315.671 s    3 runs
```

## How do we make sure the measurement is relevant?
- consistent
- same env as the other 


Best solution. Run container on a known cloud service.
Create a benchmark that can be easily duplicated 

## Features

```
  -V, --version                 output program version
  -h, --help                    output help information
  -o, --output-dir <dir>        specify the output directory for the tiles (defaults to working directory)
  -f, --output-format <format>  specify the output format for the tiles. This is either `Terrain` (the default) or any format listed by `gdalinfo --formats`
  -p, --profile <profile>       specify the TMS profile for the tiles. This is either `geodetic` (the default) or `mercator`
  -c, --thread-count <count>    specify the number of threads to use for tile generation. On multicore machines this defaults to the number of CPUs
  -t, --tile-size <size>        specify the size of the tiles in pixels. This defaults to 65 for terrain tiles and 256 for other GDAL formats
  -s, --start-zoom <zoom>       specify the zoom level to start at. This should be greater than the end zoom level
  -e, --end-zoom <zoom>         specify the zoom level to end at. This should be less than the start zoom level and >= 0
  -r, --resampling-method <algorithm> specify the raster resampling algorithm.  One of: nearest; bilinear; cubic; cubicspline; lanczos; average; mode; max; min; med; q1; q3. Defaults to average.
  -n, --creation-option <option> specify a GDAL creation option for the output dataset in the form NAME=VALUE. Can be specified multiple times. Not valid for Terrain tiles.
  -z, --error-threshold <threshold> specify the error threshold in pixel units for transformation approximation. Larger values should mean faster transforms. Defaults to 0.125
  -m, --warp-memory <bytes>     The memory limit in bytes used for warp operations. Higher settings should be faster. Defaults to a conservative GDAL internal setting.
  -R, --resume                  Do not overwrite existing files
  -q, --quiet                   only output errors
  -v, --verbose                 be more noisy
```

## Benchmark 

```
mkdir /data/tiles 
hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'ctb-tile --output-format JPEG --profile mercator -o ./tiles ./source.tif'
```