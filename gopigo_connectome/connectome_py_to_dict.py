import pickle
txt = open("connectome.py","r").readlines()
connectome = {}
for line in txt:
        if "()" in line:
                sending_neuron = line.split()[-1].split("()")[0]
                connectome[sending_neuron] = {}
        if "postSynaptic" in line:
                receiving = line.split("\'")[1]
                weight = line.split("+=")[1].split()[0]
                connectome[sending_neuron][receiving] = int(weight)
pickle.dump(connectome,open("connectome_dict.pickle","wb"))