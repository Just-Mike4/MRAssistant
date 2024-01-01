import pandas as pd

df = pd.read_csv('MRA_rec.csv')

def get_random_unique_recommendations(mood, num_recommendations=3):
    # Filter activities based on mood
    mood_data = df[df['Mood'] == mood][['Activity', 'Description']]

    # Check if there are enough unique recommendations
    if len(mood_data) < num_recommendations:
        return "Not enough unique recommendations available for this mood."

    # Randomly select unique rows
    random_rows = mood_data.sample(n=num_recommendations, replace=False)

    # Extract Activity and Description
    recommendations = random_rows[['Activity', 'Description']].values.tolist()

    return recommendations

