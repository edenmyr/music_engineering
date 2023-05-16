import numpy as np
import json
from matplotlib import pyplot as plt

def dataAnalysis(dataSets, tol=10):
    with open('data\\traditional_octave') as file:
        tradOctave = json.load(file)
    numNotes = []
    closeTones = []
    meanCentDev = []
    for set in dataSets:
        print(dataSets)
        print("ej")
        print(set)
        with open(set) as file:
            data = json.load(file)
            meanCentDev.append(np.mean(np.abs(data["centDeviation"])))
    
        closeTone = 0
        for i in range(len(data["exactNotes"])):
            for j in range(len(tradOctave["exactNotes"])):
                print(np.abs(1200 * np.log(data["exactNotes"][i]/tradOctave["exactNotes"][j])/np.log(2)))
                if np.abs(1200 * np.log(data["exactNotes"][i]/tradOctave["exactNotes"][j])/np.log(2)) < tol:
                   closeTone += 1
        numNotes.append(len(data["exactNotes"]))
        closeTones.append(closeTone)
        # print(closeTones)
    return meanCentDev, closeTones, numNotes

# Will implement deviation from traditional scale, cent deviation doesn't really tell us much
# since we have deviations in all the tritaves

# tradOctave is a tritave now, this is not what is wanted

# TODO
def plotting(res):
    meanCentDev, closeTones, numNotes = res
    fig, ax = plt.subplots()
    ax.set_xlabel("Notes in tritave")
    ax.set_ylabel("Mean deviation [cents]")
    plt.bar(numNotes, meanCentDev)
    plt.show()
    fig.savefig("cent_deviation.eps")

    fig, ax2 = plt.subplots()
    ax2.set_xlabel("Notes in tritave")
    ax2.set_ylabel("Number of tones close to trad scale")
    #clTonesNormed = [closeTones[i]/numNotes[i] for i in range(len(numNotes))]
    plt.bar(numNotes,closeTones) # currently picks upp pretty much everything. 
    # What tolerance is for the human ear?
    plt.show()
    fig.savefig("close_tones.eps")

    pass


fileNames = ['data\data_' + str(i) + "_notes" for i in range(1,24)]
# print(fileNames)
# meanCD, _ = dataAnalysis(fileNames)
# print(meanCD)

res = dataAnalysis(fileNames)
print(res)
plotting(res)



# Could look at differences between tones and try to find similar intervals
# even if the start and stop point is not on traditional notes
# MAYBE not such a good idea

# would be nice to print a document that contains listed info of the scales. 
# could contain:
# FREQ. REL. TO ROOT | JUST INTONATION | 
