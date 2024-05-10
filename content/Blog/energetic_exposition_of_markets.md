Title: An Energetic Exposition: notes about electricity markets
Date: 2024-05-08
Authors: Matt Gibson


Electricity markets are can be quite complex. They have many features which are atypical of other commodity markets, and are not frequently discussed in econ 101. For instance, my microeconomics textbooks has nearly three chapters on the environment, pollution and natural resources (it's a bit lefty) but has a single reference to energy and none to electricity. For the record, there point is that in 2009 renewables were subsidised to the tune of 4 billion USD, while fossil fuels were subsidised to the tune of 550 billion USD (yikes). 

## some history 

It is banal to observe that electricity is ever present in modern life, yet we reflect rarely on it. We might say that there are historical three major applications which have driven the mass-adoption of electricity:
1. lighting 
2. electric engine
    - our primary engine with which we are familiar is the the ICE engine, but electrice engines made the impact for manufacturing first and then to consumer devices. We use the mechanical energy from an electric energy directly in a washingmachine or drill. But indirectly through the motor in the compressor forcing coolant through a heat exchange in  a refrigerator be it a our home fridge or aircon system. 
3. portability of energy
    - surprising, as I think of internal combustion engines as the primary mode of transport for most of the 20th century, but this is very passsenger centric. A very popular mode of transport (for goods, not people) has been the diesel trains or more properly, diesel-electric transmissions. These use diesel engines to generate electricity which is then used to power electric motors. Historical popular with trains, ships and submarines.


## generation and usage



Electricity must be generated. Electricity generators are the cause of much global warming. 

energy and electricity are obvious different, but the discussion is linked since some things are do not have direct electricity use but are still energy intensive e.g. 
- transport
- heating

In, 2020-2021 Australian final energy consumption totaled 4121.9 PJ, and is broken down as follows:

Coal: 2.5%
Natural gas: 24.1%
refined products: 48.4%
electricity: 20.7% 
    generated from coal: 11%
    generated from gas: 3.9%
    generated from oil: 0.4%
    generated from renewables: 5.5%
renewables: 4.3%

notes: renewables includs bioenergy( mostly bagaasse, biogas, and wood)


How does compare with other countries? We can divide countries up into 4 categories based on their income level:
- high income countries (worldbank gni per capita >= 13,846)
Australia pop 25.7m, energy 237,000 GWh/yr, 9,200 kwh/yr,  57,000 gni 2022
19th in energy consumption, 53th in population

- upper middle income countries (worldbank gni per capita between 1,136 and 13,845)
i.e. a very important middle income country 
China pop 1,409m, energy 7,806,000 , 5,474 kwh/yr,  12,850 gni 2022
1st energy consumption, 1st in population

- lower middle income 
Indonesia, pop 279m (2023), energy 282,000 GWh/yr, 1030 kwh/yr;  4,580 gni (2022) 17th in energy consumption, 4th in population

- lower income countries 
(ethiopia, pop: 120m, energy 9,500 GWh/yr (2021),  avg 79kw per year, gni 1,020 (2022)) 103rd by energy consumption, 13th by population

- electricity consumption is wealth, but it doesn't appear to be 
 (sensibly as there are climatic concerns)
 norway is 2nd in electricy , 3rd in gni
 kuwait is 5th in electricy, but 27th in gni


https://www.worldbank.org/en/country/mic/overview

## basic properties of electricity

resistance
current 
voltage

resistivity vs resistance
conductivity vs conductance

load 

P = R*I**2

power
energy
work


frequency
phase
active power
reactive power
apparent power/ powerfactor

## Markets I

the electricity supply chain:
 - generation
 - transmission
 - distribution
 - retailing
 - dispatching


market structures:
* monopoly
* monopsony (independent power producers)
  - owenership unbundling
  - tolling agreements
  - virtual power plants
* wholesale
    - grid operator
    - distribution companies
    - organised by pool market or power exchange
        - pool market
            - uniform price
            - central entitiy matches bids and offers
             - spot market or market coupling
        - power exchange ()
            - real-time price variation
            - price determined through trading, not central entity
            - clearing price determing 
            - not necessarily phyusical exchange of 
            - like stock exchange 
            - includes derivatives (futures, options, swaps)

* wholesale +retail


## Markets II: generation  

 a simple model for cost is as follows:

C_i (Q_i) = FC_i + Fl_f *a_{f,i} * Q_i

and 

Q_i_subbar and Q_i_superbar are the upper production limits of powerplant i
so Q_i_subbar <= Q_i <= Q_i_superbar 

where 
* C_i is cost of powerplant i
* Q_i is the energy output of powerplant i
* FC_i is the fixed cost of powerplant i
* Fl_f is the fuel cost of powerplant i
* a_{f,i} is energy efficiency of the plant

this says very little about the technologies

we could have term quadratic term in Q_i, which would be a good model for a gas turbine, but not for a hydro plant.
- quasi-fixed costs:
    - no-load costs 
    - start-up costs (hydro plants minutes,, thermal power hours)



## Markets III: computational complexities

### prototypical problems I: DC optimal power flow


min ∑ c_i P_{G_i}
s.t. P minGi ≤ PGi ≤ P maxGi
B · θ = P_G − P_D
|θi − θj |/xij ≤ Pij,max

power flow study

https://docs.mosek.com/slides/2018/dtu-electric/talk.pdf

### prototypical problems II: Unit commitment problem 
 a mixed-integer conic quadratic optimization problem

https://nbviewer.org/github/MOSEK/Tutorials/blob/master/unitcommitment/ucp.ipynb

* D. Streiffert, R. Philbrick, A. Ott
    A Mixed Integer Programming Solution for Market Clearing and Reliability Analysis
    IEEE Power https://home.engineering.iastate.edu/~jdm/ee458/PJM-Areva.pdf

* https://www.sciencedirect.com/science/article/pii/S2211467X22000128?via%3Dihub https://doi.org/10.1016/j.esr.2022.100812

* Unit commitment problem in electrical power production
* merit order production
* Economic Dispatch  https://ampl.com/mo-book/notebooks/09/economicdispatch.html
https://ampl.com/mo-book/notebooks/04/power-network.html

### prototypical problems III: resource planning 

https://github.com/Power-Systems-Optimization-Course/power-systems-optimization/blob/master/Notebooks/03-Basic-Capacity-Expansion.ipynb

* Capacity/ Resource/Network Planning Models /

* facility location  problem https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/facility_location/facility_location.ipynb

## references
* https://pypsa.readthedocs.io/en/v0.28.0/plotting.html
* Economics of Electricity:  Markets, Competition and Rules
Anna Creti & Fulvio  Fontini. 2019. Cambridge University Press.
* PoWER GENERATION, OPERATION, AND CONTROL 3e,  Wood, Wollenberg & Sheblé. Wiley 2014
* see example #2 here: https://github.com/Power-Systems-Optimization-Course/power-systems-optimization/blob/master/Notebooks/02-Anatomy-of-a-Model.ipynb
* https://www.eia.gov/international/data/world/electricity/electricity-consumption?pd=2&p=0000002&u=0&f=A&v=mapbubble&a=-&i=none&vo=value&t=C&g=00000000000000000000000000000000000000000000000001&l=249-ruvvvvvfvtvnvv1vrvvvvfvvvvvvfvvvou20evvvvvvvvvvnvvvs0008&s=315532800000&e=1546300800000&
* https://ourworldindata.org/grapher/gross-national-income-per-capita
* https://www.energy.gov.au/sites/default/files/Australian%20Energy%20Statistics%202022%20Energy%20Update%20Report.pdf