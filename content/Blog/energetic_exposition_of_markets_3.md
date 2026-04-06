Title: An Energetic Exposition III: Models and complexities
Date: 2024-05-08
Authors: Matt Gibson
Modified: 2026-04-06


There are many optimisation problems in the electricity industry. Let’s consider three here:

1. economic dispatch and optimal DC power flow
2. unit commitment problem
3. resource planning problem

These three problems happen on different scales: minutes to hours for the first one, hours to days for the second one, and years to decades for the third one. 

A friend of mine asked me whether the complexity of electricity markets was intrinsic or due to neo-liberal fuckery. I’m still not sure about the answer, but as the following modelling problems suggest, there are some centralised planning problems that appear to be at the core of the industry. Certainly the distributed version of these problem are much more complex. 


## prototypical problems I: DC optimal power flow and Economic Dispatch
The physical layout of the grid and the physics of power flow are important, complicated, and relevant to the economics of electricity. The optimal powerflow problem (OPF) for physical models of AC power networks is generally non-convex and difficult to solve.  Commonly then, it is simplified to a linear model of power flow, called the DC power flow model.



The main goal is to lower the total cost of generating electricity while still meeting demand and staying within generation limits. The DC optimal power flow problem looks like this:

$$
\min \sum_i c_i P_{G_i}
$$

$$
\text{s.t.} \quad P^{\min}_{G_i} \leq P_{G_i} \leq P^{\max}_{G_i}
$$

$$
B \cdot \theta = P_G - P_D
$$

$$
|\theta_i - \theta_j| / x_{ij} \leq P_{ij,\max}
$$

Economic dispatch is a simpler case where we ignore network constraints. In this case, the problem becomes:

$$
\min \sum_i c_i P_{G_i} \quad \text{s.t.} \quad P^{\min}_{G_i} \leq P_{G_i} \leq P^{\max}_{G_i}, \quad \sum_i P_{G_i} = P_D
$$


The per-unit cost $c_i$ comes from a cost function $C_i(P_{G_i})$. A basic linear model for this is:

$$
C_i(P_{G_i}) = FC_i + Fl_i \cdot a_{f,i} \cdot P_{G_i}
$$


Here, $FC_i$ is the fixed cost for plant $i$, $Fl_i$ is the fuel price, and $a_{f,i}$ is the heat rate, which means the energy needed for each unit of output. The variable cost part, $Fl_i \\cdot a_{f,i}$, gives the fuel cost per unit, which is the same as $c_i$ in the main equation.

In real situations, heat rates change depending on how much power is produced, so the actual cost function is not linear. Using a quadratic approximation works fairly well for gas turbines, but not for hydro plants. In the industry, people usually use a piecewise linear approximation of $C_i$ to keep the problem manageable as an MILP.

* [Power Flow Introduction](https://invenia.github.io/blog/2020/12/04/pf-intro/)
* [A power flow study](https://docs.mosek.com/slides/2018/dtu-electric/talk.pdf)
* [Economic Dispatch](https://ampl.com/mo-book/notebooks/09/economicdispatch.html)
* [Power Network](https://ampl.com/mo-book/notebooks/04/power-network.html)

## Prototypical Problems II: Cost, production and the Unit commitment problem

The simple dispatch model above does not tell us much about the features of different technologies. However, it is important to know which plants are running or what storage is available at any given time. For example, a hydro plant might have zero marginal cost but can only run for a few hours, while a thermal power plant might have high start-up costs and cannot change its output quickly.

This means we need to add terms to the cost function to include these features and add constraints for production limits. For example, there may be quasi-fixed costs such as:

  * no-load costs
  * start-up cost and time (minutes for hydro plants, hours for thermal power)

These costs are represented by 0-1 variables, which means the problem becomes a mixed-integer linear program (MILP).


* [Unit Commitment Problem Notebook](https://nbviewer.org/github/MOSEK/Tutorials/blob/master/unitcommitment/ucp.ipynb)
* D. Streiffert, R. Philbrick, A. Ott. A Mixed Integer Programming Solution for Market Clearing and Reliability Analysis
IEEE Power [paper](https://home.engineering.iastate.edu/~jdm/ee458/PJM-Areva.pdf)
* [A survey comparing centralized and decentralized electricity markets](https://doi.org/10.1016/j.esr.2022.100812)
* [Unit commitment problem in electrical power production](https://en.wikipedia.org/wiki/Unit_commitment_problem_in_electrical_power_production)
* [merit order production](https://en.wikipedia.org/wiki/Merit_order)
* [Electrical Power Generation 1 Python Notebook](https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/electrical_power_generation/electrical_power_1.ipynb)


## prototypical problems III: resource and capacity planning

These Capacity Planning Models address questions like whether to build or not, how much capacity to build, and which technology to use. We might break down the capacity planning problem by what it is trying to plan for:
1. generation
2. transmission
3. distribution
4. consumer

Generation planning focuses on economics to plan both short- and long-term capacity expansion, production costs, and resource adequacy. The goal is to meet reliability and policy requirements.

Transmission planning uses both economic and technical analysis to find out what transmission investments are needed in the short and long term. They look at capacity, reliability, stability, congestion relief, and other important factors.

Distribution planning uses technical studies to help identify what investments are needed in the distribution system, usually in the near term, based on planning standards.

Consumer planning uses economic analysis or set budgets to support distributed energy resource programs, customer initiatives, and rate or tariff design.


* [Power systems course capacity planning Python Notebook](https://github.com/Power-Systems-Optimization-Course/power-systems-optimization/blob/master/Notebooks/03-Basic-Capacity-Expansion.ipynb)

* [facility location  problem](https://colab.research.google.com/github/Gurobi/modeling-examples/blob/master/facility_location/facility_location.ipynb)

* [Optimization for Integrated Electricity System Planning report 2025](https://www.esig.energy/wp-content/uploads/2025/06/ESIG-IP-Optimization-Capacity-Expansion-report-2025.pdf)


## things omitted:



The "neoliberal fuckery" adds more complexity in to these problems by requiring more complex modelling around market clearing and auction design.

In the context of increase use of renewables and decentralisation of generation stochastic and robust variants of the above problems are becoming more important

Ancillary services and reserve markets for things like frequecy control and voltage control are also important, and have their own modelling problems.


## References on Electricity Markets and Modelling

* library: [PyPSA: Python for Power System Analysis](https://pypsa.readthedocs.io/)
* book: Economics of Electricity:  Markets, Competition and Rules
Anna Creti & Fulvio  Fontini. 2019. Cambridge University Press.
* book: Power Generation, Operation, and Control 3e,  Wood, Wollenberg & Sheblé. Wiley 2014
* course: [see example #2 here](https://github.com/Power-Systems-Optimization-Course/power-systems-optimization/blob/master/Notebooks/02-Anatomy-of-a-Model.ipynb)
* report: [Australian Energy Statistics 2022 Energy Update Report](https://www.energy.gov.au/sites/default/files/Australian Energy Statistics 2022 Energy Update Report.pdf)
* [a game on grid balancing](https://www.neso.energy/energy-101/balancing-grid-interactive-game)