
def estimator(data):
  currentlyInfected = {}
  currentlyInfected["data"] = data
  currentlyInfected["impact"] = {}
  currentlyInfected["impact"]["currentlyInfected"] = data["reportedCases"] * 10

  if data['periodType']=='days':
      num_days = data['timeToElapse']
  elif data['periodType']=='weeks':
      num_days = data['timeToElapse'] * 7
  else:
      num_days = data['timeToElapse'] * 30

  factor = num_days//3

  multiplier = 2 ** factor

  
  currentlyInfected["impact"]["infectionsByRequestedTime"] = currentlyInfected["impact"]["currentlyInfected"] * multiplier

  currentlyInfected["severeImpact"] = {}
  currentlyInfected["severeImpact"]["currentlyInfected"] = data["reportedCases"] * 50
  currentlyInfected["severeImpact"]["infectionsByRequestedTime"] = currentlyInfected["severeImpact"]["currentlyInfected"] * multiplier
  
#   currentlyInfected["impact"]["severeCasesByRequestedTime"] = 0.15 * currentlyInfected["impact"]["infectionsByRequestedTime"]
#   currentlyInfected["severeImpact"]["severeCasesByRequestedTime"] = 0.15 * currentlyInfected["severeImpact"]["infectionsByRequestedTime"]

#   currentlyInfected['data']['hospitalBedsByRequestedTime'] = currentlyInfected['data']['totalHospitalBeds'] - (currentlyInfected["severeImpact"]["severeCasesByRequestedTime"]+currentlyInfected["impact"]["severeCasesByRequestedTime"])

