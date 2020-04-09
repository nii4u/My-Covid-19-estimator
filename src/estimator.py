def estimator(data):
  currentlyInfected = {}
  currentlyInfected["data"] = data
  dict1 = {}
  dict1["currentlyInfected"] = data["reportedCases"] * 10
  dict1["infectionsByRequestedTime"] = dict1["currentlyInfected"] * 512

  currentlyInfected["impact"] = dict1
  dict2 = {}
  dict2["currentlyInfected"] = data["reportedCases"] * 50
  dict2["infectionsByRequestedTime"] = dict2["currentlyInfected"] * 512
  currentlyInfected["severeImpact"] = dict2

  # currentlyInfected["impact"] = inputdata
  # currentlyInfected = {
  #   "data": inputdata,
  #   "impact": {"currentlyInfected" : inputdata["reportedCases"] * 10 },
  #   "severeImpact": {"currentlyInfected" : inputdata["reportedCases"] * 50 }
  # }

  return currentlyInfected
