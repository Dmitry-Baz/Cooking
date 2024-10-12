def load_recipes(filename):
    recipes = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1
            ingredients_count = int(lines[i].strip())
            i += 1
            
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_line = lines[i].strip()
                ingredients.append(ingredient_line)
                i += 1
            
            recipes[dish_name] = ingredients
            
    return recipes

def display_recipes(recipes):
    for dish_name, ingredients in recipes.items():
        print(f"Название блюда: {dish_name}")
        print("Ингредиенты:")
        for ingredient in ingredients:
            print(f" - {ingredient}")
        print()

def add_recipe(filename):
    dish_name = input("Введите название блюда: ")
    ingredients_count = int(input("Введите количество ингредиентов: "))
    
    ingredients = []
    for _ in range(ingredients_count):
        ingredient = input("Введите ингредиент (Название | Количество | Единица измерения): ")
        ingredients.append(ingredient)
        
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{dish_name}\n{ingredients_count}\n")
        for ingredient in ingredients:
            file.write(f"{ingredient}\n")
        file.write("\n")

def main():
    filename = 'recipes.txt'
    
    while True:
        print("1. Показать рецепты")
        print("2. Добавить рецепт")
        print("3. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            recipes = load_recipes(filename)
            display_recipes(recipes)
        elif choice == '2':
            add_recipe(filename)
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()