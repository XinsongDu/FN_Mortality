[![HitCount](http://hits.dwyl.com/XinsongDu/FN_Mortality.svg)](http://hits.dwyl.com/XinsongDu/FN_Mortality)

## Predicting In-hospital Mortality of Patients with Febrile Neutropenia Using Machine Learning Models (Manuscript in preparation)

Several commonly used machine leanring models, as well as deep neural network, were built upon [Healthcare Cost and Utilization Project (HCUP)’s National Inpatient Sample (NIS)](https://www.hcup-us.ahrq.gov/db/nation/nis/nisdbdocumentation.jsp) data to predict the mortality of adult cancer febrile neutropenia admissions. Machine learning models achieved areas under the receiver operating characteristic (AUROC) above 90%.

Variable importance analysis was also conducted with ridge logistic regression and gradient boosting tree. The variable importance analysis results consistent with previous studies.

> - You are welcome to re-use any code from this repo for your project, please cite this paper: https://www.sciencedirect.com/science/article/pii/S1386505619314078?via%3Dihub.
> - Please refer to our [wiki](https://github.com/XinsongDu/FN_Mortality/wiki) for more information regarding how to use our code to do different things related to HCUP data

---

## Requirements:

- Python 2.7
- Python 3.6
- Pandas 0.21.1
- Numpy 1.14.5
- Pyhcup 0.1.6.4
- Scikit-learn 0.19.2
- Pandas-summary 1.11.0
- Scipy 1.14.5

---

## Workflow

![alt text](https://github.com/XinsongDu/FN_Mortality/blob/master/fig/workflow.png)

## Datasets:

- [Healthcare Cost and Utilization Project (HCUP)’s National Inpatient Sample (NIS)](https://www.hcup-us.ahrq.gov/db/nation/nis/nisdbdocumentation.jsp) from 2007 to 2015 third quarter.

---

## Experiment Procedure (Use python 3 if not specified):

#### Descriptive statistics, trend analysis and data preparation

- Run src/sas2csv.py with **Python 2** to convert ASCII files to csv. Use the following code to convert the ASCII files of core, hospital, severity and diagnose/procedure group of each year to csv.
```bash
python src/sas2csv.py -d {path of ASC file} -l {path of corresponding SAS load file} -o {path of the directory of output csv file} -y {year of data}
```
- Use nbs/files_combination_each_year.ipynb to merge core, hospital, severity and diagnose/procedure group files of each year to one file.
- Run through nbs/train_test_generator.ipynb to get the number of cancer, febrile neutropenia (FN) and FN death of each year, and generate a csv file including all adult cancer FN admissions of each year.
- Run nbs/merge_all_year_data.ipynb to merge all years' adult cancer FN admissions to one file, which is for machine learning models training and evaluation.
- Run nbs/combined_inputs_generator.ipynb to do one hot encoding for diagnose/procedure variables.
- Run nbs/missing_data_imputation.ipynb to do data imputation (using mean values for continuous variables, most common values for categorical variables)
- Use nbs/desctiptive_statistics.ipynb to get statistics of selected data. P-values for proportions were calculated with [z score calculator online](https://www.socscistatistics.com/tests/ztest/Default2.aspx); p-values for continuous variables were calculated with python.

#### Sample Selection Bias Test

- Use nbs/file_preparison_for_selection_bias_test.ipynb to generate files containing samples with age value and without age value separately.
- Use nbs/train_test_generator.ipynb and nbs/merge_all_year_data.ipynb to get adult FN samples with missing died information and without.
- Use nbs/Selection_bias_test.ipynb to test whether removing samples with missing age/died value will introduce bias or not.
- Consort diagram:
![alt text](https://github.com/XinsongDu/FN_Mortality/blob/master/fig/consort_diagram.jpeg)

#### Diagnose/procedure ontology evaluation

- Use random forest as the learning algorithm. Run nbs/dx_pr_selection.ipynb to test predictive power of different diagnose/procedure coding systems.

#### Model training, evaluation and predictor analysis

- nbs/Model_Development.ipynb

## More

- Please post your question in [issue tracker](https://github.com/XinsongDu/FN_Mortality/issues)
