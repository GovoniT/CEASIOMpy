# TODO

## CEASIOMpy project

* Make installation easier
  * External dependencies
    * Sumo
    * SU2
    * PyTornado
    * Conda?
  * Script for automatic installation?
* Separate code from user working directory ???

## Module dependencies

* Create a function to check consistency (does same variable name are stored a the same xpath, ...)

## Modules

* To develop
  * Propulsion
  * DynamicStability
  * FlightModel
  * LaTeXReport
  * Beam model generator (automatic sizing)

### Aerodynamics

* Calculate and save controls surface deflections
* SU2CheckConvergence (maybe integrate with SU2Run)

### Weight and Balance modules

* Check input/output, try to simplify
* Modify the code to make it more CEASIOMpy style

### AeroFrame

* Get OptiMale test case to work (A/C with multiple wings) with SU2
* How deal with wing symmetries?
* Getting analysis settings from CPACS file
  * Choose e.g. PyTornado or SU2
* File path handling (where store temp files, results, etc.)
* Save intermediate results (i.e. results from each iteration)
* Add test case (make sure it runs)
* What should be stored in CPACS?
  * Maximum deflections at the end of the loop?
  * Or max. absolute difference versus iteration number

## Tests

* Create test function for every module

### Platform compatibility

* Try to install on different platform

## Miscellaneous

* Where and when update 'reference/area' and 'length'? (e.g. after changing A/C geometry)
