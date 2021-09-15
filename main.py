import papermill as pm

# params1 = {"target_drive":"I","sound_file":"beep-01a.wav","output_path":"outputs"}
# pm.execute_notebook(
#    'drive_map_analysis.ipynb',
#    'outputs/drive_map_analysis_output1.ipynb',
#    parameters = params1
# )

# params2 = {"target_drive":"C","sound_file":"beep-01a.wav","output_path":"outputs"}
# pm.execute_notebook(
#    'drive_map_analysis.ipynb',
#    'outputs/drive_map_analysis_output2.ipynb',
#    parameters = params2
# )

params3 = {"base_path":"Y:","target_drive":"\\Unit_SCT","sound_file":"beep-01a.wav","output_path":"C:\\Users\\manakang\\Videos\\Repos\\papermill\\outputs"}
pm.execute_notebook(
   'drive_map.ipynb',
   'outputs/drive_map_output3.ipynb',
   parameters = params3
)

# params4 = {"target_drive":"C","sound_file":"beep-01a.wav","output_path":"outputs"}
# pm.execute_notebook(
#    'drive_map.ipynb',
#    'outputs/drive_map_output4.ipynb',
#    parameters = params4
# )