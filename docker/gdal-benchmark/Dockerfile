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

# command for creating a docker image based on the this file:
# docker build -t gdal-test:latest .

# This image is used for becnchmarking gdal_translate and gdal2tiles. 