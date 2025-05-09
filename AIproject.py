def calculate_bmi(weight, height):
    """Calculate BMI based on weight (kg) and height (m)."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_calories(weight, height, age, gender, activity_level, goal):
    """Calculate daily calorie needs using Mifflin-St Jeor equation."""
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161

    # Adjust for activity level
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    tdee = bmr * activity_multipliers.get(activity_level.lower(), 1.2)

    # Adjust for goal
    if goal == "Weight Loss":
        return tdee - 500  # Calorie deficit
    elif goal == "Muscle Gain":
        return tdee + 500  # Calorie surplus
    else:
        return tdee  # Maintenance

def generate_diet_plan(bmi_category, goal, calories, is_vegan):
    """Generate a diet plan based on BMI, goal, calorie needs, and dietary preference."""
    if bmi_category == "Underweight" and goal == "Muscle Gain":
        if is_vegan:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "40% Carbs, 30% Protein, 30% Fats",
                "Meal Plan": {
                    "Breakfast": "Vegan protein smoothie (pea protein, almond milk, banana, chia seeds)",
                    "Snacks": "Handful of mixed nuts and dried fruits",
                    "Lunch": "Home made Dal and any vegetable with brown rice and 2 or 3 Chapati with salad",
                    "Snack": "Vegan protein bar",
                    "Dinner": "Lentil curry with brown rice and steamed broccoli and Protein Shake",
                    "Before Bed": "Almond butter on whole grain toast"
                }
            }
        else:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "40% Carbs, 30% Protein, 30% Fats",
                "Meal Plan": {
                    "Breakfast": "Oatmeal with fruits and nuts, 2 boiled eggs",
                    "Snack": "Protein shake with banana",
                    "Lunch": "Grilled chicken breast, brown rice, steamed vegetables",
                    "Snack": "Greek yogurt with honey",
                    "Dinner": "3 or 4 boiled eggs with Chicken breast and Protein Shake",
                    "Before Bed": "Cottage cheese with almonds"
                }
            }
    elif bmi_category == "Underweight" and goal == "Maintenance":
        if is_vegan:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "50% Carbs, 25% Protein, 25% Fats",
                "Meal Plan": {
                    "Breakfast": "Vegan pancakes with maple syrup and berries",
                    "Snacks": "Apple with almond butter",
                    "Lunch": "Vegan Buddha bowl (quinoa, roasted veggies, tofu, tahini dressing)",
                    "Snack": "Handful of mixed nuts",
                    "Dinner": "Vegan chili with kidney beans and brown rice",
                    "Before Bed": "Glass of almond milk"
                }
            }
        else:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "50% Carbs, 25% Protein, 25% Fats",
                "Meal Plan": {
                    "Breakfast": "Whole grain toast with avocado, scrambled eggs",
                    "Snack": "Apple with peanut butter",
                    "Lunch": "Grilled fish, sweet potato, broccoli",
                    "Snack": "Handful of mixed nuts",
                    "Dinner": "Lean beef stir-fry with brown rice",
                    "Before Bed": "Glass of milk"
                }
            }
    elif bmi_category == "Underweight" and goal == "Weight Loss":
        return {"Message": "You are already underweight. Focus on gaining weight instead."}

    elif bmi_category == "Normal" and goal == "Maintenance":
        if is_vegan:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "50% Carbs, 25% Protein, 25% Fats",
                "Meal Plan": {
                    "Breakfast": "Vegan pancakes with maple syrup and berries",
                    "Snack": "Apple with almond butter",
                    "Lunch": "Vegan Buddha bowl (quinoa, roasted veggies, tofu, tahini dressing)",
                    "Snack": "Handful of mixed nuts",
                    "Dinner": "Vegan chili with kidney beans and brown rice",
                    "Before Bed": "Glass of almond milk"
                }
            }
        else:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "50% Carbs, 25% Protein, 25% Fats",
                "Meal Plan": {
                    "Breakfast": "Whole grain toast with avocado, scrambled eggs",
                    "Snack": "Apple with peanut butter",
                    "Lunch": "Grilled fish, sweet potato, broccoli",
                    "Snack": "Handful of mixed nuts",
                    "Dinner": "Lean beef stir-fry with brown rice",
                    "Before Bed": "Glass of milk"
                }
            }
    elif bmi_category == "Normal" and goal == "Muscle Gain":
        if is_vegan:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "40% Carbs, 30% Protein, 30% Fats",
                "Meal Plan": {
                    "Breakfast": "Vegan protein smoothie (pea protein, almond milk, banana, chia seeds)",
                    "Snacks": "Handful of mixed nuts and dried fruits",
                    "Lunch": "Home made Dal and any vegetable with brown rice and 2 or 3 Chapati with salad",
                    "Snack": "Vegan protein bar",
                    "Dinner": "Lentil curry with brown rice and steamed broccoli and Protein Shake",
                    "Before Bed": "Almond butter on whole grain toast"
                }
            }
        else:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "40% Carbs, 30% Protein, 30% Fats",
                "Meal Plan": {
                    "Breakfast": "Oatmeal with fruits and nuts, 2 boiled eggs",
                    "Snack": "Protein shake with banana",
                    "Lunch": "Grilled chicken breast, brown rice, steamed vegetables",
                    "Snack": "Greek yogurt with honey",
                    "Dinner": "3 or 4 boiled eggs with Chicken breast and Protein Shake",
                    "Before Bed": "Cottage cheese with almonds"
                }
            }
    elif bmi_category == "Normal" and goal == "Weight Loss":
        return {"Message": "You are already at a normal weight. Focus on maintenance or muscle gain."}

    elif (bmi_category == "Overweight" or bmi_category == "Obese") and goal == "Weight Loss":
        if is_vegan:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "40% Protein, 30% Carbs, 30% Fats",
                "Meal Plan": {
                    "Breakfast": "Tofu scramble with spinach and whole grain toast",
                    "Snack": "Carrot sticks with hummus",
                    "Lunch": "Vegan lentil soup with a side salad",
                    "Snack": "Vegan protein bar",
                    "Dinner": "Grilled tempeh, quinoa, steamed vegetables",
                    "Before Bed": "Handful of walnuts"
                }
            }
        else:
            return {
                "Calories": f"{calories:.0f} kcal/day",
                "Macronutrient Split": "40% Protein, 30% Carbs, 30% Fats",
                "Meal Plan": {
                    "Breakfast": "Vegetable omelette, whole grain toast",
                    "Snack": "Carrot sticks with hummus",
                    "Lunch": "Grilled chicken salad with olive oil dressing",
                    "Snack": "Protein bar",
                    "Dinner": "Grilled turkey, quinoa, steamed vegetables",
                    "Before Bed": "Handful of walnuts"
                }
            }
    elif (bmi_category == "Overweight" or bmi_category == "Obese") and goal == "Muscle Gain":
        return {"Message": "First lose some fat. Muscles will form in the process."}

    return {"Message": "No plan found for your inputs. Please check your details."}

def generate_workout_plan(bmi_category, goal):
    """Generate a 6-day workout plan based on BMI and goal."""
    if bmi_category == "Underweight" and goal == "Muscle Gain":
        return {
            "Day 1": "Chest & Triceps: Bench Press, Incline Dumbbell Press, Chest Flys, Tricep Dips, Tricep Pushdowns",
            "Day 2": "Back & Biceps: Deadlifts, Pull-Ups, Bent-Over Rows, Barbell Curls, Hammer Curls",
            "Day 3": "Legs & Core: Squats, Lunges, Leg Press, Calf Raises, Planks, Russian Twists",
            "Day 4": "Chest & Triceps: Bench Press, Incline Dumbbell Press, Chest Flys, Tricep Dips, Tricep Pushdowns",
            "Day 5": "Back & Biceps: Deadlifts, Pull-Ups, Bent-Over Rows, Barbell Curls, Hammer Curls",
            "Day 6": "Legs & Core: Squats, Lunges, Leg Press, Calf Raises, Planks, Russian Twists",
            "Day 7": "Rest"
        }
    elif bmi_category == "Underweight" and goal == "Maintenance":
        return {
            "Day 1": "Full Body + Cardio: Squats, Push-Ups, Bent-Over Rows, Planks, 20-min Cardio",
            "Day 2": "Cardio & Core: 30-min Cardio, Russian Twists, Leg Raises, Mountain Climbers",
            "Day 3": "Full Body + Cardio: Deadlifts, Bench Press, Lunges, Planks, 20-min Cardio",
            "Day 4": "Cardio & Core: 30-min Cardio, Russian Twists, Leg Raises, Mountain Climbers",
            "Day 5": "Full Body + Cardio: Squats, Push-Ups, Bent-Over Rows, Planks, 20-min Cardio",
            "Day 6": "Cardio & Core: 30-min Cardio, Russian Twists, Leg Raises, Mountain Climbers",
            "Day 7": "Rest"
        }
    elif bmi_category == "Underweight" and goal == "Weight Loss":
        return {"Message": "You are already underweight. Focus on gaining weight instead."}

    elif bmi_category == "Normal" and goal == "Maintenance":
        return {
            "Day 1": "Upper Body: Bench Press, Dumbbell Rows, Shoulder Press, Bicep Curls, Tricep Extensions",
            "Day 2": "Lower Body: Squats, Deadlifts, Leg Press, Calf Raises, Lunges",
            "Day 3": "Cardio & Core: Running/Cycling, Planks, Russian Twists, Leg Raises",
            "Day 4": "Upper Body: Bench Press, Dumbbell Rows, Shoulder Press, Bicep Curls, Tricep Extensions",
            "Day 5": "Lower Body: Squats, Deadlifts, Leg Press, Calf Raises, Lunges",
            "Day 6": "Cardio & Core: Running/Cycling, Planks, Russian Twists, Leg Raises",
            "Day 7": "Rest"
        }
    elif bmi_category == "Normal" and goal == "Muscle Gain":
        return {
            "Day 1": "Chest & Triceps: Bench Press, Incline Dumbbell Press, Chest Flys, Tricep Dips, Tricep Pushdowns",
            "Day 2": "Back & Biceps: Deadlifts, Pull-Ups, Bent-Over Rows, Barbell Curls, Hammer Curls",
            "Day 3": "Legs & Core: Squats, Lunges, Leg Press, Calf Raises, Planks, Russian Twists",
            "Day 4": "Chest & Triceps: Bench Press, Incline Dumbbell Press, Chest Flys, Tricep Dips, Tricep Pushdowns",
            "Day 5": "Back & Biceps: Deadlifts, Pull-Ups, Bent-Over Rows, Barbell Curls, Hammer Curls",
            "Day 6": "Legs & Core: Squats, Lunges, Leg Press, Calf Raises, Planks, Russian Twists",
            "Day 7": "Rest"
        }
    elif bmi_category == "Normal" and goal == "Weight Loss":
        return {"Message": "You are already at a normal weight. Focus on maintenance or muscle gain."}

    elif (bmi_category == "Overweight" or bmi_category == "Obese") and goal == "Weight Loss":
        return {
            "Day 1": "Full Body + Cardio: Squats, Push-Ups, Bent-Over Rows, Planks, 20-min Cardio",
            "Day 2": "Cardio & Core: 30-min Cardio, Russian Twists, Leg Raises, Mountain Climbers",
            "Day 3": "Full Body + Cardio: Deadlifts, Bench Press, Lunges, Planks, 20-min Cardio",
            "Day 4": "Cardio & Core: 30-min Cardio, Russian Twists, Leg Raises, Mountain Climbers",
            "Day 5": "Full Body + Cardio: Squats, Push-Ups, Bent-Over Rows, Planks, 20-min Cardio",
            "Day 6": "Cardio & Core: 30-min Cardio, Russian Twists, Leg Raises, Mountain Climbers",
            "Day 7": "Rest"
        }
    elif (bmi_category == "Overweight" or bmi_category == "Obese") and goal == "Muscle Gain":
        return {"Message": "First lose some fat. Muscles will form in the process."}

    return {"Message": "No plan found for your inputs. Please check your details."}

def main():
    """Main function to interact with the user."""
    print("Welcome to the Workout & Diet Planner Chatbot!")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ").strip().title()
    activity_level = input("Enter your activity level (Sedentary/Lightly Active/Moderately Active/Very Active/Extra Active): ").strip().title()
    goal = input("Enter your goal (Muscle Gain/Maintenance/Weight Loss): ").strip().title()
    is_vegan = input("Are you vegan? (Yes/No): ").strip().lower() == "yes"

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi)
    print(f"\nYour BMI is {bmi:.2f}, which is classified as {bmi_category}.")

    # Calculate calories
    calories = calculate_calories(weight, height, age, gender, activity_level, goal)
    print(f"Your daily calorie target is {calories:.0f} kcal.")

    # Generate diet plan
    diet_plan = generate_diet_plan(bmi_category, goal, calories, is_vegan)
    if diet_plan:
        print("\nHere's your diet plan:")
        for key, value in diet_plan.items():
            print(f"{key}: {value}")

    # Generate workout plan
    workout_plan = generate_workout_plan(bmi_category, goal)
    if workout_plan:
        print("\nHere's your 6-day workout plan:")
        for day, exercises in workout_plan.items():
            print(f"{day}: {exercises}")
    else:
        print("No plan found for your inputs. Please check your details.")

if __name__ == "__main__":
    main()