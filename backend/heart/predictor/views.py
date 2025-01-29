from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import os
from django.shortcuts import redirect

# Load and preprocess the dataset once
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'C:/Users/Rahul Ramakrishnan/OneDrive/Rahav/MLops/MLOPS/data/Medicaldataset.csv')  # Update with correct relative path

# Preprocess dataset and train model during app startup
data = pd.read_csv(DATA_PATH).dropna()
le = LabelEncoder()
data['Result'] = le.fit_transform(data['Result'])
x = data.iloc[:, :-1]
y = data['Result']

model = DecisionTreeClassifier()
model.fit(x, y)

def home(request):
    return redirect('admin/')

class PredictView(APIView):
    def post(self, request):
        # Extract input values from request
        try:
            v1 = int(request.data.get('v1'))
            v2 = int(request.data.get('v2'))
            v3 = int(request.data.get('v3'))
            v4 = int(request.data.get('v4'))
            v5 = int(request.data.get('v5'))
            v6 = float(request.data.get('v6'))
            v7 = float(request.data.get('v7'))
            v8 = float(request.data.get('v8'))
        except (TypeError, ValueError) as e:
            print(f"Error extracting input: {e}")
            return Response({'error': 'Invalid or missing input values'}, status=status.HTTP_400_BAD_REQUEST)

        print(f"Received inputs: {v1}, {v2}, {v3}, {v4}, {v5}, {v6}, {v7}, {v8}")  # Log the inputs

        # Make predictions
        input_data = np.array([v1, v2, v3, v4, v5, v6, v7, v8]).reshape(1, -1)
        print(f"Input data shape for prediction: {input_data.shape}")  # Check input shape
        prediction = model.predict(input_data)[0]  # Get the prediction
        print(f"Prediction result: {prediction}")  # Log the prediction

        return Response({'prediction': int(prediction)}, status=status.HTTP_200_OK)
