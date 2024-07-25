import requests

# Replace these with your own Edamam API credentials
app_id = '739072ba'
app_key = '519b50ccceb80a225a2c5cb1668030d5'

def get_nutrition_data(ingredient):
    url = 'https://api.edamam.com/api/nutrition-data'
    params = {
        'app_id': app_id,
        'app_key': app_key,
        'nutrition-type': "logging",
        'ingr': ingredient
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_macros(nutrition_data):
    if 'totalNutrients' in nutrition_data:
        nutrients = nutrition_data['totalNutrients']
        print
        print(f"Calories: {nutrients.get('ENERC_KCAL', {}).get('quantity', 0)} kcal")
        print(f"Protein: {nutrients.get('PROCNT', {}).get('quantity', 0)} g")
        print(f"Fat: {nutrients.get('FAT', {}).get('quantity', 0)} g")
        print(f"Carbohydrates: {nutrients.get('CHOCDF', {}).get('quantity', 0)} g")
    else:
        print("No nutritional data found.")

def main():
    while True:
        ingredient = input("Enter an ingredient (or 'exit' to quit): ")
        if ingredient.lower() == 'exit':
            break
        nutrition_data = get_nutrition_data(ingredient)
        if nutrition_data:
            display_macros(nutrition_data)
        else:
            print("Error retrieving data. Please try again.")

if __name__ == "__main__":
    main()
