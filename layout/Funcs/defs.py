#from tuya_relay_python import connect_to_relay 
#from layout.Funcs.tuya_relay_python import connect_to_relay 
import layout.Funcs.basicFunctions as basicFunctions
import time
#######################################################################
#network
#######################################################################
mul_lab = "38c554e6-b68b-43cd-b4a1-b7f7cbc714c5"
rosIP = "192.168.30.25" #"192.168.30.116"
#map
WS_URL = "ws://192.168.30.25:8765"  # your Foxglove websocket server
SUBPROTOCOL = "foxglove.websocket.v1"



allBays = "bd07dd40-7461-11f1-80be-f44d306dcb63"
#######################################################################
#missions
#######################################################################
chargingStation = "76a5ddbd-75ff-11f1-a0a7-f44d306dcb63"
DropDown = "4082a527-76b9-11f1-a507-f44d306dcb63" 
MarathonTest = "c0ec2b88-7613-11f1-a056-f44d306dcb63" #UPDATE
B3Demo = "07e06440-7478-11f1-9f07-f44d306dcb63"
LeahsDesk = "1bd779cf-76b7-11f1-a507-f44d306dcb63" 
apprG1 = "ef103854-76b6-11f1-a507-f44d306dcb63"
enterG1 = "912913b9-76b0-11f1-a507-f44d306dcb63"
ExitGate1 = "f4e45c86-76af-11f1-a507-f44d306dcb63"
leaveCharger = "afeece9e-76c7-11f1-ae32-f44d306dcb63"

#######################################################################
## footprints
#######################################################################
defaultFootprint = '11d39594-283c-11f1-8f8d-f44d306dcb63'
footprintWithShelf = '54b23ee4-283b-11f1-8f8d-f44d306dcb63'


#######################################################################
## Shelf 
#######################################################################
dockToShelfB1 = "064d772c-75f0-11f1-a0a7-f44d306dcb63"
dockToShelfB2 =  "c059dd5f-75f1-11f1-a0a7-f44d306dcb63"
leaveDock = "16200ac6-76c2-11f1-ae32-f44d306dcb63"
plc12 = "b41361fe-7477-11f1-9f07-f44d306dcb63" 
plc2add = "d999e717-7477-11f1-9f07-f44d306dcb63"
plc2reset = "ed573610-7477-11f1-9f07-f44d306dcb63"


