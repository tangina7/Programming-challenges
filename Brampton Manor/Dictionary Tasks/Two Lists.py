def createDict(keys, values):
    keysLength = len(keys)
    dictionary = {}
    for i in range (0, keysLength):
        
        if len(values) <= i:
            values.append(None)
            
        key = keys[i]
        dictionary[key] = values[i]

    return dictionary

