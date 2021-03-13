import papermill as pm

pm.execute_notebook(
   'mill1.ipynb',
   'outputs/output1.ipynb',
   parameters = dict(alpha=0.6, ratio=0.2)
)

pm.execute_notebook(
   'mill2.ipynb',
   'outputs/output2.ipynb',
   parameters = dict(alpha=0.4, ratio=0.1 )
)