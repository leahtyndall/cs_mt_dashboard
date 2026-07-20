Run dashboard.py & go to IP adress given to access dashboard

Dependencies:
- numpy
- dash
- dash-bootstrap-components
- pandas
- plotly
- requests
- tinytuya
- websocket-client
- scipy

Summary of files:
- assets - images, cvs data files, txt logic files ect
- APIs - Connect to Mir/shelly to handle requests
- defs.py - Defines missions from mir
- mirStatus.py - retrieves status info from mir
- missions.py - contains docking/undocking sequences & other buttons on dash
- network.py - to be updated...void?
- networkMap.py - records robot position and signal strength data to be plotted
- rosDiagnostics.py - recieves signal level from mir ros driver
- shellyGateControl.py - runs gate control
- shellyStatsdorMir.py - gets status of gate (combine^?)
- layout2.py - plotly dash layout of dashboard
- dashboard.py - handles all call backs, creates map plot
