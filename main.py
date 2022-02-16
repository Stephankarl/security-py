import os
import json

class Alarm:
    def __init__(self):
      self.last_update=0.0
      self.json_data={}
      self.loop_status={}
      self.state={}
    def check_json(self):
        '''
        Checks the JSON control file and updates the required components status
        '''
        last_saved=os.path.getmtime("/Users/casey/VSCode/Control.json")
        if self.last_update != last_saved:
            self.last_update = last_saved
            f=open('/Users/casey/VSCode/Control.json','r') #fix this file path
            control_json=json.load(f) 
            self.json_data=control_json
            self.loop_status=control_json #Temp only. The main script will do the updating
            self.update_state() #Temp only. The main script will do the updating
        else:
            pass
    def update_state(self):
        '''
        Updates the State.json file when ever there is a change to the state of the system
        '''
        if self.loop_status == self.state:
            pass
        else:
            json_data=json.dumps(self.loop_status)
            f=open('/Users/casey/VSCode/State.json', 'w') #fix this file path
            f.write(json_data)
            f.close()
            self.state=self.loop_status
            print("State.json file updated")

alarm = Alarm()

while True:
    alarm.check_json()