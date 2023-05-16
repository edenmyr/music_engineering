import numpy as np
from main import *
import json
from tqdm import tqdm

def dataGatherer(n):
    dataDict = {}
    notes = genNotes(n)
    dataDict["exactNotes"] = notes
    closest, cent_deviation, idx, exFracs = closestRelation(notes,cent_tol=25,easyFracLim=50)

    dataDict["closestFraction"] = closest
    dataDict["centDeviation"] = cent_deviation
    dataDict["exactFractions"] = exFracs

    with open("data\\data_"+ str(n) + "_notes", "w") as outfile:
        json.dump(dataDict,outfile,indent=2)
    return 


for i in tqdm(range(1,25)):
    dataGatherer(i)

dataDict = {}
notes = genNotes(12,octFreq=2)
dataDict["exactNotes"] = notes
closest, cent_deviation, idx, exFracs = closestRelation(notes,cent_tol=25,easyFracLim=50)

dataDict["closestFraction"] = closest
dataDict["centDeviation"] = cent_deviation
dataDict["exactFractions"] = exFracs

with open("data\\traditional_octave", "w") as outfile:
    json.dump(dataDict,outfile,indent=2)