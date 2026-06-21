import streamlit as st

def get_letter_grade(score):
    """Convert numerical score to letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


# Capture user input directly via widget
    
def main():
    st.title("Grade Calculator")
    score = st.number_input("Please enter a number between 0 and 100:", min_value=0, max_value=100, step=1)
    grade = get_letter_grade(score)
    st.success(f"Mark: {int(score)} -> Grade: {grade}")


if __name__ == "__main__":
    main()


