# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

class preprocessing:
    
    def __init__(self):
        pass

    def preprocess_Xtrain(self, df):
        import pandas as pd
        import numpy as np

        df.columns = ['q', 'confidence_(0.5, 0.55]',
               'confidence_(0.55, 0.6]', 'confidence_(0.6, 0.65]',
               'confidence_(0.65, 0.7]', 'confidence_(0.7, 0.75]',
               'confidence_(0.75, 0.8]', 'confidence_(0.8, 0.85]',
               'confidence_(0.85, 0.9]', 'confidence_(0.9, 0.95]',
               'confidence_(0.95, 1.0]', 'sc_(0.0, 0.05]', 'sc_(0.05, 0.1]',
               'sc_(0.1, 0.15]', 'sc_(0.15, 0.2]', 'sc_(0.2, 0.25]', 'sc_(0.25, 0.3]',
               'sc_(0.3, 0.35]', 'sc_(0.35, 0.4]', 'sc_(0.4, 0.45]', 'sc_(0.45, 0.5]',
               'sc_(0.5, 0.55]', 'sc_(0.55, 0.6]', 'sc_(0.6, 0.65]', 'sc_(0.65, 0.7]',
               'sc_(0.7, 0.75]', 'sc_(0.75, 0.8]', 'sc_(0.8, 0.85]', 'sc_(0.85, 0.9]',
               'sc_(0.9, 0.95]', 'sc_(0.95, 1.0]', 'number_of_participants', 'own_percentage',
               'topic', 'mean_sc', 'std_sc', 'min_sc', 'p25_sc', 'p50_sc', 'p75_sc',
               'max_sc', 'mean_conf', 'std_conf', 'min_conf', 'p25_conf', 'p50_conf',
               'p75_conf', 'max_conf', 'skew_own', 'skew_sc', 'skew_conf',
               'skew_row_average', 'skew_row_skew', 'minority_percentage',
               'real_expert_number', 'P_expert_number_rT', 'P_expert_number_rF', 
               'MEAN_P_expert_rT', 'MEAN_P_expert_rF', 'prelec_prediction', 'majority_prediction']

        cont_features = ['confidence_(0.5, 0.55]',
                         'confidence_(0.55, 0.6]', 'confidence_(0.6, 0.65]',
                         'confidence_(0.65, 0.7]', 'confidence_(0.7, 0.75]',
                         'confidence_(0.75, 0.8]', 'confidence_(0.8, 0.85]',
                         'confidence_(0.85, 0.9]', 'confidence_(0.9, 0.95]',
                         'confidence_(0.95, 1.0]', 'sc_(0.0, 0.05]', 'sc_(0.05, 0.1]',
                         'sc_(0.1, 0.15]', 'sc_(0.15, 0.2]', 'sc_(0.2, 0.25]', 'sc_(0.25, 0.3]',
                         'sc_(0.3, 0.35]', 'sc_(0.35, 0.4]', 'sc_(0.4, 0.45]', 'sc_(0.45, 0.5]',
                         'sc_(0.5, 0.55]', 'sc_(0.55, 0.6]', 'sc_(0.6, 0.65]', 'sc_(0.65, 0.7]',
                         'sc_(0.7, 0.75]', 'sc_(0.75, 0.8]', 'sc_(0.8, 0.85]', 'sc_(0.85, 0.9]',
                         'sc_(0.9, 0.95]', 'sc_(0.95, 1.0]', 'number_of_participants', 'own_percentage',
                         'mean_sc', 'std_sc', 'min_sc', 'p25_sc', 'p50_sc', 'p75_sc',
                         'max_sc', 'mean_conf', 'std_conf', 'min_conf', 'p25_conf', 'p50_conf',
                         'p75_conf', 'max_conf', 'skew_own', 'skew_sc', 'skew_conf',
                         'skew_row_average', 'skew_row_skew', 'minority_percentage',
                         'real_expert_number', 'P_expert_number_rT', 'P_expert_number_rF',
                         'MEAN_P_expert_rT', 'MEAN_P_expert_rF']

        q = df["q"]
        df = df.set_index('q')

#         #Target Variable
#         from sklearn.preprocessing import LabelEncoder

#         # Actual Answer (0 or 1)
#         le = LabelEncoder()
#         df['actual'] = le.fit_transform(df['actual'])
    
        from sklearn.preprocessing import OneHotEncoder
        enc_onehot = OneHotEncoder(sparse=False, handle_unknown='ignore')

        # topic - the topic of the question
        df_topic = enc_onehot.fit_transform(df[['topic']])
        df_topic = pd.DataFrame(df_topic)
        df_topic.columns = enc_onehot.get_feature_names()
        df = df.drop('topic', 1)

        from sklearn.preprocessing import StandardScaler
        s_scaler = StandardScaler()

        # Number of Participants
        for f in cont_features:
            df[f] = s_scaler.fit_transform(df[[f]])

        df_final = df
        df_topic = df_topic.set_index(q)
        df_final = pd.concat([df, df_topic], axis=1)
#         actual_result = df_final["actual"]
#         df_final = df_final.drop("actual", axis=1)
#         df_final["actual"] = actual_result

        arr = []
        for c in df_final.columns:
            if "meta" in c:
                c = c.replace("meta", "sc")
            arr.append(c)
        df_final.columns = arr

        return df_final, enc_onehot, s_scaler
    
    def preprocess_ytest(self, df, le):
        import warnings
        warnings.filterwarnings("ignore")
        #Target Variable
#         from sklearn.preprocessing import LabelEncoder

#         # Actual Answer (0 or 1)
#         le = LabelEncoder()
        x = le.transform(df['actual'])
        df.loc[:,'actual'] = x
        return df
    
    def preprocess_ytrain(self, df):
        import warnings
        warnings.filterwarnings("ignore")
        #Target Variable
        from sklearn.preprocessing import LabelEncoder

        # Actual Answer (0 or 1)
        le = LabelEncoder()
        x = le.fit_transform(df['actual'])
        df.loc[:,'actual'] = x
        return df, le
    
    def preprocess_Xtest(self, df, enc_onehot, s_scaler):
        import pandas as pd
        import numpy as np

        df.columns = ['q', 'confidence_(0.5, 0.55]',
               'confidence_(0.55, 0.6]', 'confidence_(0.6, 0.65]',
               'confidence_(0.65, 0.7]', 'confidence_(0.7, 0.75]',
               'confidence_(0.75, 0.8]', 'confidence_(0.8, 0.85]',
               'confidence_(0.85, 0.9]', 'confidence_(0.9, 0.95]',
               'confidence_(0.95, 1.0]', 'sc_(0.0, 0.05]', 'sc_(0.05, 0.1]',
               'sc_(0.1, 0.15]', 'sc_(0.15, 0.2]', 'sc_(0.2, 0.25]', 'sc_(0.25, 0.3]',
               'sc_(0.3, 0.35]', 'sc_(0.35, 0.4]', 'sc_(0.4, 0.45]', 'sc_(0.45, 0.5]',
               'sc_(0.5, 0.55]', 'sc_(0.55, 0.6]', 'sc_(0.6, 0.65]', 'sc_(0.65, 0.7]',
               'sc_(0.7, 0.75]', 'sc_(0.75, 0.8]', 'sc_(0.8, 0.85]', 'sc_(0.85, 0.9]',
               'sc_(0.9, 0.95]', 'sc_(0.95, 1.0]', 'number_of_participants', 'own_percentage',
               'topic', 'mean_sc', 'std_sc', 'min_sc', 'p25_sc', 'p50_sc', 'p75_sc',
               'max_sc', 'mean_conf', 'std_conf', 'min_conf', 'p25_conf', 'p50_conf',
               'p75_conf', 'max_conf', 'skew_own', 'skew_sc', 'skew_conf',
               'skew_row_average', 'skew_row_skew', 'minority_percentage',
               'real_expert_number', 'P_expert_number_rT', 'P_expert_number_rF', 
               'MEAN_P_expert_rT', 'MEAN_P_expert_rF', 'prelec_prediction', 'majority_prediction']

        cont_features = ['confidence_(0.5, 0.55]',
                         'confidence_(0.55, 0.6]', 'confidence_(0.6, 0.65]',
                         'confidence_(0.65, 0.7]', 'confidence_(0.7, 0.75]',
                         'confidence_(0.75, 0.8]', 'confidence_(0.8, 0.85]',
                         'confidence_(0.85, 0.9]', 'confidence_(0.9, 0.95]',
                         'confidence_(0.95, 1.0]', 'sc_(0.0, 0.05]', 'sc_(0.05, 0.1]',
                         'sc_(0.1, 0.15]', 'sc_(0.15, 0.2]', 'sc_(0.2, 0.25]', 'sc_(0.25, 0.3]',
                         'sc_(0.3, 0.35]', 'sc_(0.35, 0.4]', 'sc_(0.4, 0.45]', 'sc_(0.45, 0.5]',
                         'sc_(0.5, 0.55]', 'sc_(0.55, 0.6]', 'sc_(0.6, 0.65]', 'sc_(0.65, 0.7]',
                         'sc_(0.7, 0.75]', 'sc_(0.75, 0.8]', 'sc_(0.8, 0.85]', 'sc_(0.85, 0.9]',
                         'sc_(0.9, 0.95]', 'sc_(0.95, 1.0]', 'number_of_participants', 'own_percentage',
                         'mean_sc', 'std_sc', 'min_sc', 'p25_sc', 'p50_sc', 'p75_sc',
                         'max_sc', 'mean_conf', 'std_conf', 'min_conf', 'p25_conf', 'p50_conf',
                         'p75_conf', 'max_conf', 'skew_own', 'skew_sc', 'skew_conf',
                         'skew_row_average', 'skew_row_skew', 'minority_percentage',
                         'real_expert_number', 'P_expert_number_rT', 'P_expert_number_rF',
                         'MEAN_P_expert_rT', 'MEAN_P_expert_rF']

        q = df["q"]
        df = df.set_index('q')

#         #Target Variable
#         from sklearn.preprocessing import LabelEncoder

#         # Actual Answer (0 or 1)
#         le = LabelEncoder()
#         df['actual'] = le.transform(df['actual'])

#         from sklearn.preprocessing import OneHotEncoder
#         enc_onehot = OneHotEncoder(sparse=False, handle_unknown='ignore')

        # topic - the topic of the question
        df_topic = enc_onehot.transform(df[['topic']])
        df_topic = pd.DataFrame(df_topic)
        df_topic.columns = enc_onehot.get_feature_names()
        df = df.drop('topic', 1)

#         from sklearn.preprocessing import StandardScaler
#         s_scaler = StandardScaler()

        # Number of Participants
        for f in cont_features:
            df[f] = s_scaler.transform(df[[f]])

        df_final = df
        df_topic = df_topic.set_index(q)
        df_final = pd.concat([df, df_topic], axis=1)
#         actual_result = df_final["actual"]
#         df_final = df_final.drop("actual", axis=1)
#         df_final["actual"] = actual_result

        arr = []
        for c in df_final.columns:
            if "meta" in c:
                c = c.replace("meta", "sc")
            arr.append(c)
        df_final.columns = arr

        return df_final


















