
# @author: Lilian


import test_utils
from question_5 import molecule_to_list

# Question 5: check that the function handles molecules composed of 
# single character molecules only.       
test_utils.assert_equals([('H',2), ('O',1)], molecule_to_list, ('H2O',), 
                         description= "Input 'H2O'")
test_utils.assert_equals([('C',1), ('O',2)], molecule_to_list, ('CO2',), 
                         description= "Input 'CO2'")
test_utils.assert_equals([('C',6), ('H',12), ('O',6)], molecule_to_list, ('C6H12O6',), 
                         description= "Input 'C6H12O6'")
test_utils.assert_equals([('C',1), ('H',3), ('C',1), ('O',1), ('O',1), ('H',1)], 
                         molecule_to_list, ('CH3COOH',), 
                         description= "Input 'CH3COOH'")


# Question 5: check that the function handles molecules composed of 
# single or multiple characters molecules.        
test_utils.assert_equals([('Ca',1), ('C',1), ('O',3)], molecule_to_list, ('CaCO3',),  
                         description= "Input 'CaCO3'")
test_utils.assert_equals([('Na',1), ('H',1), ('S',1), ('O',4)], molecule_to_list, ('NaHSO4',),  
                         description= "Input 'NaHSO4'")
test_utils.assert_equals([('Na',2), ('S',2), ('O',7)], molecule_to_list, ('Na2S2O7',),  
                         description= "Input 'Na2S2O7'")


# Question 5: check that the function returns None if the molecule
# contains non alphabet symbols.
test_utils.assert_is_None(molecule_to_list, ('C++H3COOHCa',), 
                          description= "Input 'C++H3COOHCa'",
                          failed="Check the symbols used in molecules.")

# Question 5: check that the function returns None if the molecule
# starts with a lower case character.
test_utils.assert_is_None(molecule_to_list, ('cO2',), 
                          description= "Input 'cO2'",
                          failed="Check the upper/lower case of molecules.")

# Question 5: check that the function returns None if the molecule
# contains an atom symbol starting with a lower case character.
test_utils.assert_is_None(molecule_to_list, ('H2o',), 
                          description= "Input 'H2o'",
                          failed="Check the upper/lower case of molecules.")
