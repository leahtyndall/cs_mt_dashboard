#import API.APIshelly as APIshelly, API.APImir as APImir
import layout.Funcs.API.APIshelly as APIshelly, layout.Funcs.API.APImir as APImir
import time
import json

get = APIshelly.get
request = APIshelly.Request
post = APIshelly.post
id = "?id=0"
on = "&on=true"
off = "&on=false"

#funcs----------------------------------------------
def status():
    print("Switch status: ",flush=True)
    status = get("Switch.GetStatus" + id)

    return status ##

def openG():
    extend = get("Switch.Set" + id+on)
    print("Opening", flush = True)
    return extend

def close():
    retract = get("Switch.Set" +id+off)
    print("Closing",flush=True)
    return retract

#-----logic to open gate when 4 meters away-------------
def disToTarget():
    statusData = APImir.mirRequest("GET", "/status") 
    return round(statusData.get("distance_to_next_target"))


def openGate():
    while disToTarget() > 4 or disToTarget() == 0:
        time.sleep(1)
        #print(disToTarget())     
        if disToTarget() < 4:
            break
    print(f"{disToTarget()}m away, Opening gates")
    return openG()
#---------------------------------------------------
#----info-------------------------------------------
def info():
    info =  get("Shelly.GetDeviceInfo")
    print('INFO:')
    print(info)
    return info

def status():
    status = get("Shelly.GetStatus")
    print('STATUS:')
    print(status)
    return status

def config():
    config = get("Shelly.GetConfig")
    print('CONFIG:')
    print(config)
    return config

def methods():
    methods = get("Shelly.ListMethods")
    print('METHODS:')
    print(methods)
    return methods

def currScriptID():

    return currScriptID
#-----for dashboard---------------------------------
def getStatus():
    status = get("Shelly.GetStatus")
    return status
    
def shellyState():
    status = getStatus()
    statusJSON = json.loads(status)
    state = statusJSON['switch:0']['output']
    #print(state)
    if state == True:
        gateOn()
    if state == False:
        gateOff()
    return state
    
def gateOn():
    with open('layout/assets/gateStat.txt', 'wt') as p:
        p.write('1')
    return

def gateOff():
    with open('layout/assets/gateStat.txt', 'wt') as p:
        p.write('0')
    return

