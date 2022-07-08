def closest_in_list(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def closest_in_dict(dict_in, value_in):
    res_key, res_val = min(dict_in.items(), key=lambda x: abs(value_in - x[1]))
    return res_key, res_val