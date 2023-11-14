from kestra import Kestra
import json
import pytz
from datetime import datetime

#Conversion vers python dict
citerne_stats = json.loads({{outputs['load-citerne-stats'].body}})

# Recup de l'objet reponse, list
response = citerne_stats['DeviceResponse']

#Conversion date lastUdate
lastUpdateDt = datetime.strptime(response[0]['LastUpdate'], "{{ vars.citerne_api.last_updatedate_format }}").replace(microsecond=0).replace(tzinfo=pytz.timezone('CET')).isoformat()

#Creation DateExport
reportDt = datetime.today().replace(tzinfo=pytz.timezone('CET')).replace(microsecond=0).isoformat()

# Creation de l'objet à persister
atlas_document = {
    "ActualVolume": response[0]['ActualVolume'],
    "MaxVolume": response[0]['MaxVolume'],
    "ActualVolume": response[0]['ActualVolume'],
    "TemperatureF": response[0]['Temperature'],
    "ActualVolumePerCent": response[0]['ActualVolumePercent'],
    "Battery": response[0]['Battery'],
    "LastUpdate": { "$date" : lastUpdateDt },
    "DateExport": { "$date" : reportDt  }
}

atlas_request_body = {
    "dataSource": "{{ vars.atlas.cluster }}",
    "database": "{{ vars.atlas.database }}",
    "collection" : "{{ vars.atlas.collection }}",
    "document": atlas_document
}

#Stockage interne
Kestra.outputs({ "atlas_request_body": json.dumps(atlas_request_body)})