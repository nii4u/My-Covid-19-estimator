
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

  currentlyInfected["impact"]["severeCasesByRequestedTime"] = int(0.15 * currentlyInfected["impact"]["infectionsByRequestedTime"])
  currentlyInfected["severeImpact"]["severeCasesByRequestedTime"] = int(0.15 * currentlyInfected["severeImpact"]["infectionsByRequestedTime"])
  
  currentlyInfected["impact"]["hospitalBedsByRequestedTime"] = int(data['totalHospitalBeds']*0.35 - currentlyInfected["impact"]["severeCasesByRequestedTime"])
  currentlyInfected["severeImpact"]["hospitalBedsByRequestedTime"] = int(data['totalHospitalBeds']*0.35 - currentlyInfected["severeImpact"]["severeCasesByRequestedTime"])
  

  currentlyInfected["impact"]["casesForICUByRequestedTime"] = int(0.05 * currentlyInfected["impact"]["infectionsByRequestedTime"])
  currentlyInfected["severeImpact"]["casesForICUByRequestedTime"] = int(0.05 * currentlyInfected["severeImpact"]["infectionsByRequestedTime"])


  currentlyInfected["impact"]["casesForVentilatorsByRequestedTime"] = int(0.02 * currentlyInfected["impact"]["infectionsByRequestedTime"])
  currentlyInfected["severeImpact"]["casesForVentilatorsByRequestedTime"] = int(0.02 * currentlyInfected["severeImpact"]["infectionsByRequestedTime"])

  #currentlyInfected["impact"]["dollarsInFlight"] = int(currentlyInfected["impact"]["infectionsByRequestedTime"] * data['region']['avgDailyIncomePopulation']*data['region']['avgDailyIncomeInUSD']  * num_days)
  currentlyInfected["severeImpact"]["dollarsInFlight"] = int(currentlyInfected["severeImpact"]["infectionsByRequestedTime"]  * data['region']['avgDailyIncomePopulation']*data['region']['avgDailyIncomeInUSD']  * num_days)





  return currentlyInfected
