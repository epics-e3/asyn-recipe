#!/bin/bash

# LIBVERSION shall only include MAJOR.MINOR.PATCH for require
LIBVERSION=$(echo ${PKG_VERSION}| cut -d'.' -f1-3)

# Clean between variants builds
make clean

make DRV_USBTMC=YES MODULE=${PKG_NAME} LIBVERSION=${LIBVERSION}
make DRV_USBTMC=YES MODULE=${PKG_NAME} LIBVERSION=${LIBVERSION} db
make DRV_USBTMC=YES MODULE=${PKG_NAME} LIBVERSION=${LIBVERSION} install

