# Import your libraries
import pandas as pd
import numpy as np
# Start writing code
db_employee['department'] = db_employee['department_id'].map(dict(zip(db_dept['id'],db_dept['department'])))
np.abs(db_employee[db_employee['department']=='marketing']['salary'].max())-(db_employee[db_employee['department']=='engineering']['salary'].max())
