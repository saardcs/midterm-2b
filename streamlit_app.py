import streamlit as st 
import streamlit.components.v1 as components
import decimal
from itertools import permutations

st.set_page_config(page_title="Midterm", layout="centered")
st.title("Midterm")

st.header("Student Information")
class_options = ["2/11", "2/12"]
selected_class = st.selectbox("Select your class:", class_options)
nickname = st.text_input("Nickname")
student_number = st.text_input("Student Number")

answers = st.secrets["answers"]

# ==== Part I: Sudoku Puzzle (5pts) ====
st.header("Part I: Sudoku Puzzle (5pts)")

# Questions 1–4
questions_1_4 = {
    1: ("The highlighted portion of the sudoku puzzle below is called", 
        ["a. Column", "b. Row", "c. Run", "d. Square"], 
        answers["q1"]),
    2: ("The highlighted portion of the sudoku puzzle below is called", 
        ["a. Column", "b. Row", "c. Run", "d. Square"], 
        answers["q2"]),
    3: ("Given a 6x6 sudoku puzzle, which set of numbers do you use to solve the puzzle?", 
        ["a. 1-4", "b. 1-6", "c. 1-9", "d. 1-100"], 
        answers["q3"]),
    4: ("Given a 9x9 sudoku puzzle, which set of numbers do you use to solve the puzzle?", 
        ["a. 1-4", "b. 1-6", "c. 1-9", "d. 1-100"], 
        answers["q4"])
    }

for qnum in questions_1_4:
    q, opts, _ = questions_1_4[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

    # Insert image after questions 1 and 2
    if qnum == 1:
        st.image("row.png")
    if qnum == 2:
        st.image("column.png")

st.write("**5. Solve the 6x6 Sudoku puzzle using the numbers 1 to 6.**")

puzzle = st.secrets["sudoku"]["puzzle"]
solution = st.secrets["sudoku"]["solution"]

sudoku = components.declare_component("sudoku", path="sudoku_component")
# Call the sudoku component passing the puzzle as default
board = sudoku(default=puzzle)
# st.write(board)

# ==== Part II: Counting Combinations I Puzzle (5pts) ====
st.header("PART II: Counting Combinations I Puzzle (5pts)")
st.write("**Instruction:** Given the colors below, make the possible combinations and answer the following questions.")

st.image("rby.png")

# Question 6: Interactive tower coloring
st.write("### 6. Color the following tower of blocks with all the possible combinations you can make based on the statement above.")

colors = ["", "Red", "Blue", "Yellow"]  # Empty option for unselected blocks
tower_inputs = {}

# Display 6 towers side by side, 3 blocks each
cols = st.columns(6)
for i, col in enumerate(cols):
    with col:
        st.markdown(f"**Tower {i+1}**")
        tower_inputs[i] = []
        for block in range(3):
            block_color = st.selectbox("Select", colors, key=f"tower{i}_block{block}")
            tower_inputs[i].append(block_color)

# Questions 7–8
questions_7_8 = {
    7: ("How many three-block towers can you make if there is a restriction that red and blue blocks cannot be placed next to each other",
        ["a. 2", "b. 4", "c. 6", "d. 8"],
        answers["q7"]),
    8: ("How many three-block towers can you make if there is a restriction that the red blocks cannot be at the top",
        ["a. 2", "b. 4", "c. 6", "d. 8"],
        answers["q8"]),
}

for qnum in questions_7_8:
    q, opts, _ = questions_7_8[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

# Questions 9–10
st.write("**Instruction:** Given the colors below answer the following questions by selecting the correct answer.")
st.image("4_blocks.png")

questions_9_10 = {
    9: ("How many possible block towers can you make",
        ["a. 6", "b. 12", "c. 18", "d. 24"],
        answers["q9"]),
    10: ("How many four-block towers can you make, if there is a restriction that the red block cannot be at the top",
         ["a. 6", "b. 12", "c. 18", "d. 24"],
         answers["q10"]),
}

for qnum in questions_9_10:
    q, opts, _ = questions_9_10[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

# ==== Part III: Counting Combinations II (10pts) ====
st.header("PART III: Counting Combinations II (10pts)")
st.write("**Instruction:** Given the problem below, answer the following questions by selecting the correct answer.")

st.markdown("""
### (Items 11-15)  
**Suppose that the five-character code has the following restrictions:**  
- Numbers and letters  
- Uppercase and lowercase letters  
- Cannot repeat characters
""")
st.image("5ch.png")

questions_11_15 = {
    11: ("What characters can make up the code?",
         ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"],
         answers["q11"]),
    12: ("What sets of characters can the code contain?",
         ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. All of the above"],
         answers["q12"]),
    13: ("How many possible characters are there for the first spot in the password?",
         ["a. 60 possible letters and numbers", "b. 62 possible letters and numbers", 
          "c. 61 possible letters and numbers", "d. 59 possible letters and numbers"],
         answers["q13"]),
    14: ("How many possible characters are there for the fifth spot in the password?",
         ["a. 60 possible letters and numbers", "b. 58 possible letters and numbers", 
          "c. 61 possible letters and numbers", "d. 59 possible letters and numbers"],
         answers["q14"]),
    15: ("How many total password combinations are possible?",
         ["a. 44,261,653,680 possible combinations", 
          "b. 916,132,832 possible combinations", 
          "c. 776,520,240 possible combinations", 
          "d. 13,388,280 possible combinations"],
         answers["q15"]),
}

for qnum in questions_11_15:
    q, opts, _ = questions_11_15[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

st.markdown("""
### (Items 16-20)  
**Suppose that the five-character code has the following restrictions:**  
- Numbers and letters  
- Uppercase letters ONLY
""")
st.image("5ch.png")

questions_16_20 = {
    16: ("What characters can make up the code?",
         ["a. 10 numbers", "b. 26 letters", "c. 10 numbers and 26 letters", "d. 10 numbers and 52 letters"],
         answers["q16"]),
    17: ("What sets of characters can the code contain?",
         ["a. a-z (lowercase letters)", "b. 0-9 (numbers)", "c. A-Z (uppercase letters)", "d. b and c"],
         answers["q17"]),
    18: ("How many possible characters are there for the first spot in the password?",
         ["a. 62 possible letters and numbers", "b. 26 possible letters and numbers", 
          "c. 36 possible letters and numbers", "d. 10 possible letters and numbers"],
         answers["q18"]),
    19: ("How many possible characters are there for the fifth spot in the password?",
         ["a. 26 possible letters and numbers", "b. 22 possible letters and numbers", 
          "c. 36 possible letters and numbers", "d. 32 possible letters and numbers"],
         answers["q19"]),
    20: ("How many total password combinations are possible?",
         ["a. 916,132,832 possible combinations", 
          "b. 60,466,176 possible combinations", 
          "c. 45,239,040 possible combinations", 
          "d. 11,881,376 possible combinations"],
         answers["q20"]),
}

for qnum in questions_16_20:
    q, opts, _ = questions_16_20[qnum]
    st.radio(f"**{qnum}. {q}**", options=opts, key=f"q{qnum}")

# ==== Grading Functions ====
def grade_question_group(question_group):
    correct = 0
    for qnum, (_, _, corr) in question_group.items():
        ans = st.session_state.get(f"q{qnum}", "")
        if ans and ans[0].lower() == corr:
            correct += 1
    return correct

def grade_multiple_groups(*groups, scale):
    total_correct = 0
    total_questions = 0
    for group in groups:
        total_correct += grade_question_group(group)
        total_questions += len(group)
    return round(total_correct / total_questions * scale, 2)

def grade_sudoku(user_board, puzzle, solution):
    total = correct = 0

    if not user_board:
        return 0
    for i in range(6):
        for j in range(6):
            if puzzle[i][j] == 0:
                total += 1
                if user_board[i][j] == solution[i][j]:
                    correct += 1
    return round(correct / total * 3, 2) if total else 0

def grade_part1():
    return grade_multiple_groups(questions_1_4, scale=2) + grade_sudoku(board, puzzle, solution)
    
def grade_block_towers():
    # Grading Q6 (tower permutations)
    valid_towers = list(permutations(['Red', 'Blue', 'Yellow']))
    student_towers = []

    for i in range(6):
        t = [
            st.session_state.get(f"tower{i}_block0", ""),
            st.session_state.get(f"tower{i}_block1", ""),
            st.session_state.get(f"tower{i}_block2", "")
        ]
        if all(c in ("Red", "Blue", "Yellow") for c in t) and len(set(t)) == 3:
            student_towers.append(tuple(t))

    # Count unique valid permutations
    unique_valid = set(student_towers) & set(valid_towers)
    if len(unique_valid) == 6:
        return 1  # Full credit for Q6
    return 0

def grade_part2():
    return grade_block_towers() + grade_multiple_groups(questions_7_8, questions_9_10, scale=4)

def grade_part3():
    return grade_multiple_groups(questions_11_15, questions_16_20, scale=10)

# if st.button("Grade Test"):
#     s1 = grade_part1()
#     s2 = grade_part2()
#     s3 = grade_part3()
#     total = s1 + s2 + s3
#     st.success(f"Scores → Part I: {s1}/5 · Part II: {s2}/5 · Part III: {s3}/10 · **Total: {total}/20**")

# if st.button("Grade Test (with debug)"):
#     for q in range(16, 21):
#         st.write(f"Q{q} answer:", st.session_state.get(f"q{q}", ""))
#     s3 = grade_part3()
#     st.success(f"Part III score: {s3}")

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

if st.button("Submit Test"):
    if not nickname or not student_number:
        st.error("Please fill in your nickname and student number.")
    else:
        # Grade parts
        s1 = grade_part1()
        s2 = grade_part2()
        s3 = grade_part3()
        total = s1 + s2 + s3

        # Build submission record
        submission = {
            "nickname": nickname,
            "student_number": student_number,
            "scores": {
                "part1_sudoku": s1,
                "part2_block_towers": s2,
                "part3_code_combinations": s3,
                "total": total
            },
            "answers": {
                "sudoku": {
                    "board": board,
                    # Q1 to Q4 multiple choice answers
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(1, 5)}
                },

                # Part II: Counting Combinations I (Q7 to Q10 and tower inputs)
                "block_towers": {
                    # Tower inputs (6 towers × 3 blocks)
                    "towers": {
                        f"tower{i}": [
                            st.session_state.get(f"tower{i}_block0", ""),
                            st.session_state.get(f"tower{i}_block1", ""),
                            st.session_state.get(f"tower{i}_block2", "")
                        ]
                        for i in range(6)
                    },
                    # Q7 to Q10 multiple choice answers
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(7, 11)}
                },

                # Part III: Counting Combinations II (Q10 to Q20)
                "code_combinations": {
                    # Q10 to Q15 (first group)
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(11, 16)},
                    # Q16 to Q20 (second group)
                    **{f"q{q}": st.session_state.get(f"q{q}", "") for q in range(16, 21)},
                },
            }
                    }

        # st.markdown("### 📄 Submission Preview")
        # st.json(submission)

        # Save to file
        import json, os
        os.makedirs("submissions", exist_ok=True)
        
        import gspread
        from google.oauth2.service_account import Credentials

        # Set up creds and open your sheet
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        
        # Load credentials from Streamlit secrets
        service_account_info = st.secrets["gcp_service_account"]
        creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
        
        client = gspread.authorize(creds)
        import datetime
        
        # Timestamp for filenames and sheets
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename_ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        json_path = os.path.join("submissions", f'{selected_class.replace("/", "-")}_{nickname}_{student_number}_{filename_ts}.json')
        with open(json_path, "w") as f:
            json.dump(submission, f, indent=2)
            
        try:
            sheet = client.open("Midterm").worksheet(selected_class)
        except gspread.WorksheetNotFound:
            st.error(f"Worksheet '{selected_class}' not found. Please check your Google Sheet.")

        # Convert your submission dict into a list of values (flatten if needed)
        row = [
            student_number,
            nickname,
            s1,
            s2,
            s3,
            total,
            timestamp
            # add other fields or stringify answers if needed
        ]

        sheet.append_row(row)
        # st.success(f"Submission received! ✅ Total Score: {round(total)}/20")
        st.success(f"Submission received!")
        
        with open(json_path, "rb") as f:
            st.download_button(
            "Download answers",
                data=f,
                file_name=os.path.basename(json_path),
                mime="application/json"
            )
