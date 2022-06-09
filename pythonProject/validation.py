
#function for checking length of data compared to length it MUST have

def is_valid_length(option,data, length):
    try:
        if option == 1:
            print(len(data), "length of data")
            if len(data) == length:
                print("1 ok")
                return True
            else:
                return False

        elif option == 2:
            print("option 2 is accessed")
            print(len(data))
            if len(data) >= length:
                print("2 ok")
                return True
            else:
                return False

        else:
            if len(data) < length:
                return False
            else:
                return True
    except:
        print("You entered an incorrect value ")


#function for checking the range a variable must have
#if the range is met it will return TRUE
#if the range is not met it will return FALSE



def is_range_valid(data,hi, lo, option):
    try:
#this option checks the data is within a certain range
#e.g. data is withon 1-100
        if option == 1:

            if hi - lo:
                return True
            else:
                return False

        elif option == 2:
            if hi - lo <= data:
                return True
            else:
                return False
        else:
            if hi-lo >= data:
                return True
            else:
                return False

    except:
        print("You entered an incorrect value ")