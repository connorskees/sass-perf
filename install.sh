# install rust
curl https://sh.rustup.rs -sSf | sh -s -- -y

# install the latest version of grass
cargo install grass --force
grass --version

# install dart-sass
wget https://github.com/sass/dart-sass/releases/download/1.57.1/dart-sass-1.57.1-linux-x64.tar.gz
tar -xvzf dart-sass-1.57.1-linux-x64.tar.gz
./dart-sass/sass --version

# install sassc (libsass)
git clone https://github.com/sass/sassc.git
git clone https://github.com/sass/libsass.git
make -C sassc -j4
./sassc/bin/sassc --version

# install sass libraries
git clone https://github.com/twbs/bootstrap --branch v4.1.3 --depth 1
git clone https://github.com/jgthms/bulma --depth 1
git clone https://github.com/zaydek/duomo --branch v0.7.12 --depth 1

git clone https://github.com/carbon-design-system/ibm-cloud-cognitive --branch @carbon/ibm-cloud-cognitive@1.0.0-rc.0 --depth 1


git clone https://github.com/alex-page/sass-a11ycolor
cd sass-a11ycolor
git checkout 2e7ef93ec06f8bbec80b632863e4b2811618af89
cd ..



# install hyperfine for benchmarking
cargo install hyperfine

# generate input files
python3 generate.py

