""" 

Creates dictonry from lists. 
It required 2 list, one for keys 
    and 2nd one containg values

"""
def list_to_dict(keys, values):
    return dict(zip(keys, values if len(keys) < len (values) else values + [None] * (len(keys) - len(values))))
