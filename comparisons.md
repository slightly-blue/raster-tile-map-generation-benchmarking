

Frontend raster tile ingestion  
|Package|PNG | JPEG | WebP | GeoTIFF | COG |  GeoJP2| TMS tiles (OSGeo) | XYZ tiles (slippy map tilenames)| Other tiling |
|---|---|---|---|---|---|---|---|---|---|
|Leaflet| | | | | | | | | | |
|OpenLayers3| | | | | | | | | | |
|Cesium| | | | | | | | | | |
|mapbox.js| | | | | | | | | | |
|vts-browser-js| | | | | | | | | | |
|polymaps| | | | | | | | | | |
|modest maps| | | | | | | | | | |
|DeckGL     | | | | | Yes*| | | | | |
|titiler viwer| | | | | | | | | | |

\* with extensions 

\** with unofficial extensions 


rio-viz
titler-digitaltwin


Tile size: width x height 


Other factors:
- supported tile sizes 
- color depth
- compression
- transparency



Backend raster tile Generation
||opensource|maintained||q|
|---|---|---|---|---|
|ctb-tile|||||
|gdal2tiles|
|gdal2tiles_parallel|
|rio-tiler|
|rio-cogeo(?)|
|[gdal_translate ](https://github.com/cogeotiff/cog-spec/blob/master/spec.md#how-to-generate-it-with-gdal)|
||
||
||
||
||

Backend raster tile server
- titiler (allows more creative requests to COG files or )(comes with viwers)
- static webserver (nginx / apache)
- [terracotta](https://github.com/DHI-GRAS/terracotta)