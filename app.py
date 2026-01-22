# app.py

def interpret_score(mean_score):
    """
    Pure function to interpret the score.
    Logic based on assignment requirements:
    High: > 4
    Moderate: 2 <= mean <= 4
    Low: < 2
    """
    if mean_score > 4:
        return "High"
    elif mean_score >= 2:
        return "Moderate"
    else:
        return "Low"

def get_valid_input(question_text):
    """
    Handles user input with error checking (try/except).
    Ensures input is a number between 0 and 6.
    """
    while True:
        try:
            response = input(f"{question_text} (0-6): ")
            value = int(response)
            if 0 <= value <= 6:
                return value
            else:
                print("Error: Please enter a number between 0 and 6.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def main():
    # The list of questions as required by the assignment
    questions = [
        {"text": "At my work, I feel bursting with energy.", "dim": "Vigor"},
        {"text": "At my job, I feel strong and vigorous.", "dim": "Vigor"},
        {"text": "I am enthusiastic about my job.", "dim": "Dedication"},
        {"text": "My job inspires me.", "dim": "Dedication"},
        {"text": "When I get up in the morning, I feel like going to work.", "dim": "Vigor"},
        {"text": "I feel happy when I am working intensely.", "dim": "Absorption"},
        {"text": "I am proud of the work that I do.", "dim": "Dedication"},
        {"text": "I am immersed in my job.", "dim": "Absorption"},
        {"text": "I get carried away when I am working.", "dim": "Absorption"}
    ]

    # Simple lists to store scores for each dimension
    scores_vigor = []
    scores_dedication = []
    scores_absorption = []

    print("--- Work Engagement Scale (UWES-9) ---")
    print("Please answer: 0=Never to 6=Always.\n")

    # Loop through questions and ask for input
    for item in questions:
        score = get_valid_input(item["text"])
        
        # Add score to the correct list based on dimension
        dimension = item["dim"]
        
        if dimension == "Vigor":
            scores_vigor.append(score)
        elif dimension == "Dedication":
            scores_dedication.append(score)
        elif dimension == "Absorption":
            scores_absorption.append(score)

    print("\n--- Results ---")

    # Calculate means (averages) for each dimension
    # (Avoiding division by zero is good practice, though not strictly asked if inputs are guaranteed)
    mean_vigor = sum(scores_vigor) / len(scores_vigor)
    mean_dedication = sum(scores_dedication) / len(scores_dedication)
    mean_absorption = sum(scores_absorption) / len(scores_absorption)

    # Calculate Global Engagement (average of the 3 dimension means)
    global_mean = (mean_vigor + mean_dedication + mean_absorption) / 3

    # Display results with formatting
    print(f"Vigor: mean = {mean_vigor:.2f} -> {interpret_score(mean_vigor)}")
    print(f"Dedication: mean = {mean_dedication:.2f} -> {interpret_score(mean_dedication)}")
    print(f"Absorption: mean = {mean_absorption:.2f} -> {interpret_score(mean_absorption)}")
    print(f"Global Engagement: mean = {global_mean:.2f} -> {interpret_score(global_mean)}")

if __name__ == "__main__":
    main()
