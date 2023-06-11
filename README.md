# Raster tile map generation benchmarking

A collection of docker files used to benchmark tile generation software and scripts. Most of these images are just the official images for the respective tile generation softwares with [hyperfine](https://github.com/sharkdp/hyperfine) added. Was used in the bachelor's thesis [The Server-side of Tiled Raster Web Maps: benchmarking and evaluating static raster tile map generation tools for geospatial data processing and visualization](https://www.theseus.fi/handle/10024/800013)

## Benchmark results
![](/docs/benchmarks.png)

|                     | COG to JPEG | COG to PNG | COG to WEBP | JP2 to JPEG | JP2 to PNG | JP2 to WEBP |
|---------------------|-------------|------------|-------------|-------------|------------|-------------|
| ctb-tile            | 209.358     | 288.706    | 247.566     | 697.819     | 775.139    | 944.983     |
| gdal2tiles          | N/A         | 573.102    | 312.204     | N/A         | 152.518    | 88.837      |
| gdal2tiles_parallel | 58.605      | 147.538    | N/A         | 171.121     | 260.293    | N/A         |
| gdal2tiles_mp       | N/A         | 229.855    | N/A         | N/A         | 340.669    | N/A         |

