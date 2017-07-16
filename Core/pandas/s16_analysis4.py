import pandas as pd
import numpy as np
from sklearn import svm, preprocessing, model_selection

# get data
hpi_states = pd.read_pickle("hpi_states.pickle")
hpi_rest = pd.read_pickle("hpi.pickle")
hpi = hpi_states.join(hpi_rest)

# prepare data
hpi = hpi.pct_change()
hpi.replace([np.inf, -np.inf], np.nan, inplace=True)
hpi["USA_F"] = hpi["USA"].shift(-1)
hpi["Label"] = (hpi["USA_F"] > hpi["USA"])*1
hpi.dropna(inplace=True)

# prediction
# data = hpi[["USA"]]  # usa 55%
data = hpi.drop(["USA_F", "Label"], 1)  # all 70%
# data = hpi.drop(["MORG", "SP500", "GDP", "UNEMPLOYMENT", "USA_F", "Label"], 1)  # states 65%
# data = hpi[["USA", "MORG", "SP500", "GDP", "UNEMPLOYMENT"]]  # 58%
print(data.head())

features = np.array(data)
features = preprocessing.scale(features)
labels = np.array(hpi["Label"])
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, train_size=0.2)
classifier = svm.SVC(kernel="linear")
classifier.fit(features_train, labels_train)
result = classifier.score(features_test, labels_test)
print(result)
