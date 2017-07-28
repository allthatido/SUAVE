# Constant_Speed_Constant_Altitude_Loiter.py
#
# Created:  Jun 2017, E. Botero 
# Modified:

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

# SUAVE imports
from SUAVE.Methods.Missions import Segments as Methods

from Constant_Speed_Constant_Altitude import Constant_Speed_Constant_Altitude

# Units
from SUAVE.Core import Units

# ----------------------------------------------------------------------
#  Segment
# ----------------------------------------------------------------------

class Constant_Speed_Constant_Altitude_Loiter(Constant_Speed_Constant_Altitude):
    
    def __defaults__(self):
        
        # --------------------------------------------------------------
        #   User inputs
        # --------------------------------------------------------------
        self.altitude  = None
        self.air_speed = 1.0
        self.time      = 1.0 * Units.sec
        
        # --------------------------------------------------------------
        #   The Solving Process
        # --------------------------------------------------------------
        initialize = self.process.initialize
        initialize.conditions = Methods.Cruise.Constant_Speed_Constant_Altitude_Loiter.initialize_conditions


        return

