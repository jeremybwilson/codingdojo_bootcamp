# For loop

# create a new list
# remember lists can hold many data-types, even lists!

def ultimateAnalyze(some_list):
  dictionary = {'Sum Total': 0, 'Average': 0, 'Minimum': 0, 'Maximum': 0, 'Length': 0}

  sum_list = sum(some_list)
  dictionary['Sum Total'] = sum_list
  dictionary['Length'] = len(some_list)
  dictionary['Average'] = sum_list / len(some_list)
  dictionary['Minimum'] = min(some_list)
  dictionary['Maximum'] = max(some_list)

  return dictionary

print (ultimateAnalyze([1,4,8,10, 25, 50, 100]))