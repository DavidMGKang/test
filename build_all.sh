#!/bin/bash

####Script to build lighttpd for KARA-S and PINETREE

## pleas edit below JUNIPER_REPO for you own!!
export JUNIPER_REPO="/home/kangmg/sdk/kara_pinetree/juniper"
export CFLAGS="-mapcs-frame -Wall -mlittle-endian -Wno-unknown-pragmas -fno-strict-aliasing -mmarvell-div -mcpu=marvell-fv7 -mfloat-abi=hard"

function build_libxml2()
{
   cd $WEBSERVER_DIR
   rm -rf libxml2-2.9.2
   tar -xvzf libxml2-2.9.2.tar.gz && cd libxml2-2.9.2 && mkdir libxml_install
   ./configure --host=arm-marvell-linux --target=arm-marvell-linux-gnueabi CC=arm-marvell-linux-gnueabi-gcc AR=arm-marvell-linux-gnueabi-ar LD=arm-marvell-linux-gnueabi-ld RANLIB=arm-marvell-linux-gnueabi-ranlib  STRIP=arm-marvell-linux-gnueabi-strip --prefix=$PWD/libxml_install --with-minimum --with-writer --without-lzma --with-tree && make && make install-strip || exit 1
   cd $PWD/libxml_install
   cp -a `find . -name "*.so*"` ${WEBSERVER_DIR}/lib   
}

function build_libzip()
{
   cd $WEBSERVER_DIR
   rm -rf libzip-0.11.2
   tar -xvzf libzip-0.11.2.tar.gz && cd libzip-0.11.2 && mkdir libzip_install
   ./configure --host=arm-marvell-linux --target=arm-marvell-linux-gnueabi CC=arm-marvell-linux-gnueabi-gcc AR=arm-marvell-linux-gnueabi-ar LD=arm-marvell-linux-gnueabi-ld RANLIB=arm-marvell-linux-gnueabi-ranlib STRIP=arm-marvell-linux-gnueabi-strip --prefix=$PWD/libzip_install --with-zlib=$PRJROOT/sysapps/zlib/ZLib_output && make && make install-strip || exit 1
   cd $PWD/libzip_install
   cp -a `find . -name "*.so*"` ${WEBSERVER_DIR}/lib
}

function build_libpcre()
{
   cd $WEBSERVER_DIR
   rm -rf pcre-8.37
   tar -xvzf pcre-8.37.tar.gz && cd pcre-8.37 
    ./configure --host=arm-marvell-linux-gnueabi --prefix=$WEBSERVER_DIR/pcre-8.37/pcre_install && make && make install-strip || exit 1
   cd $PWD/pcre_install
   cp -a `find . -name "*.so*"` ${WEBSERVER_DIR}/lib
}


function build_lighttpd()
{
	cd $WEBSERVER_DIR
	rm -rf lighttpd-1.4.41
	tar -xvzf lighttpd-1.4.41.tar.gz && cd lighttpd-1.4.41
	export CFLAGS="$CFLAGS -I$PRJROOT/sysapps/include -I$PRJROOT/sysapps/zlib -I$JUNIPER_REPO/latest/WebServerDesign/pcre-8.37/pcre_install/include -I$JUNIPER_REPO/latest/WebServerDesign/pcre-8.37/pcre_install/include -I$JUNIPER_REPO/latest/WebServerDesign/cgi-bin/application/ "
	export LDFLAGS="-L$PRJROOT/newroot/lib -L$JUNIPER_REPO/latest/WebServerDesign/pcre-8.37/pcre_install/lib -L$JUNIPER_REPO/latest/WebServerDesign/libxml2-2.9.2/libxml_install/lib -L$JUNIPER_REPO/latest/WebServerDesign/cgi-bin/commonLibrary/ -L$PRJROOT/newroot/lib"
	export LIBS="-lz -lssl -lcrypto"
	export PATH=/opt/armcc.mv61x0/bin:$PATH
	rm -rf $PWD/LIGHTTPD_TEST/sbin
	rm -rf $PWD/LIGHTTPD_TEST/lib
	rm -rf $PWD/LIGHTTPD_TEST/share
	make distclean
	CC=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-gcc CXX=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-g++ AR=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-ar LD=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-ld NM=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-nm RANLIB=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-ranlib STRIP=/opt/armcc.mv61x0/bin/arm-marvell-linux-gnueabi-strip ./configure --host=arm-marvell-linux-gnueabi --prefix=$PWD/LIGHTTPD_TEST --without-bzip2 --with-pcre=$JUNIPER_REPO/latest/WebServerDesign/pcre-8.37/pcre_install --with-webdav-props --with-openssl  --with-openssl-libs=$PRJROOT/newroot/lib --with-openssl-includes=$PRJROOT/sysapps/include --with-zlib=$PRJROOT/sysapps/zlib/ZLib_output

	make && make install || exit 1

}

if [ -z "$PRJROOT" ]; then echo "Need to set PRJROOT"; exit 1; fi

export PATH=/opt/armcc.mv61x0/bin:$PATH
export WEBSERVER_DIR=$PWD
cd $WEBSERVER_DIR
rm -rf ./lib
mkdir ./lib
echo "Building libxml2"
build_libxml2
echo "Building libzip"
build_libzip
echo "Building pcre"
build_libpcre
echo "Building lighttpd"
build_lighttpd

