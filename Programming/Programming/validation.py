
#function for checking length of data compared to length it MUST have

def is_valid_length(data, length, option):
    if option == 1:
        if len(data) == length:
            return True
        else:
            return False

    elif option == 2:
        if len(data) >= length:
            return True
        else:
            return False

    else:
        if len(data) < length:
            return False
        else:
            return True



#function for checking the range a variable must have
#if the range is met it will return TRUE
#if the range is not met it will return FALSE



def is_range_valid(data,hi, lo, option):
#this option checks the data is within a certain range
#e.g. data is withon 1-100
    if option == 1:
        if hi > data and data > lo:
            return True
        else:
            return False
        
    elif option == 2:
        if hi - lo == data:
            return True
        else:
            return False
    else:
        if hi-lo >= data:
            return True
        else:
            return False

    
