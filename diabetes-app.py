#importing libraries
#import catboost
import xgboost as xgb
import pandas as pd
import streamlit as st
import base64
 
#importing model
model = xgb.XGBRegressor()
model.load_model('large_xgb_model.json')

#setting background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:images/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/bg2.jpg')

#main body
def main():
    st.title('Employee Attrition Prediction')
    st.image('images/bg4.png')
    st.subheader('(Please fill in the Employee details accordingly)')

    Age = st.number_input('Age')
    BusinessTravel = st.number_input('BusinessTravel')
    DailyRate = st.number_input('DailyRate')
    Department = st.number_input('Department')     
    DistanceFromHome = st.number_input('DistanceFromHome')
    Education = st.number_input('Education')
    EducationField  = st.number_input('EducationField')
    EmployeeCount = st.number_input('EmployeeCount')
    EmployeeNumber = st.number_input('EmployeeNumber')
    EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction')
    Gender = st.number_input('Gender')
    HourlyRate = st.number_input('HourlyRate')
    JobInvolvement = st.number_input('JobInvolvement')
    JobLevel = st.number_input('JobLevel')
    JobRole = st.number_input('JobRole')
    JobSatisfaction   = st.number_input('JobSatisfaction')
    MaritalStatus = st.number_input('MaritalStatus')
    MonthlyIncome = st.number_input('MonthlyIncome')
    MonthlyRate = st.number_input('MonthlyRate')
    NumCompaniesWorked = st.number_input('NumCompaniesWorked')
    Over18 = st.number_input('Over18')
    OverTime = st.number_input('OverTime')
    PercentSalaryHike = st.number_input('PercentSalaryHike')
    PerformanceRating = st.number_input('PerformanceRating')
    RelationshipSatisfaction = st.number_input('RelationshipSatisfaction')
    StandardHours = st.number_input('StandardHours')
    StockOptionLevel = st.number_input('StockOptionLevel')
    TotalWorkingYears = st.number_input('TotalWorkingYears')
    TrainingTimesLastYear = st.number_input('TrainingTimesLastYear')
    WorkLifeBalance = st.number_input('WorkLifeBalance')
    YearsAtCompany = st.number_input('YearsAtCompany')
    YearsInCurrentRole = st.number_input('YearsInCurrentRole')
    YearsSinceLastPromotion  = st.number_input('YearsSinceLastPromotion')
    YearsWithCurrManager = st.number_input('YearsWithCurrManager')


    
    if st.button('Click to Predict'):
        result = model.predict([[Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager]])
        
        if result > 0 :
            st.success(result)
            st.success('Employee Does not seem to attrite')
        else:
            st.warning(result)
            st.warning('Employee tends to attrite')
            

if __name__=='__main__':
    main()
