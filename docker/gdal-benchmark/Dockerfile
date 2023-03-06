FROM osgeo/gdal:ubuntu-full-latest

# Install the application. 
# ubuntu apt and apt-get does not have hyperfine so we will need 
# to install it trough cargo
# Inspired by: https://stackoverflow.com/questions/49676490/when-installing-rust-toolchain-in-docker-bash-source-command-doesnt-work

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


# I used the following command to create the image inside 
# the directory with this file 

# docker build -t gdal-test:latest .

# This image is used for gdal_translate, gdal2tiles, 