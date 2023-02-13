# parallel versions of gadal2tiles
- [gdal2tiles_parallel](https://github.com/GitHubRGI/geopackage-python/wiki/Usage-Instructions-for-gdal2tiles_parallel.py)
- [gdal2tiles_mp](https://github.com/parallelo-ai/gdal2tiles_mp)
  - multiprocessing 


## usage 
### gdal2tiles_mp
- download files
- have gdal isntalled `
- run using command 

```
python3 gdal2tiles_mp.py --zoom 12-20 --profile=mercator -a 0,0,0 USA_IFR_Low_Alaska_RESIZE.tif`
```


### gdal2tiles_parallel.py


The script relies on Python 2.7.x, GDAL core, and the GDAL Python bindings.
```
python gdal2tiles_parallel.py -p mercator -e -z 15 /data/raw/WhiteHorse.tif /data/tiles/mercator/WhiteHorse_tiles
```