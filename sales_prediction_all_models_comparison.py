# -*- coding: utf-8 -*-
"""sales_prediction_all_models_comparison(1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ifTHbR3NvD0fhNBhkLJuAkHYME0dD4Pm
"""

import pandas as pd

master_data = pd.read_csv('Book2.csv',sep=',', encoding='latin-1')
print('data shape: ', master_data.shape)
master_data.head()

master_data.info()
master_data_copy=master_data.copy()

cleaned_data=master_data_copy.drop(['Name'], axis=1)
cleaned_data.head()

cleaned_data_copy = cleaned_data.copy()
cleaned_data_copy.head()

Qualification_dic={"NA":1,
                  "BSC-IT":2,
"Diplomo-Mechanical":3,
"BBA":4,
"Bcom":5,
"BE/BTech-CS":6,
"MBA":7,
"MA":8,
"BE/BTech-E&C":9,
"BSC-Physics":10,
"BE/BTech-E&T":11,
"Mcom":12,
"12th":13,
"BSC":14,
"BE/Btech-Mechanical":15,
"BA":16,
"BE/BTech":17,
"12th ":18,
"MCA":19,
"BE-Mech":20,
"BCA":21,
"BE/BTech-Automobiles":22,
"BE/BTech-EEE":23,
"Others":24,
"Mtech/ME":25,
"Diplomo-EEE":26,
"BE/BTech-Civil":27,
"MSC-CS":28,
"BSC- Chemistry":29,
"BSC-CS":30,
"BE/BTech-IT":31,
"BT/BTech-Chemical":32,
"MSC-IT":33,
"MSc":34,
"Diplomo-CS":35,
"Diplomo-Civil":36,
"Btech -Mech":37,
"Bsc-CS - MBA":38,
"Bsc -Maths":39,
"BE":40,
"Btech-IT":41,
"Masters in computers":42,
"Btech-CS (89//89//59)":43,
"BE -Mech":44,
}

Employment_Status_dic={"NA":1,
"Not working":2,
"Working":3,
"Others":4,
"Fresher":5,
"3.5lpa":6,
"4.9lpa":7,
"18k":8,
"89000 per month":9,}

Salary_dic={"NA":1,
"40000":2,
"32000":3,
"4.5 lpa":4,
"4.2 LPA":5,
"4.25LPA":6,
"3lpa ":7,
"5.7lpa":8,
"7.5 LPA":9,
"18.5LPA":10,
"13000":11,
"2lpa":12,
"4.2LPA":13,
"5lpa":14,
"40000PM":15,
"3.7LPA":16,
"3lpa":17,
"15000":18,
"4LPA":19,
"8.7LPA":20,
"5.5lpa":21,
"40000 PM":22,
"25000 PM":23,
"12000 P M":24,
"3.1LPA":25,
"3.5 LPA":26,
"3.5LPA":27,
"18000 PM":28,
"20000":29,
"3.2 LPA":30,
"25000":31,
"6lpa":32,
"8lpa":33,
"8 lPA":34,
"2.7LPA":35,
"17000 in hand ":36,
"21000":37,
"1.2LPA":38,
"16500":39,
"22000":40,
"22000 PM":41,
"3.6lpa":42,
"55000PM":43,
"50000":44,
"6.5LPA":45,
"4.28LPA":46,
"2.5lpa":47,
"4.85":48,
"4.8lpa":49,
"6.5 LPA":50,
"2.4 lpa":51,
"1.5L":52,
"2.2L":53,
"2L":54,
"4.2L":55,
"5L":56,
"10L":57,
"6.45L":58,
"1.4L":59,
"3.6L":60,
"4L":61,
"2.6L":62,
"3L":63,
"25k":64,
"Very less":65,
"10K":66,
"4.5L":67,
"2.4L":68,
"6L":69,
"20k":70,
"3.3L":71,
"15K":72,
"7L":73,
"15k / month":74,
"18k":75,
"600 per day":76,
"3.9L":77,
"4.8 LPA":78,
"2.3 LPA":79,
"2.5L":80,
"2.8 LPA":81,
"1.4lpa":82,
"84k per year":83,
"25k monthly":84,
"3.3LPA":85,
"20k per month":86,
"4.5LPA":87,
"9LPA":88,
"24k":89,
"3.8LPA":90,
"10LPA":91,
"7LPA":92,
"29k":93,
"":94,
"16LPA":95,
"4.4lpa":96,
"20LPA":97,
"5.8lpa":98,
"2.4LPA":99,
"invalid":100,
"Not interested":101,
"Followup(cold)":102,
"Followup(CBL)":103,
"Non contact":104,
"Followup(warm)":105,
"11.9L":106,
"4lpa ":107,
"12LPA":108,}

Sub_stage_dic={"Attempt above 5":1,
"Not comfortable in English":2,
"Not aware of showing any interest":3,
"No Financial support ":4,
"Call Back Later":5,
"Not valid for our program":6,
"Family din't agreed":7,
"Wrong Number":8,
"Change of Plans":9,
"Warm ":10,
"No particular reason":11,
"Cold":12,
"12th Std":13,
"looking for other courses":14,
"Cibil issue":15,
"Disconnected the call saying not interested ":16,
"Looking for job":17,
"Undergraduate":18,
"Already done course":19,
"Incoming call restricted":20,
"Fees is tooo high":21,
"Not in service":22,
"Joined somewhere else":23,
"Need Pay after placement":24,
"personal reason":25,
"Looking for future batches":26,
"Disconnected the call":27,
"financial issue":28,
"Dropped a message as not interested":29,
"High Foir":30,
"Attempt 5 ":31,
"Looking for only internship":32,
"Need course for shorter period":33,
"NA":34,
"Looking for offline classes":35,
"Attempt 4":36,
"Attempt 2":37,
"Hot":38,
"Attempt 1":39,
"Attempt 3":40,
"Others":41,
"Still pursuing bachelors":42,
"Warm":43,
"Batch timings is not flexible":44,
"":45,
"Looking for offline":46,
}

Lead_Stage_dic={"Non Contact":1,
"Invalid":2,
"Not Interested":3,
"In contact":4,
"Follow Up":5,
"Undergraduate":6,
"Future Batches":7,
"Loan Rejected":8,
"Duplicate":9,
"Deal Won ":10,
"Documents Collected":11,
"":12,
"Deal Won":13,
}

def clean_map(df, dictToMap, oldColName):
    """This will take a dataframe,
    a number of column names &
    create new columns of datetime objects"""
    newColName = oldColName + "_map"
    df[newColName] = df[oldColName].map(dictToMap)
    del df[oldColName]
    return df

data_only_numbers=cleaned_data_copy.copy()

data_only_numbers.info()

data_only_numbers = clean_map(data_only_numbers, Qualification_dic, 'Qualification')
data_only_numbers = clean_map(data_only_numbers, Employment_Status_dic, 'Employment Status')
data_only_numbers = clean_map(data_only_numbers, Salary_dic, 'Salary')
data_only_numbers = clean_map(data_only_numbers, Sub_stage_dic, 'Sub stage')
data_only_numbers = clean_map(data_only_numbers, Lead_Stage_dic, 'Lead Stage')

data_only_numbers

data_only_numbers.info()

print(data_only_numbers.isnull().sum())

mydataset_without_null = data_only_numbers.fillna(0)

print(mydataset_without_null.isnull().sum())

procesed_data_copy=mydataset_without_null.copy()

procesed_data_copy.head()

y=procesed_data_copy.iloc[:, 6]
x=procesed_data_copy.drop(['Lead Stage_map'], axis=1)
x.head()

y.head()

import numpy as np

"""after running " *from mlxtend.feature_selection import SequentialFeatureSelector as SFS* " this command you might get error this is because mlxtend is trying to import joblib from sklearn but it no longer exist there so fix this issue go to the file location (there will a file location link in the error message like this " /usr/local/lib/python3.7/dist-packages/mlxtend/feature_selection/sequential_feature_selector.py <module> " click on this location link)
then it will show you code written in that file then you just have to look for this line " from sklearn.externals.joblib import Parallel, delayed " and edit it to " from joblib import Parallel, delayed " and then save it by pressing ctrl+s. then run the code again. Again it will give error but this time the location link will be different and you have to again edit the file in same way as done priviouslly and save it and run the code again and this will solve the error.
"""

from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
from sklearn.svm import SVC
svc = SVC()

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
from xgboost import XGBClassifier
gb = XGBClassifier()

efs = EFS(gb, # can use any any learning method
          min_features=1,
          max_features=4,
          scoring='accuracy',
          print_progress=True,
          cv=2
          ).fit(np.array(x[x.columns[0:4]].fillna(0)), y)

print(efs.best_idx_)

# x with feature selection
x_reduced = efs.transform(x)
x_reduced.shape

# x without feature selection
x.shape

y.shape

# normal spliting with feature selection
from sklearn.model_selection import train_test_split
x_f_train, x_f_test, y_f_train, y_f_test = train_test_split(x_reduced, y, test_size=0.2, random_state=42, shuffle=True)

# normal spliting without feature selection
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, shuffle=True)

x_train

from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

#without feature selection
gb = XGBClassifier()
gb.fit(x_train,y_train)

y_pred_gb = gb.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print("Accuracy Score: ",accuracy_score(y_test, y_pred_gb))

#with feature selection
gb = XGBClassifier()
gb.fit(x_f_train,y_f_train)

y_pred_gb = gb.predict(x_f_test)

print("Accuracy Score: ",accuracy_score(y_f_test, y_pred_gb))

#20% for training and 80% for testing without feature selection
x_b_train, x_b_test, y_b_train, y_b_test = train_test_split(x, y, test_size=0.8, random_state=42, shuffle=True)

gb_b = XGBClassifier()
gb_b.fit(x_b_train,y_b_train)

y_pred_gb_b = gb_b.predict(x_b_test)

print("Accuracy Score: ",accuracy_score(y_b_test, y_pred_gb_b))

#20% for training and 80% for testing with feature selection
x_f_b_train, x_f_b_test, y_f_b_train, y_f_b_test = train_test_split(x_f_train, y_f_train, test_size=0.8, random_state=42, shuffle=True)

gb_b = XGBClassifier()
gb_b.fit(x_f_b_train,y_f_b_train)

y_pred_gb_b = gb_b.predict(x_f_b_test)

print("Accuracy Score: ",accuracy_score(y_f_b_test, y_pred_gb_b))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, shuffle=True)

#without feature selection
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(x_train,y_train)

y_pred_rf = rf.predict(x_test)
print("Accuracy Score: ",accuracy_score(y_test, y_pred_rf))

# with feature selection
rf=RandomForestClassifier()
rf.fit(x_f_train,y_f_train)

y_pred_rf = rf.predict(x_f_test)
print("Accuracy Score: ",accuracy_score(y_f_test, y_pred_rf))

# without feature selection
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train,y_train)

ylr_pred = logreg.predict(x_test)

print("Accuracy Score: ", accuracy_score(ylr_pred, y_test))

# with feature selection
logreg = LogisticRegression()
logreg.fit(x_f_train,y_f_train)

ylr_pred = logreg.predict(x_f_test)
print("Accuracy Score: ", accuracy_score(ylr_pred, y_f_test))