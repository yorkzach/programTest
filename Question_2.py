def max_val(x,y,z):
    max(x,y,z) # simple using python library

    # if wanting a real implementation
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
