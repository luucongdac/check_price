#! /bin/bash
# This bash use to install Qt enviroment.
#   1. Setup msys2.
#       + setup_msys2.sh
#   2. Build dependencies.
#   3. Build Qt

PWD=`pwd`
Qt_version="5.1.0"
Qt_git_url=""

build_openssl(){
    OPENSSL_URL="https://www.openssl.org/source/openssl-1.0.1e.tar.gz"
    curl ${OPENSSL_URL} --out openssl-1.0.1e.tar.gz
    tar -zxvf openssl-1.0.1e.tar.gz
    cd openssl-1.0.1e
    ./Configure --prefix=${PWD}/../dist/ no-idea no-mdc2 no-rc5 shared mingw64
    make depend && make && make install
    cd ..
}

build_icu() {
    git clone "https://github.com/unicode-org/icu.git"
    cd "icu/icu4c/source"
    ./runConfigureICU MinGW prefix=$PWD/../dist
    cp config/mh-mingw64 ./config/mh-unknown
    make && make install
    cd "../../../"
}

main() {
    # run setup_msys2.sh to install dependence package.
    ./setup_msys.sh
    # create directory
    mkdir -p "/c/Qt/qt5_deps"

    # build openssl, icu (unicode support)
    pushd "/c/Qt/qt5_deps"
        build_openssl
        #cp ${PWD}/../dist/bin/*.dll /c/Qt/qt5/qtbase/bin
        build_icu
    popd

    # install qt
    pushd "/c/Qt/"
        git clone
        cd qt5
        git checkout v5.10.0
        ./init-repository
    popd
}


# main entry

main $@
