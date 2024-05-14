{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "586b043b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, jsonify\n",
    "import joblib\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "# Load the trained XGBoost model\n",
    "model = joblib.load(\"Lethal_model.pkl\")\n",
    "# Function to get class description based on predicted class\n",
    "def get_class_description(predicted_class):\n",
    "    class_mapping = {\n",
    "        0: \"unknown (alive)\",\n",
    "        1: \"cardiogenic shock\",\n",
    "        2: \"pulmonary edema\",\n",
    "        3: \"myocardial rupture\",\n",
    "        4: \"progress of congestive heart failure\",\n",
    "        5: \"thromboembolism\",\n",
    "        6: \"asystole\",\n",
    "        7: \"ventricular fibrillation\"\n",
    "    }\n",
    "    return class_mapping.get(predicted_class, \"Unknown\")\n",
    "\n",
    "# Function to preprocess input data\n",
    "def preprocess_input(data):\n",
    "    scaler = StandardScaler()\n",
    "    scaled_data = scaler.fit_transform(data)\n",
    "    return scaled_data\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    if request.method == 'POST':\n",
    "        user_input = request.json\n",
    "        \n",
    "        # Convert input to DataFrame\n",
    "        user_input_df = pd.DataFrame(user_input)\n",
    "        \n",
    "        # Standardize the input data\n",
    "        input_df_scaled = preprocess_input(user_input_df)\n",
    "        \n",
    "        # Make prediction\n",
    "        prediction = model.predict(input_df_scaled)\n",
    "        \n",
    "        # Get predicted class description\n",
    "        predicted_class = get_class_description(prediction[0])\n",
    "        \n",
    "        return jsonify({\"prediction\": predicted_class})\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
