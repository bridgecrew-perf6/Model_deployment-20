import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
data = pd.read_csv('cpdata.csv')

features = ['temperature', 'humidity', 'ph', 'rainfall']
X = data[features]
Y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

classifier = RandomForestClassifier(n_estimators=150, max_depth=15)
classifier.fit(X_train, y_train)
pickle.dump(classifier,open('model.pkl','wb'))
def predictions(inputs):

    return classifier.predict(inputs)
