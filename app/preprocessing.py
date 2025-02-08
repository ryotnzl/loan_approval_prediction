import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load encoders and scalers
mm_scaler = MinMaxScaler()

# Job Group Mapping
job_groups = {
    'Engineering': ['Mechanical_engineer', 'Civil_engineer', 'Chemical_engineer', 'Design_Engineer',
                    'Computer_hardware_engineer', 'Petroleum_Engineer', 'Industrial_Engineer', 'Engineer'],
    'IT/Software': ['Software_Developer', 'Web_designer', 'Computer_operator', 'Technology_specialist'],
    'Creative': ['Graphic_Designer', 'Technical_writer', 'Fashion_Designer', 'Artist', 'Designer'],
    'Healthcare': ['Physician', 'Dentist', 'Surgeon', 'Psychologist', 'Biomedical_Engineer'],
    'Management': ['Hotel_Manager', 'Consultant', 'Architect', 'Official', 'Chef', 'Analyst'],
    'Legal/Government': ['Politician', 'Magistrate', 'Lawyer', 'Civil_servant', 'Police_officer', 'Firefighter', 'Army_officer'],
    'Financial': ['Financial_Analyst', 'Chartered_Accountant', 'Economist'],
    'Science/Research': ['Scientist', 'Geologist', 'Microbiologist', 'Statistician', 'Technician'],
    'Aviation': ['Flight_attendant', 'Air_traffic_controller', 'Aviator'],
    'Miscellaneous': ['Librarian', 'Secretary', 'Drafter', 'Comedian', 'Surveyor']
}

# Define function for feature engineering
def preprocess_input(data):
    df = pd.DataFrame([data])  # Convert input dictionary to DataFrame

    # Label encoding
    df['Married/Single'] = df['Married/Single'].map({'married': 1, 'single': 0})
    df['Car_Ownership'] = df['Car_Ownership'].map({'yes': 1, 'no': 0})
    df['House_Ownership'] = df['House_Ownership'].map({'norent_noown': 0, 'rented': 1, 'owned': 2})

    # Job Group Encoding
    df['job_groups'] = df['Profession'].map({job: group for group, jobs in job_groups.items() for job in jobs})

    # Feature Scaling
    df[['Experience_Norm', 'CURRENT_JOB_YRS_Norm']] = mm_scaler.fit_transform(df[['Experience', 'CURRENT_JOB_YRS']])

    # Create Career Maturity Index (CMI)
    alpha, beta = 0.8, 0.2
    df['CMI'] = alpha * df['Experience_Norm'] + beta * df['CURRENT_JOB_YRS_Norm']

    # Scale numeric features
    scale_features = ['Income', 'Age', 'CURRENT_HOUSE_YRS']
    df[scale_features] = mm_scaler.fit_transform(df[scale_features])

    # Select required columns (matching model input)
    model_features = ['Married/Single', 'Car_Ownership', 'House_Ownership', 'CMI', 'Income', 'Age', 'CURRENT_HOUSE_YRS']
    
    return df[model_features].values  # Convert to NumPy array for model

