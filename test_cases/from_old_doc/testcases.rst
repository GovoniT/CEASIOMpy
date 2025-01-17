Getting started
===============

Once you finished the installation you could try to run the following test cases to familiarize yourself with |name|

.. warning::

These test case are not up to date, they will be updated soon.


Test Case 1 : Simple workflow
*****************************

The module 'WorkflowCreator' can be found at /CEASIOMpy/ceasiompy/WorkflowCreator/workflowcreator.py you can run it by simply type in your terminal:

.. code::

    cd YourPath/CEASIOMpy/ceasiompy/WorkflowCreator/
    python workflowcreator.py -gui


.. hint::

    If you use a Linux you can easily set an alias in you .bashrc file to run these command with a shortcut of your choice.


When you run this module, a GUI will appear. The first thing to do is to chose the CPACS file we will use for this analysis, click on "Browse" and select "D150_simple.xml", it is a test aircraft similar to an A320 . Then, we will have the possibility to chose which module to run and in which order. For this first test case, we will use only the tab "Pre". On the left you will see the list of all available modules, when you select one you can add it to the list of module to execute. You can also remove module from this list or change the order with the buttons.
We will create a simple workflow with only three modules:

SettingsGUI -> WeightConventional -> Range.

.. figure:: getting_started_fig/TestCase1_WorkflowCreator.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - WorkflowCreator - Test case 1

Once you added these three modules in order you can click "Save & Quit". The first module to run will be "SettingsGUI", it will show you all the available options for the next modules. All the options are pre-filled with default values. You don't need to change any value for this example, so you can just click "Save & Quit".
The two next modules will be executed automatically without showing anything except some results in the terminal.


Test Case 2 : Aerodynamic database with PyTornado
*************************************************

In this example we will see how to create an aerodynamic database with PyTornado and plot them on a graph.
As in test case 1, we will run 'WorkflowCreator'. In the GUI, after selecting the same D150_simple.xml CPACS file, we will select some modules in the list and place them in order to create the following workflow:

CPACSCreator -> SettingsGUI -> PyTornado -> PlotAeroCoefficients

.. figure:: getting_started_fig/TestCase2_WorkflowCreator.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - WorkflowCreator - Test case 2

Then, you can click "Save & Quit". The first module to be executed will be CPACSCreator, with this module you can modify the geometry of the aircraft. We won't made changes now, but if you want to learn how to use CPACSCreator, you can follow the link bellow:

https://dlr-sc.github.io/tigl/doc/cpacscreator-0.1/tuto.html#tuto_create_from_scratch

If you apply some changes, save your modifications and close the CPACSCreator windows. Now, the SettingsGUI windows will appear, and first, we will import a new AeroMap.  Now, click on 'Import CSV' to add a new AeroMap, select 'Aeromap_4points_aoa.csv' and 'OK'.

.. figure:: getting_started_fig/TestCase2_ImportAeroMap.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - Import AeroMap - Test case 2

You can also click on the 'aeromap_empty' and delete it with the buttons. You must click on the button 'Update' to make the new AeroMap available for all modules.

Now, you can click on the 'PyTornado' Tab, the AeroMap selected should be the one you imported before. We will not change the other option and just click 'Save & Quit'.

The software should run for a few seconds and when the calculation are done, a plot of the aerodynamic coefficient should appear.


Test Case 3 : SU2 at fixed CL and Range
***************************************

For this test case you can try to run the following workflow with the same aircraft. It will compute the range after performing a CFD analysis at fixed CL.

At first add all recquired modules to the workflow as illustrated in the figure below.

.. figure:: getting_started_fig/TC3_Modules.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - WFC - Test case 3

After that you can modify the different parameters for each module. For the CLCalculator you can choose under which condition you want to be able to fly. The required Cl will be computed and the SU2 analysis will modify the angle of attack in order to reach this value of Cl.

.. figure:: getting_started_fig/TC3_CLCalculator.png
    :width: 400px
    :align: center
    :alt: CEASIOMpy - CLC - Test case 3
    
After that the SkinFriction module will add the friction term that is not taken into account by the SU2 computation, in order to have a corrected value of the drag.

The range is then computed and you can find your results within the CPACS file in the ToolOutput folder of the WorkflowCreator module. For the results of the CFD analysis you can find all the files in the WKDIR/CEASIOMpy_Run_DATE/ with the correct date.

.. figure:: getting_started_fig/TC3_Ranges.png
    :width: 600px
    :align: center
    :alt: CEASIOMpy - RNG_RES - Test case 3

    
Test Case 4 : Optimizing the CL
*******************************

To launch an optimisation routine or a DoE, launch the WorkflowCreator tool with the GUI and select the modules you want to run in the routine in the 'Optim' tab and select the Optim option from the type list. Here the modules 'WeightConventional' and 'PyTornado' are chosen.

.. figure:: getting_started_fig/TestCase4_WorkflowCreator.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - WFC - Test case 4
    
The next window that opens is the SettingsGUI, were you can tune the options specific to each module. Focusing on the options of the Optimisation tab, different options can be set. In our case the 'Objective' is set on 'cl' and the 'Optimisationn goal' is set to 'max' in order to search for the maximal cl. The other options from the 'Optimisation settings' group are left at their default values and the 'DoE settings' group is not used in the case of an optimisation. 
The 'CSV file path' is left blank as we have not defined a file with the problem parameters.

.. figure:: getting_started_fig/TestCase4_Optimisation.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - STGui - Test case 4

After saving the settings a CSV file is automatically generated and opened with your standard CSV opener.

.. figure:: getting_started_fig/TestCase4_Generated_CSV.png
    :width: 630 px
    :align: center
    :alt: CEASIOMpy - CSV - Test case 4
    
Here you can see all the parameters that can be used in the routine. The ones that appear in the objective function are labelled as 'obj' in the 'type' column, and the ones that are only outputs of some modules are labelled 'const', their type must not be changed. All the other parameters can have their values modified in the following columns :

.. code::
    ['type','min','max']

Or you can add a new element to the file if you know what to add. Here we suppress all the elements that we do not desire to have in our routine and we end up with just the parameters that we want for this optimisation. Note that you can also let some cases blank in the 'min' and 'max' columns if you don't want to restrain the domain on one side. The 'min' and 'max' values of the 'obj'-labelled parameters are not taken into account.

.. figure:: getting_started_fig/TestCase4_Variable_library.png
    :width: 630 px
    :align: center
    :alt: CEASIOMpy - VL - Test case 4

Save the file and close it, you must then press the enter key into the terminal to launch the routine. After that the routine is running and you just have to wait for the results.

.. figure:: getting_started_fig/TestCase4_terminal.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - Terminal - Test case 4

When the routine finishes two windows are generated containing the history plots of the parameters on one and the objective function on the other. After closing these windows the program closes and you finished the process !

For the post-processing you can go in the WKDIR folder, where you will find the CEASIOMpy_Run with the corresponding date at which you launched the routine. In this file you will find the results of an initial run the program did befpore launching the optimisation loop and the 'Optim' folder, in which all the results of the routine are saved.

* Driver_recorder.sql : Recorder of the routine from the OpenMDAO library. It is used to access the history of the objective function.
* circuit.sqlite : File that is used to generate the N2 diagram of the problem.
* circuit.html : This file represents an N2 diagram of the problem that was solved, showing the dependencies of the variables between the different modules.
* Variable_library.csv : This file is the CSV that you modified before launching the routine.
* Variable_history.csv : This file contains the value of all the desired parameters at each iteration, plus the basic informations of the parameters (name, type, getcmd, setcmd).
* 
* Geometry : This folder contains the CPACS that is used in the routine at each iteration, this can be changed by tuning the 'Save geometry every' parameter in the Optimisation settings.
* Runs: This folder contains the directories of all the workflow runs that were made during the routine. These folders are equivalent to a simple CEASIOMpy_Run workflow folder.


Test Case 5 : Surrogate model for SU2
*************************************

Before using a surrogate model the first step is to create a model and train it over a data set, for that the SMTrain module must be used. First launch a DoE with the lift as an objective function and at least 25 sample points (the more the better).
When the CSV file for the parameters opens, choose the wing span and the angle of attack as design variables.

.. figure:: getting_started_fig/TC5_Param.png
    :width: 800 px
    :align: center
    :alt: CEASIOMpy - Terminal - Test case 5

After the DoE launch a new workflow with the SettingsGUI and the SMTrain modules. Here get the Variable_history file that was generated by the DoE which is located under WKDIR/CEASIOMpy_Run_DATE/DoE/, which will serve as the training set.
As we do not have a lot of data, we will use all of it to train the model by setting the % of training data to 1.0 and deactivate the plots used for validation. The model we chose this time is the simple krigin model KRG.

.. figure:: getting_started_fig/TC5_SGUI.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - SettingsGUI - Test case 5

After setting the options launch the program, which will only take a few seconds before finishing, and go look for the trained model in the SM folder of the current working directory. This file cannot be normally opened as it has been dumped using a special python library (ref to 'pickle'). Note that there also is a CSV called 'Data_setup' which was generated that contains the informations about the model inputs/outputs in case you want to check your model entries. Now the part comes were we call the SMUse module to get results with our surrogate.
 
.. figure:: getting_started_fig/TC5_SMTrain.png
    :width: 400 px
    :align: center
    :alt: CEASIOMpy - SM - Test case 5   

For this part chose a CPACS file with different values than the one you fed to the model (either with a new CPACS or you can modify it using cpacscreator). Launch a workflow with SettingsGUI and SMUse. In the settings, choose the resulting file containing the surrogate, you don't have to change any other option. Launch the program and now you have the resulting CPACS file in the ToolOutput folder of the SMUse module ! If you take a look at the aeromap you chose for the computation you will see that only a value of cl has been added/modified.



Module compatibility
--------------------

Visualization of which module can be connected to which other modules:

in development...
