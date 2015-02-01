# lambda function

Example of how to use lambda function in data analysis with pandas.

In this scenario, we have to_float() that works with one value, but we want to apply the function to a DataFrame.
lambda function allows us to create a function that takes a row or a column of data and operates on a single value,
which is required by to_float().

    >>def to_float(x):
      '''returns float value of x or NaN'''
      try:
          x = float(x)
      except (ValueError, UnicodeEncodeError):
          return np.nan
      else:
          return x

    >>data[['Glucose', 'Triglyceride', 'HDL-C', 'Systolic', 'Diastolic']].apply(lambda x: x.map(to_float)).head()
