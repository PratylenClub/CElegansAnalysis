# CElegansAnalysis
Analysis of the C. Elegans connectome

## TODO
- [ ] Define the strengh associated with every synapse.
	- [ ] Representing this information in a heatmap where all the neurons are organized in every axes and the color is the connection.
- [ ] Check the correlation between the communities extracted and the Neurotransmitter released by each vertex
- [ ] Check other networks
- [ ] Did the initial project of C.Elegans robot takes into account the type of neurotransmitter?

## Datasets
### OpenWorm NeuroML
This connectome is based in the first connectome described in [@White1986]. This dataformat include several parameters values useful in realistic simulations. Maybe we can use those values to infer a weight.

They developed [PyOpenWorm]() a python package to manage the connectome information. *c302* makes use of this package to perform the simple simulations.

### Bentley et al. 2016
[The Multilayer Connectome of Caenorhabditis elegans](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005283)

In this [Dataset](https://docs.google.com/spreadsheets/d/1kCxOOKu1wAREa9VbBiWVVHh-GEC3kJk0A3YVEipPKcc/edit#gid=0) the Openworm team defines the type of **neuron** vs the **neurotransmitter** that they release or the **receptor** that they express.


###  CCeP
[Database of Synaptic Connectivity of C. Elegans for computation](http://ims.dse.ibaraki.ac.jp/ccep/download.html)


## Functional Systems
### Sensory System
> the 52 sensory neurons are extensively reciprocally and recurrently connected by both chemical and gap junction synapses. Forty-nine percent of the chemical synaptic output of sensory neurons is onto other sensory neurons, and this constitutes input to the sensory neurons that is seven times the feedback from type Ib and type Ic interneurons. [@Jarrel2012]

#### Touch System

Neurons involved in touch response [@Chalfie1985]
- Touch sensory neurons (front)	ALML, ALMR, AVM
- Touch sensory neurons (back)	PLML, PLMR, PVM


### Muscle System

## Behaviour
>  For example, C. elegans adjusts its rate of locomotion in the presence of food (Sawin et al., 2000). This behavioral adaptation is achieved through a dopaminergic neural circuit (Sawin et al., 2000; Omura et al., 2012). Moreover C. elegans expresses over 250 different neuropeptides, but for most of them little is known about how they affect the physiology of neurons and other cells (Li and Kim, 2008). [@Szigeti2014]


## Interesting Random Facts

- Delay of signal while passing through chemical synapse	2ms
- Delay of signal while passing through gap junction	0,2ms


## Bibliography

- [Jarrel2012. The Connectome of a Decision-Making Neural Network](http://science.sciencemag.org/content/337/6093/437.full?ijkey=lgRX8mUnpCa/Q&keytype=ref&siteid=sci)
- [C elegans Connectome Research](http://www.connectomeengine.com/Home/CElegans)
- [Database of Synaptic Connectivity of C. Elegans for computation](http://ims.dse.ibaraki.ac.jp/ccep/download.html)
- [Szigeti2014. OpenWorm: an open-science approach to modeling Caenorhabditis elegans](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4217485/)
- [Sawin2014. C. elegans Locomotory Rate Is Modulated by the Environment through a Dopaminergic Pathway and by Experience through a Serotonergic Pathway](http://www.cell.com/neuron/pdf/S0896-6273(00)81199-X.pdf)
- [Chalfie1985. The neural circuit for touch sensitivity in Caenorhabditis elegans.](http://www.jneurosci.org/content/5/4/956.long)
- [Varshney2011. Structural Properties of the Caenorhabditis elegans Neuronal Network](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1001066)
- [White1986. The structure of the nervous system of the nematode Caenorhabditis elegans.](https://www.ncbi.nlm.nih.gov/pubmed/22462104?dopt=abstract)
- [Kato2015. Global Brain Dynamics Embed the Motor Command Sequence of Caenorhabditis elegans](http://www.cell.com/cell/pdf/S0092-8674(15)01196-4.pdf)
