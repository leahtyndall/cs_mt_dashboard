import layout.Funcs.API.APImir as APImir
import layout.Funcs.MIRstatus as MIRstatus
import layout.Funcs.defs as defs
import layout.Funcs.shellyGateControl as shellyGateControl
import time
#
statusData = APImir.mirRequest("GET", "/status") 
dis = MIRstatus.disToTarget()
#robot actions

def clearqueue():
    return APImir.mirRequest("DELETE", "/mission_queue")                   
                      
def doMission(mission_id):
    data = {"mission_id": mission_id}
    return APImir.mirRequest("POST","/mission_queue", data)

def disToTarget():
    statusData = APImir.mirRequest("GET", "/status") 
    return round(statusData.get("distance_to_next_target"))

def openGate():
    while disToTarget() > 5 or disToTarget() == 0:
        time.sleep(1)
        #print(disToTarget())     

        if disToTarget() < 5:
            break
    print(f"{disToTarget()}m away, Opening gates")
    return shellyGateControl.open()


#--------------------------------------------------------------------------------------------------------------------------
#main method
if __name__ == "__main__":


 
    time.sleep(2)
    print("on my way dawg")
    clearqueue()
    #approach gate
    doMission(defs.ApproachGate1)
    #check if open??????????
        #closed -> open it
    openGate()
    time.sleep(1)
    doMission(defs.Desk1)
    time.sleep(2)
   
    doMission(defs.ExitGate1)
    openGate()
    time.sleep(2)
    doMission(defs.LeahsDesk)

