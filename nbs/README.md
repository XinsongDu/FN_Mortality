file_name                   |  description
-----------------------------|----------------------------------------------------------------------------------------
descriptive_statistics       |  calculate descriptive statistics for selected admissions
files_combination_each_year  |  merge core, hospital, severity and diagnose/procedure groups file into one.
combined_inputs_generator    |  merge variables from all domains into one data file
mimic_learning               |  neural network tuning, log probalility extraction, and drawing optimized decision tree
param_tuning                 |  parameter tuning for diagnose/procedure coding systems
variable_filtering           |  eliminate unimportant variables using ridge logistic regression
variable_importance          |  combine variable importance txt files of 10 times bootstrap into one csv file
merge_all_year_data          |  merge data from all years into one
missing_data_imputation      |  impute missing data for both categorical and numerical variables
t-test                       |  perform Bengio's corrected t-test for repeated cross validation