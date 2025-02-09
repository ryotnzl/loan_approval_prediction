import re
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

# Load pre-trained scaler
SCALER_PATH = "models/scaler.pkl"
try:
    df_scaler = joblib.load(SCALER_PATH)
except FileNotFoundError:
    df_scaler = MinMaxScaler()

# Function to clean city names
def clean_city_name(city: str) -> str:
    return re.sub(r'\[\d+\]', '', city).strip()

# Define city tiers
tier_1_cities = {"Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune"}
tier_2_cities = {"Agra", "Amritsar", "Aurangabad", "Bhopal", "Coimbatore", "Indore", "Jaipur", "Kanpur", "Lucknow", "Nagpur", "Patna", "Surat", "Vadodara", "Visakhapatnam"}

def assign_community(city: str) -> int:
    if city in tier_1_cities:
        return 2
    elif city in tier_2_cities:
        return 1
    return 0

# Job encoding mapping
job_encoding_mapping = {
    'Engineering': 0.12,
    'IT/Software': 0.15,
    'Creative': 0.08,
    'Healthcare': 0.20,
    'Management': 0.14,
    'Legal/Government': 0.18,
    'Financial': 0.17,
    'Science/Research': 0.10,
    'Aviation': 0.09,
    'Miscellaneous': 0.05
}

job_groups = {
    'Engineering': {"Mechanical_engineer", "Civil_engineer", "Chemical_engineer", "Design_Engineer", "Computer_hardware_engineer", "Petroleum_Engineer", "Industrial_Engineer", "Engineer"},
    'IT/Software': {"Software_Developer", "Web_designer", "Computer_operator", "Technology_specialist"},
    'Creative': {"Graphic_Designer", "Technical_writer", "Fashion_Designer", "Artist", "Designer"},
    'Healthcare': {"Physician", "Dentist", "Surgeon", "Psychologist", "Biomedical_Engineer"},
    'Management': {"Hotel_Manager", "Consultant", "Architect", "Official", "Chef", "Analyst"},
    'Legal/Government': {"Politician", "Magistrate", "Lawyer", "Civil_servant", "Police_officer", "Firefighter", "Army_officer"},
    'Financial': {"Financial_Analyst", "Chartered_Accountant", "Economist"},
    'Science/Research': {"Scientist", "Geologist", "Microbiologist", "Statistician", "Technician"},
    'Aviation': {"Flight_attendant", "Air_traffic_controller", "Aviator"},
    'Miscellaneous': {"Librarian", "Secretary", "Drafter", "Comedian", "Surveyor"}
}

def map_job_group(profession: str) -> str:
    for group, jobs in job_groups.items():
        if profession in jobs:
            return group
    return 'Miscellaneous'

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses input dataframe before model inference."""
    df = df.copy()
    
    # Clean city names
    df['CITY'] = df['CITY'].apply(clean_city_name)
    
    # Assign community type
    df['community_type'] = df['CITY'].apply(assign_community)
    
    # Encode categorical features
    df['Married/Single'] = df['Married/Single'].map({'married': 1, 'single': 0}).fillna(0)
    df['House_Ownership'] = df['House_Ownership'].map({'norent_noown': 0, 'rented': 1, 'owned': 2}).fillna(0)
    df['Car_Ownership'] = df['Car_Ownership'].map({'yes': 1, 'no': 0}).fillna(0)
    
    # Normalize experience and job years
    if {'Experience', 'CURRENT_JOB_YRS'}.issubset(df.columns):
        df[['Experience_Norm', 'CURRENT_JOB_YRS_Norm']] = df_scaler.transform(df[['Experience', 'CURRENT_JOB_YRS']])
        df['CMI'] = 0.8 * df['Experience_Norm'] + 0.2 * df['CURRENT_JOB_YRS_Norm']
    
    # Encode profession
    df['job_groups'] = df['Profession'].apply(map_job_group)
    df['job_encoded'] = df['job_groups'].map(job_encoding_mapping).fillna(0)
    
    # Scale numerical features
    num_features = ['Income', 'Age', 'CURRENT_HOUSE_YRS', 'community_type', 'House_Ownership']
    if set(num_features).issubset(df.columns):
        df[num_features] = df_scaler.transform(df[num_features])
    
    return df