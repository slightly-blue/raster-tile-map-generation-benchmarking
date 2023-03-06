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


## Yo

```
docker run -v D:\VMs\docker:/data -t -i gdal-parallel-test:latest bash
```


```
cd data
hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'python gdal2tiles_parallel.py -p mercator -e -z 15 -f JPEG /data/source.tif /data/tiles'

hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'python3 gdal2tiles_mp.py --zoom 12-20 --profile=mercator -a 0,0,0 /source.tif ./tiles'

cd data 
hyperfine --runs 3 --prepare 'rm -r /data/tiles/*' 'gdal2tiles.py -p mercator -s EPSG:3857 -z 8-18 --exclude -w none --xyz --tilesize=256 ./source.tif ./tiles'
```



**These work**
```
python gdal2tiles_parallel.py -p mercator -e -z 15 -f JPEG /data/source.tif /data/tiles
python gdal2tiles_mp.py -p mercator -z 15 /data/source.tif /data/tiles
```

`gdal2tiles_mp.py` does not have a way to specify output image format 
[this line seem to indicate that only png tiles are supported](https://github.com/parallelo-ai/gdal2tiles_mp/blob/baa8bf775005a55f76bf703749f0464ac3e20827/gdal2tiles_mp.py#L1390)