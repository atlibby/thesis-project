import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

def preprocess_dataset(input_file):
    # load file based on extension
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.parquet'):
        df = pd.read_parquet(input_file)
    else:
        raise ValueError("Unsupported file format")
        
    # drop rows with nulls
    df = df.dropna()

    # drop duplicates
    df = df.drop_duplicates()

    # fill missing values with column mean
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df.fillna(df.mean(numeric_only=True), inplace=True)
        
    # convert categorical columns to category dtype
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')
            
    return df
    
def normalize_features(df, feature_columns):
    # normalize specified feature columns
    scaler = StandardScaler()
    df[feature_columns] = scaler.fit_transform(df[feature_columns])
    return df, scaler # return scaler to inverse transform later if needed
    
def split_data(df, target_column, train_size=0.8, test_size=0.2, random_state=42):
    # split data into train and test sets
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, test_size=test_size, random_state=random_state, stratify=y)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # example usage
    # input_file = 'datasets/Benign-Monday-no-metadata.parque'
    # target_column = 'target'
    # feature_columns = ['feature1', 'feature2', 'feature3']
    
    # df = preprocess_dataset(input_file)
    # df, scaler = normalize_features(df, feature_columns)
    # X_train, X_test, y_train, y_test = split_data(df, target_column)
    
    # print("Preprocessing complete.")
    # print(f"Training set size: {X_train.shape[0]}")
    # print(f"Test set size: {X_test.shape[0]}")

    # count number of features in Benign-Monday-no-metadata.parquet and list them
    cicids_dir = 'datasets/CICIDS2017'
    toniot_dir = '/home/andrew-libby/VS Code Projects/PlatformIO/Projects/keyestudio_prototype_v1/datasets/TON-IoT'

    for file in os.listdir(cicids_dir):
        file_path = os.path.join(cicids_dir, file)
        df = preprocess_dataset(file_path)
        print(f"{file}: Number of features: {df.shape[1] - 1}") # subtract 1 for target column
        print("Feature columns:")
        for col in df.columns:
            if col != 'target':
                print(col)
    print("\n")

    for dir in os.listdir(toniot_dir):
        file_path = os.path.join(toniot_dir, dir)
        for file in os.listdir(file_path):
            dataset_path = os.path.join(file_path, file)
            df = preprocess_dataset(dataset_path)
            print(f"{dir}/{file}: Number of features: {df.shape[1] - 1}") # subtract 1 for target column
            print("Feature columns:")
            for col in df.columns:
                if col != 'target':
                    print(col)
    print("\n")
        # df = preprocess_dataset(file_path)
        # print(f"{file}: Number of features: {df.shape[1] - 1}") # subtract 1 for target column
        # print("Feature columns:")
        # for col in df.columns:
        #     if col != 'target':
        #         print(col)
