"""
CEASIOMpy: Conceptual Aircraft Design Software

Developed by CFS ENGINEERING, 1015 Lausanne, Switzerland

Module to export Aeromap (or other data?) to CSV

Python version: >=3.8

| Author: Aidan Jungo
| Creation: 2021-04-07

TODO:

    * export other data...
    *

"""

# =================================================================================================
#   IMPORTS
# =================================================================================================

from pathlib import Path

from ceasiompy.utils.ceasiomlogger import get_logger
from ceasiompy.utils.ceasiompyutils import get_results_directory
from ceasiompy.utils.moduleinterfaces import (
    check_cpacs_input_requirements,
    get_toolinput_file_path,
    get_tooloutput_file_path,
)
from ceasiompy.utils.commonxpath import CEASIOMPY_XPATH
from cpacspy.cpacsfunctions import get_string_vector
from cpacspy.cpacspy import CPACS

log = get_logger()

MODULE_DIR = Path(__file__).parent
MODULE_NAME = MODULE_DIR.name


# =================================================================================================
#   CLASSES
# =================================================================================================


# =================================================================================================
#   FUNCTIONS
# =================================================================================================


def export_aeromaps(cpacs_path, cpacs_out_path):

    cpacs = CPACS(cpacs_path)

    aeromap_to_export_xpath = CEASIOMPY_XPATH + "/export/aeroMapToExport"

    try:
        aeromap_uid_list = get_string_vector(cpacs.tixi, aeromap_to_export_xpath)
    except ValueError:
        aeromap_uid_list = cpacs.get_aeromap_uid_list()

    results_dir = get_results_directory("ExportCSV")

    for aeromap_uid in aeromap_uid_list:
        aeromap = cpacs.get_aeromap_by_uid(aeromap_uid)

        csv_path = Path(results_dir, f"{aeromap_uid}.csv")
        aeromap.export_csv(csv_path)

        log.info(f"Aeromap(s) has been saved to {csv_path}")

    cpacs.save_cpacs(cpacs_out_path, overwrite=True)


# =================================================================================================
#    MAIN
# =================================================================================================


def main(cpacs_path, cpacs_out_path):

    log.info("----- Start of " + MODULE_NAME + " -----")

    check_cpacs_input_requirements(cpacs_path)
    export_aeromaps(cpacs_path, cpacs_out_path)

    log.info("----- End of " + MODULE_NAME + " -----")


if __name__ == "__main__":

    cpacs_path = get_toolinput_file_path(MODULE_NAME)
    cpacs_out_path = get_tooloutput_file_path(MODULE_NAME)

    main(cpacs_path, cpacs_out_path)
