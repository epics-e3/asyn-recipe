require asyn

epicsEnvSet("ECHO_PORT", "37681")

drvAsynIPPortConfigure("ECHO", "127.0.0.1:$(ECHO_PORT)", 0, 0, 0)
asynOctetSetInputEos("ECHO", 0, "\n")
asynOctetSetOutputEos("ECHO", 0, "\n")

dbLoadRecords("$(asyn_DB)/asynRecord.db", "P=TEST:,R=asyn1,PORT=ECHO,ADDR=0,OMAX=80,IMAX=80")
dbLoadRecords("$(E3_CMD_TOP)/test.db", "P=TEST:,PORT=ECHO,ADDR=0")
