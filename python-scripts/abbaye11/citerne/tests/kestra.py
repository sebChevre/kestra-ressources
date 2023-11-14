
from kestra import Kestra
import json
from datetime import datetime

#Conversion vers python dict
data = json.loads({{outputs['load-stats'].body}})

# Recup de l'objet reponse, list
response = data['DeviceResponse']

#Conversion date lastUdate, parsing
lastUpdateDt = datetime.strptime(response[0]['LastUpdate'], "{{ vars.citerne_api.last_updatedate_format }}").replace(microsecond=0).astimezone().isoformat()

reportDt = datetime.today().replace(microsecond=0).astimezone().isoformat()
# Creation du nouvel objet json


newJson = {
"ActualVolume": response[0]['ActualVolume'],
"MaxVolume": response[0]['MaxVolume'],
"ActualVolume": response[0]['ActualVolume'],
"TemperatureF": response[0]['Temperature'],
"ActualVolumePerCent": response[0]['ActualVolumePercent'],
"Battery": response[0]['Battery'],
"LastUpdate": { "$date" : lastUpdateDt },
"DateExport": { "$date" : reportDt  }
}
Kestra.outputs({'reportJson': json.dumps(newJson)})
Kestra.outputs({'reportObject': newJson})