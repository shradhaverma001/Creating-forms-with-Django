# CREATE OUR OWN FILTERS

from django import template

# CREATE AN OBJECT
register = template.Library()
@register.filter(name='cut')
# WRITE A FUNCTION THAT WILL BE OUR CUSTOM TEMPLATE FILTER
# value which is going to be pass from context_dict
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """ 
    return value.replace(arg,'')
# this function basically calls the replace method of the python string and the then pass in what you are looking for (arg) and what you want to replace it with. 
# this is a common python string operation.
#  register this function and pass in the string('cut') what I actually want to call this filter in custom filter template tag and the actual function(cut).

# register.filter('cut',cut)

# ANOTHER WAY TO register this function USING DECORATORS
# @register.filter(name='cut') this should be written above the function
