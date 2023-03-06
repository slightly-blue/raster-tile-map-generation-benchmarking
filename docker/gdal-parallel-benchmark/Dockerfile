FROM osgeo/gdal:ubuntu-full-latest

RUN apt-get -qq update
RUN apt-get install -y -q \
    build-essential \
    curl

# Installing rust (required for hyperfine on ubuntu)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Add .cargo/bin to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# installing hyperfine 
RUN cargo install hyperfine

# gdal2tiles_parallel.py
RUN curl https://raw.githubusercontent.com/GitHubRGI/geopackage-python/master/Tiling/gdal2tiles_parallel.py --output gdal2tiles_parallel.py

# gdal2tiles_mp.py
RUN curl https://raw.githubusercontent.com/parallelo-ai/gdal2tiles_mp/master/gdal2tiles_mp.py --output gdal2tiles_mp.py


# command for creating a dcker image based on the this file:
# docker build -t gdal-parallel-test:latest .

# This image is used for becnchmarking gdal2tiles_parallel and gdal2tiles_mp, 