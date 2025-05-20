# AI-Powered Loan Default Prediction: Mitigating Risk for Financial Institutions 🏦
*Leveraging Machine Learning to Proactively Identify High-Risk Loan Applicants and Enhance Lending Decisions*

---

## Project Overview

This project presents a robust machine learning solution designed to **proactively identify high-risk loan applicants** for banking institutions. By analyzing a comprehensive dataset of loan applications, the model aims to predict the likelihood of default, thereby enabling banks to make more informed and efficient lending decisions. This system serves as a crucial **first-layer assessment tool**, filtering out potential high-risk borrowers before they proceed to traditional, time-consuming, and subjective manual reviews by loan officers. The ultimate goal is to significantly **reduce loan default rates** and safeguard the financial health of the bank.

---

## Problem Statement

A significant challenge faced by many banks is a high loan default rate, which for this particular institution, stands at **12%**. Traditional loan assessment processes, relying heavily on manual reviews by loan officers, are often **time-consuming, subjective, and prone to inconsistencies**. This leads to inefficient operations and continued financial losses due to defaulted loans. There is a critical need for an automated, data-driven system that can swiftly and accurately flag high-risk applicants, thereby optimizing the lending process and minimizing financial exposure.

---

## Dataset

The dataset used for this project is sourced from [Kaggle: Loan Prediction Dataset](https://www.kaggle.com/datasets/ethicalstar/loan-prediction). It comprises **252,000 observations** across 13 features, providing a rich foundation for risk assessment.

**Key Features:**

* `Income`: Applicant's annual income.
* `Age`: Applicant's age.
* `Experience`: Years of professional experience.
* `Married/Single`: Marital status.
* `House_Ownership`: Status of house ownership.
* `Car_Ownership`: Status of car ownership.
* `Profession`: Applicant's profession.
* `CITY`: Applicant's city of residence.
* `STATE`: Applicant's state of residence.
* `CURRENT_JOB_YRS`: Years in current job.
* `CURRENT_HOUSE_YRS`: Years at current house.
* **Target Variable:** `Risk_Flag` (0 for low-risk, 1 for high-risk/default).

---

## Methodology

This project employed a supervised machine learning approach to classify loan applicants into 'low-risk' or 'high-risk' categories. A rigorous comparative analysis of multiple models was conducted to identify the most suitable algorithm for this specific business problem.

1.  **Exploratory Data Analysis (EDA):** Initial analysis was performed to understand data distributions, feature relationships, and potential insights.
2.  **Model Selection & Training:** Seven different classification models were explored:
    * Logistic Regression
    * Random Forest Classifier
    * Decision Tree Classifier
    * Extra Trees Classifier
    * XGBoost Classifier
    * LightGBM Classifier
    * **CatBoost Classifier**
    Each model underwent specific preprocessing steps tailored to its requirements.
3.  **Evaluation Strategy:** Given the critical nature of identifying all high-risk loans, **Recall** was chosen as the primary evaluation metric. Maximizing recall ensures that the model minimizes **False Negatives** (i.e., identifying truly high-risk loaners as low-risk), which is paramount to mitigating financial losses for the bank. Other metrics like Accuracy, Precision, F1-Score, and ROC AUC were also monitored for a comprehensive understanding of model performance.
4.  **Hyperparameter Tuning:** After initial comparison, the **CatBoost Classifier** demonstrated superior performance, particularly due to its effectiveness with categorical features. Extensive **GridSearchCV** was performed on CatBoost, fitting 3 folds for each of 324 candidate parameter combinations, totaling 972 fits, to achieve optimal performance.

---

## Key Findings & Results

The **CatBoost Classifier**, after thorough hyperparameter tuning, emerged as the most effective model for high-risk loan detection, achieving exceptional performance, particularly in terms of recall.

**Final CatBoost Model Performance (on Test Set):**

| Metric             | Value |
| :----------------- | :---- |
| **Recall (High-Risk)** | **0.97** |
| Accuracy (Overall) | 0.84  |
| Precision (High-Risk) | 0.43  |
| F1-Score (High-Risk) | 0.60  |
| ROC AUC Score      | 0.95  |

* **True Negatives (Low-Risk, Correctly Predicted):** 54,574
* **False Positives (Low-Risk, Incorrectly Flagged as High-Risk):** 11,755
* **False Negatives (High-Risk, Incorrectly Flagged as Low-Risk):** 281
* **True Positives (High-Risk, Correctly Predicted):** 8,990

**Insights:**

* The model's **97% recall** for high-risk loans is a critical achievement, meaning it successfully identifies almost all actual defaulters, significantly reducing the bank's exposure to bad loans.
* Despite a moderate precision, the emphasis on recall prioritizes loss prevention by minimizing oversight of risky applicants.
* **Feature Importance:** Analysis revealed that **`CITY`** and **`Profession`** were the features with the highest impact on predicting loan risk. This insight is valuable for banks to understand demographic and professional risk factors better.

---

## Project Structure

This repository is organized to ensure clarity and ease of navigation:
├── backend/                  # (Placeholder for potential future backend services or APIs)
├── data/                     # Raw and processed datasets
├── frontend/                 # (Placeholder for UI-related files, e.g., Streamlit app)
├── models/                   # Trained machine learning models (e.g., final_model.pkl)
├── notebooks/                # Jupyter Notebooks for EDA, model training, and evaluation
├── .gitattributes            # Git LFS configuration for large files
└── README.md                 # This README file

---

## Technologies Used

* **Programming Language:** Python 3.x
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn, CatBoost, XGBoost, LightGBM
* **Data Visualization:** Matplotlib, Seaborn
* **Interactive Development:** Jupyter Notebook
* **Version Control:** Git, GitHub
* **User Interface:** Streamlit (for the frontend application)

---

## How to Run This Project Locally

To set up and run this project on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    *(Remember to replace `your-username` and `your-repo-name` with your actual GitHub details.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    First, ensure you have a `requirements.txt` file in your root directory (you can generate one by running `pip freeze > requirements.txt` after installing all libraries).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Jupyter Notebooks:**
    For a detailed walkthrough of the data analysis, model training, and evaluation:
    ```bash
    jupyter notebook
    ```
    Then, navigate to the `notebooks/` directory and open the relevant `.ipynb` files.

5.  **Run the Streamlit Application (Frontend):**
    If you've built a Streamlit UI, navigate to the `frontend/` directory (or wherever your Streamlit script is) and run:
    ```bash
    streamlit run your_app_name.py # Replace 'your_app_name.py' with your Streamlit script name
    ```

---

## Future Enhancements

Looking ahead, this project can be further enhanced by:

* **Configurable Risk Threshold:** Implementing a flexible mechanism where the bank can adjust the model's **threshold for flagging high-risk loans**. This would allow banks to dynamically control their risk appetite – for instance, becoming more selective during economic downturns or relaxing criteria when pursuing growth, by tuning the balance between precision and recall.
* **Real-time Prediction API:** Developing a lightweight API (e.g., using Flask or FastAPI) to allow for real-time loan risk predictions, integrating seamlessly with existing banking systems.
* **Explainable AI (XAI):** Incorporating techniques like SHAP or LIME to provide deeper insights into why a specific loan application was flagged as high-risk, fostering trust and transparency.
* **Automated Retraining Pipeline:** Setting up an automated pipeline for periodic model retraining with new data to ensure its continued accuracy and relevance.

---

## Contact & Connect

Feel free to connect with me or reach out if you have any questions, feedback, or collaboration opportunities!

* **LinkedIn:** https://www.linkedin.com/in/ryo-tanzil/
* **Email:** carlen.averyo@gmail.com