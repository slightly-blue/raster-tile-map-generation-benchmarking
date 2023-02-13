# A comparison between XYZ raster tile generation pipelines

Raster tile servers

1. Test all alternatives pre generated served with nginx 
2. Test if it can be used to pre generate tiles 


### A

Static Formats 
- XYZ PNG tiles
- XYZ WebP tiles 
- XYZ COG tiles 

Comparisons 
- size on disk 
- frontend load time
- processing cost to generate tile set (e.g. compute time and required memory)


### B

Software capabilities 
- What formats can they generate 
- What input formats are supported 
- What software stack is used (Node, Python, OS)

Comparisons 
- processing cost to generate tile set (e.g. compute time and required memory)



### C
A completely dynamic system based on a minimal storage dataset with no overviews or tiling.
would probably be pretty expensive in cost. EC2 Compute instance + S3 Storage instance. 
-> additional complexity and cost with no real benefits 

Reviewing this as part of my thesis would make it noncohesive and a bit weird since the system I would propose doesn't really exist, nor do it make economical sense from any angle. 

S3 Standard - stockholm 
$0.023 per GB
$0.0004 per 1,000 requests

EC2 - t2.small 
$0.0248 per hour 




## For each solution:
- on the fly 
  - time to generate tiles
  - total tile size on disk 
- pre generated 
  - server response time


## TODO
1. dynamic tiling 
2. test all solutions
3. start writing
4. fredde meeting 
5. benchmark 

## LATER
- utred språk karina kiukas akademi chef 
- create a git repo with each alternative separate folder 
- make sure each work 
- CSC account, check if bucket exist, 

# Notes
## Dynamic Tiling 
  - utred Cloud-Optimized GeoTIFF (COG) format  [good article](https://kylebarron.dev/blog/cog-mosaic/overview)
  - [official page](https://www.cogeo.org/)
  - COG https://medium.com/devseed/cog-talk-part-1-whats-new-941facbcd3d1
  - [mosaic json](https://github.com/developmentseed/mosaicjson-spec)  (like gdal VRT)
  - [article on building cogs with gdal](https://sean-rennie.medium.com/cogs-in-production-e9a42c7f54e4)






# Dynamic tiling
static catalog / dynamic catalog 

## Ecosystem 
- rio-tile: generates mercator XYZ tiles (has plugins for special purposes)
- cogeo-mosaic: Python library to create MosaicJSON files
- titiler:
- rio-cogeo: create COG files

## Flow
1. Create COG files (these take less space than other solutions)
2. MosaicJSON (like gdal VRT but for cog files, think of it as instructions sent to the tiler. Seems to mostly be used for requesting files from AWS or other cloud tile services )
3. serve trough titiler?
X. COGs can be generated with GDAL from VSTs 

Can COG files be served statically? Yes, as long as the client knows what to ask for
[DeckGL COG library](https://kylebarron.dev/deck.gl-raster/get-started/)



# All tile formats
- Vector
  - Mapbox Vector Tile (MVT) 
- Raster
  - TMS tiles (OSGeo) : TileCache 
  - XYZ tiles (slippy map tilenames) : OpenStreetMap, Bing maps, Google Maps, ESRI
  - QuadTiles (or quadkey) : Bing maps
  - WMS (web map service):  Used by professional GIS software
  - WMTS (web map tiled service) : Lefalet



# Software

## Node 
- https://turfjs.org/ (a modular GeoJson library)
- https://mapnik.org/ (low level library that many other solutions are built on) (little to no documentation)


## Display
- [Leaflet](https://react-leaflet.js.org/)
- [OpenLayers3]()
- [Cesium]()
- [mapbox.js]
- [vts-browser-js](https://github.com/melowntech/vts-browser-js)
- [polymaps](http://polymaps.org/docs/) : can also generate slippy maps 
- [modest maps](http://modestmaps.com/)[git](https://github.com/modestmaps/modestmaps-js) : (requires java)
- 

## Other helpful software
- Merkaartor (OpenStreetMap editor for Linux, macOS and Windows)
- QGIS (map editor & Viewer)

? JOSM, iD, Potlatch 2, and Merkaartor,


# Abbreviations
WMS = Web Map Service
TMS = Tile Mapping Service


## References 
[Tile-Based Geospatial Information Systems (Book)](https://link.springer.com/book/10.1007/978-1-4419-7631-4)



## Criteria
- opensource
- maintained libraries 
- hosting services in europe 


## Cog tradeoffs 
- more detail at lower zoom
- OR fast perceived load when navigating the frontend  

## Why raster tile servers in a world where vector data exist?
Raster tiles makes sense when the source material is in raster format.
- satellite imagery
- maps based on drone footage 
- infra red scans
- ground penetrating radar 

For many data visualization purposes Vector tiles are better in every aspect.




## Raster tile formats

[mapbox](https://docs.mapbox.com/api/maps/raster-tiles/)
- .grid.json	  UTFGrid
- .png	        True color PNG
- .png32	      32 color indexed PNG
- .png64	      64 color indexed PNG
- .png128	      128 color indexed PNG
- .png256	      256 color indexed PNG
- .jpg	        80% quality JPG
- .jpg70	      70% quality JPG
- .jpg80	      80% quality JPG
- .jpg90	      90% quality JPG
- .webp	        80% quality WebP


[](https://www.microimages.com/documentation/TechGuides/78tileFormats.pdf)
- jpeg
- png
- GeoTIFF
- GeoJP2



Other factors:
- supported tile sizes 
- color depth
- compression
- transparency


## Load analysis 
- 


Tile convention 
Tile protocol 
Tile Map service specification 

## Tiled web map standards (protocols?)
- TMS 
- WMTS (xyz)
- WMS (complex)
- XYZ 
- TileJSON (metadata ? wrapper for xyz or tms)
- Bing Maps Tile System (using quad keys for addresssing)



[protocols src](https://gis.stackexchange.com/questions/132242/what-are-the-differences-between-tms-xyz-wmts)

- OGC Specification for Geopackage?

## TODO IDEAS

- create a frontend for ingesting the backend 
- a module for testing features of a tile server?

## A comparison between XYZ raster tile generation pipelines

**Software to test**
- ctb-tile
- gdal2tiles
- gdal2tiles_parallel
- rio-tiler
- rio-cogeo(?)
- gdal_translate

**Software capabilities**
- File formats supported 
- tile standards supported 
- supported tile sizes 
- color depth
- compression
- transparency
- processing cost to generate tile set (e.g. compute time and required memory)

**File formats to test**
- PNG	
- JPEG	
- WebP
- COG

**Format capabilities**
- size on disk 
- frontend load time
- processing cost to generate tile set (e.g. compute time and required memory)




# Frontend
simplest possible openlayers frontend [quickstart guide](https://openlayers.org/doc/quickstart.html)