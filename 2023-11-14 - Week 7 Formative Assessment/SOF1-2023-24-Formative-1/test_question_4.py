# @author: Lilian
 

import test_utils
from question_4 import encrypt

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Question 4: check that the function encrypt a valid message. Check it 
# works with different alphabet.   
test_utils.assert_equals('CBCZ', encrypt, ('BABY', [1,1,1,1], alphabet), 
                         description="Inputs 'BABY', [1,1,1,1], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
test_utils.assert_equals('DBCB', encrypt, ('BABY', [2,1,1,3], alphabet), 
                         description="Inputs 'BABY', [2,1,1,3], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
test_utils.assert_equals('DBA', encrypt, ('BAC', [2,1,3], 'ABCDE'), 
                         description="Inputs 'BAC', [2,1,3], 'ABCDE'")


# Question 4: check that the function returns None if the size of
# the list of shifts is invalid.
test_utils.assert_is_None(encrypt, ('BABY', [2,1,1], alphabet), 
                         description="Inputs 'BABY', [2,1,1], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'",
                         failed='Check the size of the shifts.')
test_utils.assert_is_None(encrypt, ('BABY', [2,1,1,2,3], alphabet), 
                         description="Inputs 'BABY', [2,1,1,2,3], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'",
                         failed='Check the size of the shifts.')

# Question 4: check that the function returns None if one of the
# shifts is invalid (negative).   
test_utils.assert_is_None(encrypt, ('BABY', [2,1,1,-1], alphabet), 
                         description="Inputs 'BABY', [2,1,1,-1], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'",
                         failed='Check the values of the shifts.')

# Question 4: check that the function returns None  if one of the
# shifts is invalid (greater than the length of the alphabet).
test_utils.assert_is_None(encrypt, ('BABY', [2,1,1,27], alphabet), 
                         description="Inputs 'BABY', [2,1,1,27], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'",
                         failed='Check the values of the shifts.')

# Question 4: check that the function returns None  if one of the
# character is invalid (not in the alphabet).
test_utils.assert_is_None(encrypt, ('BABY', [2,1,1,2], 'ABC'), 
                         description="Inputs 'BABY', [2,1,1,2], 'ABC'",
                         failed='Check the content of the message to encrypt.')

