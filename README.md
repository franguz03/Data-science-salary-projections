# Data Science Salary Projections

## Overview
This project focuses on building a salary estimation model for job positions related to data science. The process follows a structured development approach consisting of multiple phases:

1. **Data Cleaning & Feature Engineering**
2. **Exploratory Data Analysis (EDA)**
3. **Model Implementation & Optimization**
4. **Local Deployment of the Trained Model**

## Technologies Used
- **Python Version:** 3.11
- **Packages:**
- ipykernel 6.29.5
- selenium 4.29.0
- pandas 2.2.3
- matplotlib 3.10.1
- seaborn 0.13.2
- wordcloud 1.9.4
- nltk 3.9.1
- scikit-learn 1.6.1
- statsmodels 0.14.4
- flask 3.1.0
- requests 2.32.3

## Dataset
The dataset contains job listings from the United States related to data science roles. The original dataset includes the following features:

- Job Title
- Salary Estimate
- Job Description
- Rating
- Company Name
- Location
- Company Headquarters
- Company Size
- Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors

## Data Cleaning & Feature Engineering
After collecting the raw data, extensive preprocessing was conducted to ensure usability for modeling. The following steps were performed:

- Extracted numerical values from salary estimates.
- Created separate columns for employer-provided salaries and hourly wages.
- Removed entries without salary information.
- Parsed ratings from company details.
- Created a column for the company's state.
- Added a binary column indicating if the job is at the company’s headquarters.
- Transformed the founded date into the company's age.
- Created new binary features to capture key skills mentioned in job descriptions, such as:
  - Python
  - R
  - Excel
  - AWS
  - Spark
- Generated a simplified job title and seniority level.
- Added a column for job description length.

## Exploratory Data Analysis (EDA)
EDA was performed to identify relationships between categorical variables such as:
- Seniority level (Junior, Senior, etc.)
- Job location (State-wise distribution)
- Required technical skills (Python, R, AWS, etc.)
Additionally, missing values were handled appropriately to maintain data integrity.

## Model Building
To develop a robust salary prediction model, different regression techniques were explored:

1. **Baseline Model:** A logistic regression model was implemented to establish a benchmark for comparison.
2. **Advanced Models:**
   - Lasso Regression
   - Random Forest Regressor
3. **Model Optimization:**
   - Hyperparameter tuning was performed for both Lasso and Random Forest models to enhance their performance.

### Model Performance
The performance of the models was evaluated based on standard regression metrics. Below are the results:

- **Logistic Regression:** (Specify performance metric)
- **Lasso Regression:** (Specify performance metric)
- **Random Forest Regressor:** (Specify performance metric)

## Model Deployment
To make the best-performing model accessible, the following deployment strategy was implemented:

1. **Model Persistence:** The trained model was saved using `pickle` for future use.
2. **API Development:** A Flask-based API was created for local deployment.
3. **Prediction Endpoint:** A dedicated API endpoint allows users to send job-related input data and receive a salary prediction.

## Installation & Usage
### Prerequisites
Ensure you have Python installed, then install Poetry:

```sh
pip install poetry
```

### Setup
After cloning the repository, navigate to the project directory and install dependencies using Poetry:

```sh
# Clone the repository
git clone https://github.com/franguz03/Data-science-salary-projections.git

poetry install
```

### Running the API Locally
1. Navigate to the `FlaskAPI` directory:
```sh
cd data-science-projection/FlaskAPI
```
2. Start the API by running:
```sh
poetry run python wsgi.py
```
3. To make a prediction, refer to the example request provided in `request.py`.

## Future Improvements
- Implementing deep learning techniques for salary prediction.
- Deploying the model as a cloud-based API.
- Enhancing feature engineering with additional job market insights.

## Author
Franco José Guzmán Orjuela
francorjuela04@gmail.com


---


