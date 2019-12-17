#
#  Copyright (c) 2017 - 2019  Jeong Han Lee
#  Copyright (c) 2017 - 2019  European Spallation Source ERIC
#
#  The program is free software: you can redistribute
#  it and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 2 of the
#  License, or any newer version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program. If not, see https://www.gnu.org/licenses/gpl-2.0.txt
#
# Author  : Jeong Han Lee
# email   : jeonghan.lee@gmail.com
# Date    : Wednesday, September  4 00:01:38 CEST 2019
# version : 0.1.6


LEGACY_RSET = YES

where_am_I := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
include $(E3_REQUIRE_TOOLS)/driver.makefile


USR_CFLAGS   += -Wno-unused-variable
USR_CFLAGS   += -Wno-unused-function
USR_CFLAGS   += -Wno-unused-but-set-variable
USR_CPPFLAGS += -Wno-unused-variable
USR_CPPFLAGS += -Wno-unused-function
USR_CPPFLAGS += -Wno-unused-but-set-variable



ASYN = asyn

# Default Dependency order of the sources 
# for the community epics makefile
# 

DEVGPIB:=$(ASYN)/devGpib
VXI11:=$(ASYN)/vxi11
ASYNRECORD:=$(ASYN)/asynRecord
DEVEPICS:=$(ASYN)/devEpics
ASYNPORTCLIENT:=$(ASYN)/asynPortClient
ASYNPORTDRIVER:=$(ASYN)/asynPortDriver
MISCELLANEOUS:=$(ASYN)/miscellaneous
INTERFACES:=$(ASYN)/interfaces
DRVASYNSERIAL:=$(ASYN)/drvAsynSerial
ASYNGPIB:=$(ASYN)/asynGpib
ASYNDRIVER:=$(ASYN)/asynDriver


USR_INCLUDES += -I$(where_am_I)$(DEVGPIB)
USR_INCLUDES += -I$(where_am_I)$(VXI11)
USR_INCLUDES += -I$(where_am_I)$(ASYNRECORD)
USR_INCLUDES += -I$(where_am_I)$(DEVEPICS)
USR_INCLUDES += -I$(where_am_I)$(ASYNPORTDRIVER)
USR_INCLUDES += -I$(where_am_I)$(ASYNPORTDRIVER)/exceptions
USR_INCLUDES += -I$(where_am_I)$(MISCELLANEOUS)
USR_INCLUDES += -I$(where_am_I)$(INTERFACES)
USR_INCLUDES += -I$(where_am_I)$(DRVASYNSERIAL)
USR_INCLUDES += -I$(where_am_I)$(ASYNGPIB)
USR_INCLUDES += -I$(where_am_I)$(ASYNDRIVER)


#
HEADERS += $(ASYNDRIVER)/asynDriver.h
HEADERS += $(ASYNDRIVER)/epicsInterruptibleSyscall.h

SOURCES += $(ASYNDRIVER)/asynManager.c
SOURCES += $(ASYNDRIVER)/epicsInterruptibleSyscall.c


#
HEADERS += $(ASYNGPIB)/asynGpibDriver.h
SOURCES += $(ASYNGPIB)/asynGpib.c


#
HEADERS += $(DRVASYNSERIAL)/drvAsynSerialPort.h
SOURCES += $(DRVASYNSERIAL)/drvAsynSerialPort.c
DBDS    += $(DRVASYNSERIAL)/drvAsynSerialPort.dbd


HEADERS += $(DRVASYNSERIAL)/drvAsynIPPort.h
SOURCES += $(DRVASYNSERIAL)/drvAsynIPPort.c
SOURCES += $(DRVASYNSERIAL)/drvAsynIPServerPort.c
DBDS    += $(DRVASYNSERIAL)/drvAsynIPPort.dbd
HEADERS += $(DRVASYNSERIAL)/drvAsynIPServerPort.h

#
HEADERS += $(INTERFACES)/asynInt32.h
HEADERS += $(INTERFACES)/asynInt32SyncIO.h
HEADERS += $(INTERFACES)/asynUInt32Digital.h
HEADERS += $(INTERFACES)/asynUInt32DigitalSyncIO.h
HEADERS += $(INTERFACES)/asynFloat64.h
HEADERS += $(INTERFACES)/asynFloat64SyncIO.h
HEADERS += $(INTERFACES)/asynInt8Array.h
HEADERS += $(INTERFACES)/asynInt8ArraySyncIO.h
HEADERS += $(INTERFACES)/asynInt16Array.h
HEADERS += $(INTERFACES)/asynInt16ArraySyncIO.h
HEADERS += $(INTERFACES)/asynInt32Array.h
HEADERS += $(INTERFACES)/asynInt32ArraySyncIO.h
HEADERS += $(INTERFACES)/asynFloat32Array.h
HEADERS += $(INTERFACES)/asynFloat32ArraySyncIO.h
HEADERS += $(INTERFACES)/asynFloat64Array.h
HEADERS += $(INTERFACES)/asynFloat64ArraySyncIO.h
HEADERS += $(INTERFACES)/asynOctet.h
HEADERS += $(INTERFACES)/asynOctetSyncIO.h
HEADERS += $(INTERFACES)/asynGenericPointer.h
HEADERS += $(INTERFACES)/asynGenericPointerSyncIO.h
HEADERS += $(INTERFACES)/asynEnum.h
HEADERS += $(INTERFACES)/asynEnumSyncIO.h
HEADERS += $(INTERFACES)/asynCommonSyncIO.h
HEADERS += $(INTERFACES)/asynOption.h
HEADERS += $(INTERFACES)/asynOptionSyncIO.h
HEADERS += $(INTERFACES)/asynDrvUser.h
HEADERS += $(INTERFACES)/asynStandardInterfaces.h


SOURCES += $(INTERFACES)/asynInt32Base.c
SOURCES += $(INTERFACES)/asynInt32SyncIO.c
SOURCES += $(INTERFACES)/asynInt8ArrayBase.c
SOURCES += $(INTERFACES)/asynInt8ArraySyncIO.c
SOURCES += $(INTERFACES)/asynInt16ArrayBase.c
SOURCES += $(INTERFACES)/asynInt16ArraySyncIO.c
SOURCES += $(INTERFACES)/asynInt32ArrayBase.c
SOURCES += $(INTERFACES)/asynInt32ArraySyncIO.c
SOURCES += $(INTERFACES)/asynUInt32DigitalBase.c
SOURCES += $(INTERFACES)/asynUInt32DigitalSyncIO.c
SOURCES += $(INTERFACES)/asynFloat64Base.c
SOURCES += $(INTERFACES)/asynFloat64SyncIO.c
SOURCES += $(INTERFACES)/asynFloat32ArrayBase.c
SOURCES += $(INTERFACES)/asynFloat32ArraySyncIO.c
SOURCES += $(INTERFACES)/asynFloat64ArrayBase.c
SOURCES += $(INTERFACES)/asynFloat64ArraySyncIO.c
SOURCES += $(INTERFACES)/asynOctetBase.c
SOURCES += $(INTERFACES)/asynOctetSyncIO.c
SOURCES += $(INTERFACES)/asynGenericPointerBase.c
SOURCES += $(INTERFACES)/asynGenericPointerSyncIO.c
SOURCES += $(INTERFACES)/asynEnumBase.c
SOURCES += $(INTERFACES)/asynEnumSyncIO.c
SOURCES += $(INTERFACES)/asynCommonSyncIO.c
SOURCES += $(INTERFACES)/asynOptionSyncIO.c
SOURCES += $(INTERFACES)/asynStandardInterfacesBase.c


#
DBDS    += $(MISCELLANEOUS)/asyn.dbd
HEADERS += $(MISCELLANEOUS)/asynShellCommands.h
HEADERS += $(MISCELLANEOUS)/asynInterposeCom.h
HEADERS += $(MISCELLANEOUS)/asynInterposeEos.h
HEADERS += $(MISCELLANEOUS)/asynInterposeFlush.h

SOURCES += $(MISCELLANEOUS)/asynShellCommands.c
SOURCES += $(MISCELLANEOUS)/asynInterposeCom.c
SOURCES += $(MISCELLANEOUS)/asynInterposeEos.c
SOURCES += $(MISCELLANEOUS)/asynInterposeFlush.c


# From R4-36 : show two new files such as
# SOURCES += $(MISCELLANEOUS)/asynInterposeDelay.c
# SOURCES += $(MISCELLANEOUS)/asynInterposeEcho.c
# We have to use the following tricks to keep the backward compatibility.
asynInterposeDelay_src += $(MISCELLANEOUS)/asynInterposeDelay.c
SOURCES += $(filter $(asynInterposeDelay_src), $(wildcard $(MISCELLANEOUS)/*.c))
asynInterposeEcho_src += $(MISCELLANEOUS)/asynInterposeEcho.c
SOURCES += $(filter $(asynInterposeEcho_src), $(wildcard $(MISCELLANEOUS)/*.c))

#
HEADERS += $(ASYNPORTDRIVER)/exceptions/ParamListInvalidIndex.h
HEADERS += $(ASYNPORTDRIVER)/exceptions/ParamListParamNotFound.h
HEADERS += $(ASYNPORTDRIVER)/exceptions/ParamValNotDefined.h
HEADERS += $(ASYNPORTDRIVER)/exceptions/ParamValStringSizeRequestTooBig.h
HEADERS += $(ASYNPORTDRIVER)/exceptions/ParamValWrongType.h
HEADERS += $(ASYNPORTDRIVER)/exceptions/ParamValValueNotChanged.h

SOURCES += $(ASYNPORTDRIVER)/exceptions/ParamListInvalidIndex.cpp
SOURCES += $(ASYNPORTDRIVER)/exceptions/ParamListParamNotFound.cpp
SOURCES += $(ASYNPORTDRIVER)/exceptions/ParamValNotDefined.cpp
SOURCES += $(ASYNPORTDRIVER)/exceptions/ParamValStringSizeRequestTooBig.cpp
SOURCES += $(ASYNPORTDRIVER)/exceptions/ParamValWrongType.cpp
SOURCES += $(ASYNPORTDRIVER)/exceptions/ParamValValueNotChanged.cpp


HEADERS += $(ASYNPORTDRIVER)/asynParamType.h
HEADERS += $(ASYNPORTDRIVER)/paramErrors.h
HEADERS += $(ASYNPORTDRIVER)/asynPortDriver.h
# paramVal.h is needed only for nds for LLRF
HEADERS += $(ASYNPORTDRIVER)/paramVal.h
SOURCES += $(ASYNPORTDRIVER)/paramVal.cpp
SOURCES += $(ASYNPORTDRIVER)/asynPortDriver.cpp

#
HEADERS += $(ASYNPORTCLIENT)/asynPortClient.h
SOURCES += $(ASYNPORTCLIENT)/asynPortClient.cpp



#
DBDS      += $(DEVEPICS)/devAsynOctet.dbd
DBDS      += $(DEVEPICS)/devAsynInt32.dbd
DBDS      += $(DEVEPICS)/devAsynInt8Array.dbd
DBDS      += $(DEVEPICS)/devAsynInt16Array.dbd
DBDS      += $(DEVEPICS)/devAsynInt32Array.dbd
DBDS      += $(DEVEPICS)/devAsynInt32TimeSeries.dbd
DBDS      += $(DEVEPICS)/devAsynUInt32Digital.dbd
DBDS      += $(DEVEPICS)/devAsynFloat64.dbd
DBDS      += $(DEVEPICS)/devAsynFloat32Array.dbd
DBDS      += $(DEVEPICS)/devAsynFloat64Array.dbd
DBDS      += $(DEVEPICS)/devAsynFloat64TimeSeries.dbd
DBDS      += $(DEVEPICS)/devEpics.dbd


TEMPLATES += $(DEVEPICS)/asynInt32TimeSeries.db
TEMPLATES += $(DEVEPICS)/asynFloat64TimeSeries.db

HEADERS   += $(DEVEPICS)/asynEpicsUtils.h

SOURCES   += $(DEVEPICS)/devAsynOctet.c
SOURCES   += $(DEVEPICS)/asynEpicsUtils.c
SOURCES   += $(DEVEPICS)/devAsynInt32.c
SOURCES   += $(DEVEPICS)/devAsynInt8Array.c
SOURCES   += $(DEVEPICS)/devAsynInt16Array.c
SOURCES   += $(DEVEPICS)/devAsynInt32Array.c
SOURCES   += $(DEVEPICS)/devAsynInt32TimeSeries.c
SOURCES   += $(DEVEPICS)/devAsynUInt32Digital.c
SOURCES   += $(DEVEPICS)/devAsynFloat64.c
SOURCES   += $(DEVEPICS)/devAsynFloat32Array.c
SOURCES   += $(DEVEPICS)/devAsynFloat64Array.c
SOURCES   += $(DEVEPICS)/devAsynFloat64TimeSeries.c


DBDINC_SRCS += $(ASYNRECORD)/asynRecord.c
DBDINC_DBDS = $(subst .c,.dbd,   $(DBDINC_SRCS:$(ASYNRECORD)/%=%))
DBDINC_HDRS = $(subst .c,.h,     $(DBDINC_SRCS:$(ASYNRECORD)/%=%))
DBDINC_DEPS = $(subst .c,$(DEP), $(DBDINC_SRCS:$(ASYNRECORD)/%=%))

HEADERS   += $(DBDINC_HDRS)
SOURCES   += $(ASYNRECORD)/drvAsyn.c
SOURCES   += $(DBDINC_SRCS)
DBDS      += $(ASYNRECORD)/devAsynRecord.dbd

TEMPLATES += $(ASYNRECORD)/asynRecord.db




ifeq ($(TIRPC),YES)
ifeq ($(T_A),linux-ppc64e6500)
  USR_INCLUDES += -I$(SDKTARGETSYSROOT)/usr/include/tirpc
else
  USR_INCLUDES += -I/usr/include/tirpc
endif
  LIB_SYS_LIBS += tirpc
endif


#HEADERS += $(VXI11)/drvVxi11.h
#HEADERS += $(VXI11)/osiRpc.h
HEADERS += $(VXI11)/rpc/vxi11core.h
HEADERS += $(VXI11)/rpc/vxi11intr.h
#HEADERS += $(VXI11)/vxi11.h

SOURCES += $(VXI11)/rpc/vxi11intr_xdr.c
SOURCES += $(VXI11)/rpc/vxi11core_xdr.c
SOURCES += $(VXI11)/drvVxi11.c
SOURCES += $(VXI11)/E5810Reboot.c
SOURCES += $(VXI11)/E2050Reboot.c
SOURCES += $(VXI11)/TDS3000Reboot.c
DBDS    += $(VXI11)/drvVxi11.dbd


#
# driver.Makefile can add USR_INCLUDES and USR_LDFLAGS
# when we compile it.
# However, it doesn't include SOURCES and DBD file, thus
# we cannot use DBDS and SOURCES to add USBTMC.c and USBTMC.dbd.
# Try-and-Fail, found DBD_SRCS and SRCS
DRVASYNUSBTMC:=$(ASYN)/drvAsynUSBTMC
DRVASYNUSBTMC_SRC:=$(DRVASYNUSBTMC)/drvAsynUSBTMC.c
DRVASYNUSBTMC_DBD:= $(DRVASYNUSBTMC)/drvAsynUSBTMC.dbd

ifeq ($(DRV_USBTMC),YES)
ifeq ($(T_A),linux-x86_64)
  USR_INCLUDES += -I$(PREFIX)/include/libusb-1.0
  USR_LDFLAGS  += -lusb-1.0
  DBD_SRCS += $(DRVASYNUSBTMC_DBD)
  SRCS     += $(DRVASYNUSBTMC_SRC)
endif
endif

#
HEADERS += $(DEVGPIB)/devGpib.h
HEADERS += $(DEVGPIB)/devSupportGpib.h
HEADERS += $(DEVGPIB)/devCommonGpib.h
SOURCES += $(DEVGPIB)/devCommonGpib.c
SOURCES += $(DEVGPIB)/devSupportGpib.c
SOURCES += $(DEVGPIB)/boSRQonOff.c
DBDS    += $(DEVGPIB)/devGpib.dbd

SCRIPTS += $(wildcard ./iocsh/*.iocsh)


# For 3.14
#drvVxi11$(OBJ): ../$(VXI11)/vxi11intr.h
# For 3.15
#drvVxi11$(DEP): ../$(VXI11)/vxi11intr.h ../$(VXI11)/vxi11core.h
#vxi11core_xdr.c$(DEP): ../$(VXI11)/vxi11core.h


$(DBDINC_DEPS): $(DBDINC_HDRS)

.dbd.h:
	$(DBTORECORDTYPEH)  $(USR_DBDFLAGS) -o $@ $<




# db rule is the default in RULES_E3, so add the empty one

db:
#
vlibs:
#
.PHONY: vlibs db
