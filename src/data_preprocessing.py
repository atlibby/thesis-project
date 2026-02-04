""" function: preprocess_dataset(input_file):
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
            df[col].fillna(df[col].mean(), inplace=True)
        
        # convert categorical columns to category dtype
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype('category')
            
        return df
    
    function: normalize_features(df, feature_columns):
        # normalize specified feature columns
        scaler = StandardScaler()
        df[feature_columns] = scaler.fit_transform(df[feature_columns])
        return df, scaler # return scaler to inverse transform later if needed
    
    function: split_data(df, target_column, train_size=0.8, test_size=0.2, random_state=42):
        # split data into train and test sets
        X = df.drop(columns=[target_column])
        y = df[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, test_size=test_size, random_state=random_state, stratify=y)
        return X_train, X_test, y_train, y_test
"""