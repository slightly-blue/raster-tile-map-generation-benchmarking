FROM homme/cesium-terrain-builder:latest

# Installing hyperfine

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


# command for creating a dcker image based on the this file:
# docker build -t ctb-tile-test:latest .

# This image is used for becnchmarking ctb-tile