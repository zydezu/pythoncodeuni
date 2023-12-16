 
# @author: Lilian
 

import test_utils
from question_3 import ATOMS, molar_mass

         
# Question 3: check that the function computes the correct molecular mass
# of a valid molecule.
    
test_utils.assert_almost_equal(18.01534, molar_mass,([('H',2), ('O',1)],), 
                               description="Input [('H',2), ('O',1)]")
test_utils.assert_almost_equal(44.0098, molar_mass, ([('C',1), ('O',2)], ), 
                             description="Input [('C',1), ('O',2)]")
test_utils.assert_almost_equal(60.052679, molar_mass, ([('C',1), ('H',3), ('C',1), ('O',1), ('O',1), ('H',1)], ),
                             description="Input [('C',1), ('H',3), ('C',1), ('O',1), ('O',1), ('H',1)]")


    
# Question 3: check that the function returns None if the molecule
# contains an unknown atom (symbol).
    
test_utils.assert_is_None(molar_mass, ([('Cb',2), ('S',2), ('O',7)],), description="Input [('Cb',2), ('S',2), ('O',7)]")


