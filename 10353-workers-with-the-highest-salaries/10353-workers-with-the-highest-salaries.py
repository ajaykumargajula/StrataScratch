import pandas as pd
worker= pd.read_csv('worker.csv')
title = pd.read_csv('title.csv')
data = worker.merge(title,how='left',left_on='worker_id',right_on='worker_ref_id')
result = data[data['salary'] == data['salary'].max()]['worker_title']
