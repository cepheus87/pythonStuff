import papermill as pm

pm.execute_notebook("Clean.ipynb", "Filled.ipynb", parameters=dict(alpha=0.1))
