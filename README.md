spectre_cap_extraction
======================

After having finished the design and layout of a full-adder cell, I needed to know the capacitance at the input nodes. Every extracted value of R and C can be found in the netlist file made by Assura, the python script simply parse it by a regular expression and sum together every component.

USE EXAMPLE: I want to extract the capacitance at node CI

---------------------------------------------
wf111-013:Desktop harrym$ python cap.py CI
Print every single capacitance found? 0/1  1


3.13532e-16
2.10296e-16
1.91745e-16
2.05137e-16
8.39309e-16
8.64555e-16
2.19722e-16
2.56817e-16
Total capacitance at  CI :  3.101113e-15 
---------------------------------------------
