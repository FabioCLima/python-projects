import os

script_address = os.path.abspath(".")
script_address = os.path.abspath(__file__)
project_address = os.path.dirname(script_address)
data_address = os.path.join(project_address, 'data')
report_address = os.path.join(project_address, 'reports')
print(project_address)
print(script_address)
print(data_address)
print(report_address)
