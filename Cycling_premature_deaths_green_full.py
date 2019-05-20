# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 2018

@author: adm-remmer
"""
from pcraster import *
import natural_capital as nc
from natural_capital import algorithm

bomenkaart = readmap('D:\\Data\\input\\raster\\amsterdam\\bomenkaart.map')
graskaart = readmap('D:\\Data\\input\\raster\\amsterdam\\graskaart.map')
struikenkaart = readmap('D:\\Data\\input\\raster\\amsterdam\\struikenkaart.map')

groenkaart = bomenkaart + graskaart + struikenkaart
AvgGroen1000 = algorithm.windowaverage(groenkaart, 1000)

Inwonerskaart = readmap('D:\\Data\\input\\raster\\amsterdam\\Inwoners.map')
population = ifthenelse(defined(Inwonerskaart), Inwonerskaart, scalar(0))

##Minutes cycled to work calculation

TheorMinCycled = 103.4 + (0.83 * AvgGroen1000 * 100)

MinCycledIndiv = TheorMinCycled * (0.63 * 0.27)
MinCycledComm = population * MinCycledIndiv

report(MinCycledIndiv, "Minutes_cycled_individual_commuting.map")
report(MinCycledComm, "Total_min_cycled_commuting.map")

##RRM calculation

RRMcycling = (TheorMinCycled/100) * 0.1

PopRRM = population * RRMcycling
PopRRMAverage = maptotal(PopRRM)/maptotal(population)
Popmap = maptotal(population)

report(RRMcycling, "RRM_cycling.map")
report(PopRRMAverage, "PopRRMAverage.map")
report(Popmap, "Populationtotal.map")

###VSL calculation

#VSL = valueX
VSLcell = popRRM * (0.63 * 0.27) * VSL