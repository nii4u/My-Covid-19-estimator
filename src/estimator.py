def estimator(data):
  currentlyInfected = {}
  currentlyInfected["data"] = data
  currentlyInfected["impact"] = {}
  currentlyInfected["impact"]["currentlyInfected"] = data["reportedCases"] * 10
  currentlyInfected["impact"]["infectionsByRequestedTime"] = currentlyInfected["impact"]["currentlyInfected"] * 512

    
  currentlyInfected["severeImpact"] = {}
  currentlyInfected["severeImpact"]["currentlyInfected"] = data["reportedCases"] * 50
  currentlyInfected["severeImpact"]["infectionsByRequestedTime"] = currentlyInfected["severeImpact"]["currentlyInfected"] * 512


  # currentlyInfected["impact"] = inputdata
  # currentlyInfected = {
  #   "data": inputdata,
  #   "impact": {"currentlyInfected" : inputdata["reportedCases"] * 10 },
  #   "severeImpact": {"currentlyInfected" : inputdata["reportedCases"] * 50 }
  # }

  return currentlyInfected
