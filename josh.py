import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

#loading
def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Data Loaded Successfully.")
    print(data.head())
    return data

def preprocess_data(data):
    #numbering data
    data = pd.get_dummies(data, columns=['team'], drop_first=True)
    #isloating yards to predict
    X = data.drop(['yards'], axis=1) 
    y = data['yards']  
    return X, y

#training using 80% of the data and testing the rest
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training Set Size: {X_train.shape}")
    print(f"Testing Set Size: {X_test.shape}")
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

#r^2 value and error from known tests of 2024
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"\nMean Absolute Error: {mae}\nR-squared Score: {r2}")
    return mae, r2

#prediction for passing yards
def make_prediction(model, X, year, team):
    input_data = pd.DataFrame({
        'year': [year],
        **{col: 1 if f'team_{team}' == col else 0 for col in X.columns if col.startswith('team_')}
    }, columns=X.columns).fillna(0)
    
    predicted_yards = model.predict(input_data)
    print(f"Predicted Passing Yards for {team} in {year}: {predicted_yards[0]} \n")
    return predicted_yards[0]

#main, function calls
if __name__ == "__main__":
    file_path = "josh_allen_yards.csv"
    data = load_data(file_path)
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)


    year = 2024
    team = "pats" #REPLACE HERE FOR DESIRED TEAM
    make_prediction(model, X, year, team)