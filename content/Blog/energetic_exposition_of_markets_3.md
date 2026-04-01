Title: An Energetic Exposition III: Models and complexities
Date: 2024-05-08
Authors: Matt Gibson
Modified: 2026-04-01


A simple model for cost is as follows:
$$
C_i (Q_i) = FC_i + Fl_f *a_{f,i} * Q_i
$$
And we have Q_i_subbar and Q_i_superbar, which are the upper production limits of powerplant i
so Q_i_subbar <= Q_i <= Q_i_superbar

where

* C_i is the cost of powerplant i
* Q_i is the energy output of powerplant i
* FC_i is the fixed cost of powerplant i
* Fl_f is the fuel cost of powerplant i
* a_{f,i} is energy efficiency of the plant

This says very little about the technologies.

We could have a quadratic term in Q_i, which would be a good model for a gas turbine, but not for a hydro plant.

* quasi-fixed costs:
  * no-load costs
  * start-up costs (hydro plants minutes, thermal power hours)

## Planning and markets

A friend of mine asked me whether the complexity of electricity markets was intrinsic or due to neo-liberal fuckery. I’m still not sure about the answer, but as the following modelling problems suggest, there are some centralised planning problems that appear to be at the core of the industry.

Let’s consider three here:

1. optimal DC power flow
2. unit commitment problems
3. resource planning problems

prototypical problems I: DC optimal power flow

$$
\min \sum c_i P_{G_i}  \
\text{s.t.} P^{\min}{G_i} \leq P{G_i} \leq P^{\max}{G_i} \
B \cdot \theta = P_G − P_D \
|\theta_i − \theta_j | / x{ij} \leq P_{ij,\max}\
$$

power flow study

* https://docs.mosek.com/slides/2018/dtu-electric/talk.pdf

prototypical problems II: Unit commitment problem

a mixed-integer conic quadratic optimisation problem

* https://nbviewer.org/github/MOSEK/Tutorials/blob/master/unitcommitment/ucp.ipynb
* D. Streiffert, R. Philbrick, A. Ott
A Mixed Integer Programming Solution for Market Clearing and Reliability Analysis
IEEE Power https://home.engineering.iastate.edu/~jdm/ee458/PJM-Areva.pdf
* https://www.sciencedirect.com/science/article/pii/S2211467X22000128?via%3Dihub https://doi.org/10.1016/j.esr.2022.100812
* Unit commitment problem in electrical power production
* merit order production
* Economic Dispatch  https://ampl.com/mo-book/notebooks/09/economicdispatch.html
https://ampl.com/mo-book/notebooks/04/power-network.html
* https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/electrical_power_generation/electrical_power_1.ipynb

prototypical problems III: resource planning

* https://github.com/Power-Systems-Optimization-Course/power-systems-optimization/blob/master/Notebooks/03-Basic-Capacity-Expansion.ipynb
* Capacity/ Resource/Network Planning Models /
* facility location  problem https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/facility_location/facility_location.ipynb

## References

General LP /MILP/ Convex optimisation resources

I’m obviously quite interested in learning more about optimisation, but all the optimisation of interest is outside of the scope. So let me put down some pointers here.

* my 1st goto for optimisation is Google’s ORTools (a good all-round place to start for an optimisation problem; feels more CS-ish) https://developers.google.com/optimization
* My 2nd go-to for optimisation is CVXPy (when you know the general optim problem you’re working with ) https://www.cvxpy.org/
* They both include many illustrative examples in Python and references to other libraries and books.
* A recent primer on SAT and constraint problems is https://github.com/d-krupke/cpsat-primer.
* OR Tools has references to many books

   https://developers.google.com/optimization/support/resources

* The AIMMS optimisation modelling book http://www.aimms.com/downloads/manuals/optimization-modeling”
* Formulating Integer Linear Programs: A Rogues’ Gallery. Brown & Dell, 2007. INFORMS https://doi.org/10.1287/ited.7.2.153 https://pubsonline.informs.org/doi/10.1287/ited.7.2.153

Optimisation and Electricity

* library: PyPSA: Python for Power System Analysis
* book: Economics of Electricity:  Markets, Competition and Rules
Anna Creti & Fulvio  Fontini. 2019. Cambridge University Press.
* book: PoWER GENERATION, OPERATION, AND CONTROL 3e,  Wood, Wollenberg & Sheblé. Wiley 2014
* course: see example #2 here: https://github.com/Power-Systems-Optimization-Course/power-systems-optimization/blob/master/Notebooks/02-Anatomy-of-a-Model.ipynb
* report: https://www.energy.gov.au/sites/default/files/Australian Energy Statistics 2022 Energy Update Report.pdf