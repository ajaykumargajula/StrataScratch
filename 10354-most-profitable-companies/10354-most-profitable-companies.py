res = forbes_global_2010_2014.groupby('company')['profits'].sum().reset_index().sort_values(by='profits', ascending=False)
res = res[res['profits'].rank(method='max',ascending=False)<=3]
