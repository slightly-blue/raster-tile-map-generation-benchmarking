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

