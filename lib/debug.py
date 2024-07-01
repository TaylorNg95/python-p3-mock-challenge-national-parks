#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    
    nancy = Visitor('Nancy')
    arthur = Visitor('Arthur')

    yosemite = NationalPark('Yosemite')
    yellowstone = NationalPark('Yellowstone')
    badlands = NationalPark('Badlands')

    trip1 = Trip(nancy, yosemite, '1/1/24', '1/2/24')
    trip5 = Trip(nancy, yosemite, '1/1/25', '1/2/25')
    trip2 = Trip(arthur, yosemite, '1/1/24', '1/2/24')
    trip3 = Trip(nancy, yellowstone, '2/1/24', '2/2/24')
    trip4 = Trip(arthur, yellowstone, '2/1/24', '2/2/24')

    ipdb.set_trace()
