[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22246621)
# Work Engagement Scale – End-of-Semester Lab Test (Introduction to Programming)

This repository contains the program structure (and associated tests) required for the end-of-semester lab assignment.  
Use **`app.py`** for the application code and **`tests.py`** for the test suite. You may add additional files if necessary.

---

## 📌 Assignment Overview

Create a Python program that:

- Administers a quiz using the **Utrecht Work Engagement Scale – Short Version (UWES-9)**.
- Computes **mean scores** for each dimension:
  - **Vigor**
  - **Dedication**
  - **Absorption**
- Interprets engagement levels as **Low**, **Moderate**, or **High**, based on the computed means.
- Handles invalid user inputs gracefully using exceptions.
- Includes at least one **unit test** for a calculation or interpretation function (e.g., score interpretation).

---

## 🧩 Functional Requirements

### Quiz Structure
- The quiz consists of **9 questions**, covering:
  - **Vigor**
  - **Dedication**
  - **Absorption**
- Each question uses a **0–6 Likert scale**:
  - `0 = Never`
  - `1 = Almost never`
  - `2 = Rarely`
  - `3 = Sometimes`
  - `4 = Often`
  - `5 = Very often`
  - `6 = Always`

---

### Scoring
- Each response contributes to one of the three UWES dimensions.
- For each dimension:
  - Compute the **mean score** of its associated items.
- Compute a **global engagement score** as the mean of all three dimension means.

---

### Interpretation
Interpretation depends on the **mean score**:

| Mean Score               | Interpretation |
|--------------------------|----------------|
| **mean > 4**                  | High           |
| **2 ≤ mean ≤ 4**         | Moderate       |
| **mean < 2**                  | Low            |

The interpretation must be implemented as a **pure function**, which will be **unit tested**.

---

### Output Requirements
The program must:

- Display the **mean score** for each dimension.
- Show the **interpretation** (High / Moderate / Low) for each dimension.
- Display the **global engagement mean score**.

---

## ✔️ Input Validation

Handle invalid inputs by:

- Re-prompting the user if the input is **non-numeric**.
- Showing an error message and retrying if the input is **outside 0–6**.
- Using `try/except` to avoid program crashes.

---

## 🗂️ Data Structure

You may store questions in a **list of dictionaries**, or use another suitable collection type.

Each dictionary should contain:

- `text`: The question text  
- `dimension`: The UWES dimension it belongs to  

**Example:**

```python
questions = [
    {"text": "At my work, I feel bursting with energy.", "dimension": "Vigor"},
    {"text": "At my job, I feel strong and vigorous.", "dimension": "Vigor"},
    {"text": "I am enthusiastic about my job.", "dimension": "Dedication"},
    {"text": "My job inspires me.", "dimension": "Dedication"},
    {"text": "When I get up in the morning, I feel like going to work.", "dimension": "Vigor"},
    {"text": "I feel happy when I am working intensely.", "dimension": "Absorption"},
    {"text": "I am proud of the work that I do.", "dimension": "Dedication"},
    {"text": "I am immersed in my job.", "dimension": "Absorption"},
    {"text": "I get carried away when I am working.", "dimension": "Absorption"}
]
````

---

## 🛠️ Non-Functional Requirements

Your code must:

* Be **modular** (use functions appropriately).
* Be **testable**.
* Follow **good naming and coding practices**.
* Handle errors, including invalid user input.

---

## 📝 Grading Criteria (Total: 9 points)

To pass, you must earn **at least 4 points**.

| Criterion                                                                            | Points |
| ------------------------------------------------------------------------------------ | ------ |
| Program runs without errors/warnings                                                 | 1      |
| Program output is correct                                                            | 1      |
| At least one meaningful unit test                                                    | 1      |
| Correctly implements a requested live modification within 5 minutes                  | 3      |
| Answers questions about their own code (max 1 point per answer, 1 minute per answer) | 3      |

Evaluation may occur during the **last lab meeting** or during **exam sessions**.

---

## 🧪 Example Input (User Responses)

```
At my work, I feel bursting with energy. 3
At my job, I feel strong and vigorous. 4
I am enthusiastic about my job. 5
My job inspires me. 4
When I get up in the morning, I feel like going to work. 2
I feel happy when I am working intensely. 5
I am proud of the work that I do. 5
I am immersed in my job. 3
I get carried away when I am working. 4
```

---

## 🧾 Example Output

```
Vigor: mean = 3.00 → Moderate
Dedication: mean = 4.67 → High
Absorption: mean = 4.00 → Moderate
Global Engagement: mean = 3.89 → Moderate
```


