def estimator(data):
  currentlyInfected = {}
  currentlyInfected["data"] = data
  currentlyInfected["impact"] = {}
  currentlyInfected["impact"]["currentlyInfected"] = data["reportedCases"] * 10

  if data['periodType']=='days':
      num_days = data['timeToElapse']
  elif data['periodType']=='weeks':
      num_days = data['timeToEplapse'] * 7
  else:
      num_days = data['timeToEplapse'] * 30

  factor = num_days//3

  multiplier = 2** factor

  
  currentlyInfected["impact"]["infectionsByRequestedTime"] = currentlyInfected["impact"]["currentlyInfected"] * multiplier

  currentlyInfected["severeImpact"] = {}
  currentlyInfected["severeImpact"]["currentlyInfected"] = data["reportedCases"] * 50
  currentlyInfected["severeImpact"]["infectionsByRequestedTime"] = currentlyInfected["severeImpact"]["currentlyInfected"] * multiplier


  return currentlyInfected
