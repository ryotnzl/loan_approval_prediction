import streamlit as st
import requests

# FastAPI URL (ensure FastAPI backend is running)
API_URL = "http://127.0.0.1:8000/predict/"

# Title
st.title("Loan Risk Prediction App")

# Collect user inputs
Income = st.number_input("Income", min_value=0, step=1000)
Age = st.number_input("Age", min_value=18, max_value=100, step=1)
Experience = st.number_input("Work Experience (Years)", min_value=0, step=1)
CURRENT_JOB_YRS = st.number_input("Years in Current Job", min_value=0, step=1)
CURRENT_HOUSE_YRS = st.number_input("Years in Current House", min_value=0, step=1)

Married_Single = st.selectbox("Marital Status", ["married", "single"])
House_Ownership = st.selectbox("House Ownership", ["owned", "rented", "norent_noown"])
Car_Ownership = st.selectbox("Car Ownership", ["yes", "no"])
Profession = st.text_input("Profession")
CITY = st.text_input("City",['Rewa', 'Parbhani', 'Alappuzha', 'Bhubaneswar', 'Tiruchirappalli', 'Jalgaon',
                             'Tiruppur', 'Jamnagar', 'Kota', 'Karimnagar', 'Hajipur', 'Adoni', 'Erode',
                             'Kollam', 'Madurai', 'Anantapuram', 'Kamarhati', 'Bhusawal', 'Sirsa',
                             'Amaravati', 'Secunderabad', 'Ahmedabad', 'Ajmer', 'Ongole', 'Miryalaguda',
                             'Ambattur', 'Indore', 'Pondicherry', 'Shimoga', 'Chennai', 'Gulbarga',
                             'Khammam', 'Saharanpur', 'Gopalpur', 'Amravati', 'Udupi', 'Howrah',
                             'Aurangabad', 'Hospet', 'Shimla', 'Khandwa', 'Bidhannagar', 'Bellary',
                             'Danapur', 'Purnia', 'Bijapur', 'Patiala', 'Malda', 'Sagar', 'Durgapur',
                             'Junagadh', 'Singrauli', 'Agartala', 'Thanjavur', 'Hindupur', 'Naihati',
                             'North_Dumdum', 'Panchkula', 'Anantapur', 'Serampore', 'Bathinda', 'Nadiad',
                             'Kanpur', 'Haridwar', 'Berhampur', 'Jamshedpur', 'Hyderabad', 'Bidar',
                             'Kottayam', 'Solapur', 'Suryapet', 'Aizawl', 'Asansol', 'Deoghar', 'Eluru',
                             'Ulhasnagar', 'Aligarh', 'South_Dumdum', 'Berhampore', 'Gandhinagar',
                             'Sonipat', 'Muzaffarpur', 'Raichur', 'Rajpur_Sonarpur', 'Ambarnath', 'Katihar',
                             'Kozhikode', 'Vellore', 'Malegaon', 'Kochi', 'Nagaon', 'Nagpur', 'Srinagar',
                             'Davanagere', 'Bhagalpur', 'Siwan', 'Meerut', 'Dindigul', 'Bhatpara',
                             'Ghaziabad', 'Kulti', 'Chapra', 'Dibrugarh', 'Panihati', 'Bhiwandi', 'Morbi',
                             'Kalyan-Dombivli', 'Gorakhpur', 'Panvel', 'Siliguri', 'Bongaigaon', 'Patna',
                             'Ramgarh', 'Ozhukarai', 'Mirzapur', 'Akola', 'Satna', 'Motihari', 'Jalna',
                             'Jalandhar', 'Unnao', 'Karnal', 'Cuttack', 'Proddatur', 'Ichalkaranji',
                             'Warangal', 'Jhansi', 'Bulandshahr', 'Narasaraopet', 'Chinsurah', 'Jehanabad',
                             'Dhanbad', 'Gudivada', 'Gandhidham', 'Raiganj', 'Kishanganj', 'Varanasi',
                             'Belgaum', 'Tirupati', 'Tumkur', 'Coimbatore', 'Kurnool', 'Gurgaon',
                             'Muzaffarnagar', 'Bhavnagar', 'Arrah', 'Munger', 'Tirunelveli', 'Mumbai',
                             'Mango', 'Nashik', 'Kadapa', 'Amritsar', 'Khora,_Ghaziabad', 'Ambala', 'Agra',
                             'Ratlam', 'Surendranagar_Dudhrej', 'Delhi_city', 'Bhopal', 'Hapur', 'Rohtak',
                             'Durg', 'Korba', 'Bangalore', 'Shivpuri', 'Thrissur', 'Vijayanagaram',
                             'Farrukhabad', 'Nangloi_Jat', 'Madanapalle', 'Thoothukudi', 'Nagercoil',
                             'Gaya', 'Chandigarh_city', 'Jammu', 'Kakinada', 'Dewas',
                             'Bhalswa_Jahangir_Pur', 'Baranagar', 'Firozabad', 'Phusro', 'Allahabad',
                             'Guna', 'Thane', 'Etawah', 'Vasai-Virar', 'Pallavaram', 'Morena', 'Ballia',
                             'Surat', 'Burhanpur', 'Phagwara', 'Mau', 'Mangalore', 'Alwar', 'Mahbubnagar',
                             'Maheshtala', 'Hazaribagh', 'Bihar_Sharif', 'Faridabad', 'Lucknow', 'Tenali',
                             'Barasat', 'Amroha', 'Giridih', 'Begusarai', 'Medininagar', 'Rajahmundry',
                             'Saharsa', 'New_Delhi', 'Bhilai', 'Moradabad', 'Machilipatnam',
                             'Mira-Bhayandar', 'Pali', 'Navi_Mumbai', 'Mehsana', 'Imphal', 'Kolkata',
                             'Sambalpur', 'Ujjain', 'Madhyamgram', 'Jabalpur', 'Jamalpur', 'Ludhiana',
                             'Bareilly', 'Gangtok', 'Anand', 'Dehradun', 'Pune', 'Satara', 'Srikakulam',
                             'Raipur', 'Jodhpur', 'Darbhanga', 'Nizamabad', 'Nandyal', 'Dehri', 'Jorhat',
                             'Ranchi', 'Kumbakonam', 'Guntakal', 'Haldia', 'Loni', 'Pimpri-Chinchwad',
                             'Rajkot', 'Nanded', 'Noida', 'Kirari_Suleman_Nagar', 'Jaunpur', 'Bilaspur',
                             'Sambhal', 'Dhule', 'Rourkela', 'Thiruvananthapuram', 'Dharmavaram', 'Nellore',
                             'Visakhapatnam', 'Karawal_Nagar', 'Jaipur', 'Avadi', 'Bhimavaram', 'Bardhaman',
                             'Silchar', 'Buxar', 'Kavali', 'Tezpur', 'Ramagundam', 'Yamunanagar',
                             'Sri_Ganganagar', 'Sasaram', 'Sikar', 'Bally', 'Bhiwani', 'Rampur', 'Uluberia',
                             'Sangli-Miraj_&_Kupwad', 'Hosur', 'Bikaner', 'Shahjahanpur',
                             'Sultan_Pur_Majra', 'Vijayawada', 'Bharatpur', 'Tadepalligudem', 'Tinsukia',
                             'Salem', 'Mathura', 'Guntur', 'Hubliâ€“Dharwad', 'Guwahati', 'Chittoor',
                             'Tiruvottiyur', 'Vadodara', 'Ahmednagar', 'Fatehpur', 'Bhilwara', 'Kharagpur',
                             'Bettiah', 'Bhind', 'Bokaro', 'Karaikudi', 'Raebareli', 'Pudukkottai',
                             'Udaipur', 'Mysore', 'Panipat', 'Latur', 'Tadipatri', 'Bahraich', 'Orai',
                             'Raurkela_Industrial_Township', 'Gwalior', 'Katni', 'Chandrapur', 'Kolhapur']

                     )
STATE = st.text_input("State",['Madhya_Pradesh', 'Maharashtra', 'Kerala', 'Odisha', 'Tamil_Nadu', 'Gujarat',
                               'Rajasthan', 'Telangana', 'Bihar', 'Andhra_Pradesh', 'West_Bengal', 'Haryana',
                               'Puducherry', 'Karnataka', 'Uttar_Pradesh', 'Himachal_Pradesh', 'Punjab',
                               'Tripura', 'Uttarakhand', 'Jharkhand', 'Mizoram', 'Assam', 'Jammu_and_Kashmir',
                               'Delhi', 'Chhattisgarh', 'Chandigarh', 'Manipur', 'Sikkim']
                      )

# Submit button
if st.button("Predict Loan Risk"):
    # Create input dictionary
    input_data = {
        "Income": Income,
        "Age": Age,
        "Experience": Experience,
        "Married_Single": Married_Single,
        "House_Ownership": House_Ownership,
        "Car_Ownership": Car_Ownership,
        "Profession": Profession,
        "CITY": CITY,
        "STATE": STATE,
        "CURRENT_JOB_YRS": CURRENT_JOB_YRS,
        "CURRENT_HOUSE_YRS": CURRENT_HOUSE_YRS
    }

    # Make prediction request
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Loan Risk Prediction: {result['risk_flag']} (Probability: {result['probability']:.2f})")
    else:
        st.error("Error making prediction")
