
import json

def str_to_dict(str1):
    str1 = '{"' + str1\
    .replace("b","")\
    .replace('"', '')\
    .replace("'", '')\
    .replace(",", '","')\
    .replace("=", '":"')\
    .replace("&", '","')\
    .replace("PASSKEY:", 'PASSKEY":"') + '"}'

    dict1 = json.loads(str1)

    return dict1

def str_map_emb(input_str,timestr):

    convertedDict = str_to_dict(input_str)

    sensorDict = {
        'soilmoisture1' : float(convertedDict['soilmoisture1']),
        'soilatt1' : float(convertedDict['soilatt1']),
        'soilmoisture2' : float(convertedDict['soilmoisture2']),
        'soilatt2' : float(convertedDict['soilatt2']),
        'soilmoisture3' : float(convertedDict['soilmoisture3']),
        'soilatt3' : float(convertedDict['soilatt3'])
    }

    outputDict = {
        'doctype' : 'station',
        'stationtype' : str(convertedDict['stationtype']),
        'eventtime' : str(convertedDict['dateutc']),
        'processingtime' : timestr,
        'tempinf' : float(convertedDict['tempinf']),
        'humidityin' : float(convertedDict['humidityin']),
        'aromrelin' : float(convertedDict['aromrelin']),
        'aromasin' : float(convertedDict['aromasin']),
        'freq' : str(convertedDict['freq']),
        'model' : str(convertedDict['model']),
        'soilsensors' : sensorDict
    }
   
    return outputDict

def str_map_ref(input_str,timestr):

    convertedDict = str_to_dict(input_str)

    str1 = '{"' + str1\
    .replace("b","")\
    .replace('"', '')\
    .replace("'", '')\
    .replace(",", '","')\
    .replace("=", '":"')\
    .replace("&", '","')\
    .replace("PASSKEY:", 'PASSKEY":"') + '"}'

    convertedDict = json.loads(str1)

    sensorDict1 = {
        'doctype' : 'sensor',
        'sensorid' : '1',
        'eventtime' : str(convertedDict['dateutc']),
        'processingtime' : timestr,
        'soilmoisture' : float(convertedDict['soilmoisture1']),
        'soilatt' : float(convertedDict['soilatt1']),
    }

    sensorDict2 = {
        'doctype' : 'sensor',
        'sensorid' : '2',
        'eventtime' : str(convertedDict['dateutc']),
        'processingtime' : timestr,
        'soilmoisture' : float(convertedDict['soilmoisture2']),
        'soilatt' : float(convertedDict['soilatt2']),
    }

    sensorDict3 = {
        'doctype' : 'sensor',
        'sensorid' : '3',
        'eventtime' : str(convertedDict['dateutc']),
        'processingtime' : timestr,
        'soilmoisture' : float(convertedDict['soilmoisture3']),
        'soilatt' : float(convertedDict['soilatt3']),
    }

    stationDict = {
        'doctype' : 'station',
        'stationtype' : str(convertedDict['stationtype']),
        'eventtime' : str(convertedDict['dateutc']),
        'processingtime' : timestr,
        'tempinf' : float(convertedDict['tempinf']),
        'humidityin' : float(convertedDict['humidityin']),
        'aromrelin' : float(convertedDict['aromrelin']),
        'aromasin' : float(convertedDict['aromasin']),
        'freq' : str(convertedDict['freq']),
        'model' : str(convertedDict['model'])
    }
   
    return stationDict, sensorDict1, sensorDict2, sensorDict3