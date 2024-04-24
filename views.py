from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

class PredictView(APIView):
    def post(self, request):
        # Extract input values from request
        v1 = request.data.get('v1')
        v2 = request.data.get('v2')
        v3 = request.data.get('v3')
        v4 = request.data.get('v4')
        v5 = request.data.get('v5')
        v6 = request.data.get('v6')
        v7 = request.data.get('v7')
        v8 = request.data.get('v8')
        
        # Check if any value is None
        if None in [v1, v2, v3, v4, v5]:
            return Response({'error': 'One or more values are missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert values to float
        try:
            v1 = int(v1)
            v2 = int(v2)
            v3 = int(v3)
            v4 = int(v4)
            v5 = int(v5)
            v6 = float(v6)
            v7 = float(v7)
            v8 = float(v8)
        except ValueError:
            return Response({'error': 'One or more values are not valid numbers'}, status=status.HTTP_400_BAD_REQUEST)

        # Load the trained model and preprocess data
        data = pd.read_csv('C:/Users/Rahav Ramkr/mlops2/backend/Medicaldataset.csv')  # Update with your file path
        data = data.dropna()
        le = LabelEncoder()
        data['Result']=le.fit_transform(data['Result'])
        x=data.iloc[:,:-1]
        y=data['Result']
        
        # Train the model
        rg =DecisionTreeClassifier()
        rg.fit(x, y)

        # Make predictions
        out = rg.predict(np.array([v1, v2, v3, v4, v5,v6,v7,v8]).reshape(1, -1))
        prediction = int(out[0])

        # Return the prediction
        return Response({'prediction': prediction}, status=status.HTTP_200_OK)