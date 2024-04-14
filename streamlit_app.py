import streamlit as st
import pickle

# Load the pre-trained model
with open('model2.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title
st.title('Health Prediction App')

# Form for user input
st.subheader('Enter Health Parameters')

# Define a dictionary to store form data
formData = {}

# Define questions and corresponding keys in the desired sequence
questions = {
    'Age (yrs)': 'Age',
    'Weight (Kg)': 'Weight',
    'Height(Cm)': 'Height',
    'Pulse rate(bpm)': 'PulseRate',
    'RR (breaths/min)': 'RR',
    'Pregnant(Y/N)': 'Pregnant',
    'No. of aborptions': 'Abortions',
    'FSH(mIU/mL)': 'FSH',
    'TSH (mIU/L)': 'TSH',
    'LH(mIU/mL)': 'LSH',
    'AMH(ng/mL)': 'AMH',
    'PRL(ng/mL)': 'PRL',
    'Vit D3 (ng/mL)': 'VitD3',
    'PRG(ng/mL)': 'PRG',
    'RBS(mg/dl)': 'RBS',
    'Weight gain(Y/N)': 'Weight_gain',
    'hair growth(Y/N)': 'hair_growth',
    'Skin darkening (Y/N)': 'Skin_darkening',
    'Hair loss(Y/N)': 'Hair_loss',
    'FSH/LH': 'FSH_LH_ratio',
    'Pimples(Y/N)': 'Pimples',
    'Fast food (Y/N)': 'Fast_food',
    'Reg.Exercise(Y/N)': 'Reg_exercise',
    'BP _Systolic (mmHg)': 'BP_systolic',
    'BP _Diastolic (mmHg)': 'BP_diastolic',
    'Waist:Hip Ratio': 'W_H_ratio'
}

# Loop through questions and gather responses
for question, key in questions.items():
    formData[key] = st.number_input(question)

# Fill missing features with 0
missing_features = set(model.feature_importances_)
for key in formData.keys():
    if key not in missing_features:
        formData[key] = 0

# Predict function
def predict(formData):
    # Perform prediction using the loaded model
    # Example: prediction = model.predict([[input_param1, input_param2]])
    # Currently, formData is a dictionary. You need to convert it into a format that your model expects.
    # Additionally, you need to handle data preprocessing such as converting strings to numbers.
    prediction = model.predict([list(formData.values())])  # Assuming model expects a list of values
    return prediction

# Make prediction
if st.button('Predict'):
    result = predict(formData)
    st.success(f'The prediction is {result[0]}')
