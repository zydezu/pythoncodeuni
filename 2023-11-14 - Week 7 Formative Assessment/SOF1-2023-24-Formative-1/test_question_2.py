 
# @author: Lilian
 
import test_utils
from question_2 import time_to_seconds

# Question 2: check that the function returns the correct time when
# the paramter is a valid time using hours, minutes, and seconds.
    
test_utils.assert_equals(4210, time_to_seconds, ('01:10:10',), 
                        description="Input '01:10:10'")
test_utils.assert_equals(3600, time_to_seconds, ('01:00:00',), 
                        description="Input '01:00:00'")
test_utils.assert_equals(359999, time_to_seconds, ('99:59:59',), 
                        description="Input '99:59:59'")

# Question 2: check that the function returns the correct time when
# the paramter is a valid time using minutes and seconds.
    
test_utils.assert_equals(0, time_to_seconds, ('00:00',), 
                        description="Input '00:00'")
test_utils.assert_equals(61, time_to_seconds, ('01:01',), 
                        description="Input '01:01'")
test_utils.assert_equals(3599, time_to_seconds, ('59:59',), 
                        description="Input '59:59'")

# Question 2: check that the function returns None when
# the paramter is not a valid time. For example, having more than 59 minutes,
# or more than 59 seconds, or the hours are 00. In addition the time should
# be less than 100 hours.
    
test_utils.assert_is_None(time_to_seconds, ('60:10',), 
                        description="Input '60:10'")
test_utils.assert_is_None(time_to_seconds, ('10:60',), 
                        description="Input '10:60'")
test_utils.assert_is_None(time_to_seconds, ('1:10:50',), 
                        description="Input '1:10:50'")
test_utils.assert_is_None(time_to_seconds, ('100:10:50',), 
                        description="Input '100:10:50'")
test_utils.assert_is_None(time_to_seconds, ('00:10:50',), 
                        description="Input '00:10:50'")
