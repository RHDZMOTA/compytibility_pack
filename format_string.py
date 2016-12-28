
# %% stringFormat function 

def formatStringV2(string, value):
    ref_index = string.find('{}')
    return string[:ref_index]+str(value)+string[ref_index+2:]

def formatString(string, values, version = '2.7'):
    
    if version == '2.7' or version == 2.7:
        for value in values:
            string = formatStringV2(string, value)
        return string
    
    if version == '3.5' or version == 3.5:
        
        this = 'string.format('+'values[0]'
        if len(values) == 1:
            return eval(this+')')
        
        for v in range(len(values)):
            this = this+','+'values[v]'
            
        return eval(this+')')
    else:
        print('Error: version not found.')
        
# %% 

# %% 

# %% 