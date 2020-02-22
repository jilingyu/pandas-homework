import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


# We're now creating a dataframe straight from a data file
insurance = pd.read_csv(filepath_or_buffer='C:/Users/admin/Desktop/git-pandas/pandas-homework/insurance.csv',
                      sep=',',
                      header=0)

print(insurance.to_string())
print(insurance.columns)
print(insurance.index)
print(insurance.dtypes)
print(insurance.shape)
print(insurance.info())
print(insurance.describe())

print(insurance['age'])
print(insurance['age','children','charges'])
print(insurance.loc[[0,1,2,3,4],[['age','children','charges']]])
print(insurance.mean())
print(insurance.min())
print(insurance.max())
print(insurance.smoker[insurance.charges = 10797.3362])
print(insurance.age[insurance.max()])
#How many insured people do we have for each region?
print(insurance.sum[insurance.region])
#How many insured people are children?
print(insurance.sum[insurance.age < 18])
#What do you expect to be the correlation between charges and age, bmi and children?
print(insurance.corr())
#Using the method corr(), check if your assumptions were correct.
print(insurance.corr())
