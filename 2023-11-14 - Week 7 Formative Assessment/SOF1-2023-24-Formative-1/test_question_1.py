#
# @author: Lilian
#
print('---------------Tests Question 1--------------------')

import test_utils
from question_1 import seconds_to_time


#
# Question 1: check that the function returns a correct time format when
# the parameter contains a time smaller than an hour.
#
test_utils.assert_equals('01:25', seconds_to_time, (85,), description='Input is 85')
test_utils.assert_equals('00:16', seconds_to_time, (16,), description='Input is 16')
test_utils.assert_equals('59:59', seconds_to_time, (3599,), description='Input is 3599')
test_utils.assert_equals('00:00', seconds_to_time, (0,), description='Input is 0')


#
# Question 1: check that the function returns a correct time format when
# the parameter is greater or equal to an hour.
#
test_utils.assert_equals('01:00:00', seconds_to_time, (3600,), description='Input is 3600')
test_utils.assert_equals('01:01:01', seconds_to_time, (3661,), description='Input is 3661')
test_utils.assert_equals('10:11:12', seconds_to_time, (36672,), description='Input is 36672')
test_utils.assert_equals('99:59:59', seconds_to_time, (359999,), description='Input is 359999')

#
# Question 1: check that the function returns None when
# the parameter is out of the time bounds.
#
test_utils.assert_is_None(seconds_to_time, (360000,), description='Input is 360000')
test_utils.assert_is_None(seconds_to_time, (376541,), description='Input is 376541')
test_utils.assert_is_None(seconds_to_time, (-1,), description='Input is -1')

print('---------------End Tests Question 1--------------------')
      