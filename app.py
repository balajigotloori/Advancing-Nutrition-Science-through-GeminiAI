import streamlit as st
import google.generativeai as genai

# -----------------------------
# CONFIGURE API KEY
# -----------------------------
genai.configure(api_key="enter Your API KEY")

# Use working model
model = genai.GenerativeModel("models/gemini-flash-latest")

# -----------------------------
# FUNCTION TO GENERATE RESPONSE
# -----------------------------


def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🥗 NutriAI")
st.sidebar.info("AI-powered Nutrition Assistant")

feature = st.sidebar.radio(
    "Select Feature",
    ["🍎 Nutrition Analyzer", "📅 Meal Planner", "💬 AI Coach"]
)

# -----------------------------
# MAIN TITLE
# -----------------------------
st.title("🥗 NutriAI - Smart Nutrition Assistant")
st.markdown(
    "Get instant nutrition insights, personalized meal plans, and expert advice.")

# -----------------------------
# FEATURE 1 - NUTRITION ANALYZER
# -----------------------------
if feature == "🍎 Nutrition Analyzer":

    st.subheader("🍎 Nutrition Analyzer")
    st.info("Enter food items separated by commas. Example: apple, rice, chicken")

    food_items = st.text_area("Food Items")

    if st.button("Analyze Nutrition"):
        if not food_items.strip():
            st.error("Please enter food items")
        else:
            prompt = f"""
            You are a professional nutritionist.

            Analyze the following food items: {food_items}

            Provide output in this format:

            ### Food Item: <name>
            - Calories (kcal):
            - Protein (g):
            - Fat (g):
            - Carbohydrates (g):
            - Vitamins:
            - Minerals:

            Make it clean, structured, and easy to read.
            """

            with st.spinner("🤖 Analyzing nutritional information..."):
                result = generate_response(prompt)

                st.subheader("📊 Nutrition Results")
                st.markdown(result)

# -----------------------------
# FEATURE 2 - MEAL PLANNER
# -----------------------------
elif feature == "📅 Meal Planner":

    st.subheader("📅 Meal Planner")
    st.info("Describe your diet: vegetarian, weight loss, gym diet, allergies, etc.")

    user_input = st.text_area("Enter your preferences")

    if st.button("Generate Meal Plan"):
        if not user_input.strip():
            st.error("Please enter your preferences")
        else:
            prompt = f"""
            You are a certified diet planner.

            Create a detailed 7-day meal plan based on:
            {user_input}

            Format:

            Day 1:
            Breakfast:
            Lunch:
            Dinner:

            Day 2:
            ...

            Ensure:
            - Balanced nutrition
            - Variety in meals
            - Simple recipes

            At the end, provide a grocery list.
            """

            with st.spinner("📅 Generating meal plan..."):
                result = generate_response(prompt)

                st.subheader("📋 Weekly Meal Plan")
                st.markdown(result)

# -----------------------------
# FEATURE 3 - AI COACH
# -----------------------------
elif feature == "💬 AI Coach":

    st.subheader("💬 AI Nutrition Coach")
    st.info("Ask anything about diet, fitness, or nutrition")

    question = st.text_input("Enter your question")

    if st.button("Get Advice"):
        if not question.strip():
            st.error("Please enter a question")
        else:
            prompt = f"""
            You are a professional nutrition coach.

            Answer the following question:
            {question}

            Provide:
            - Clear explanation
            - Practical advice
            - Simple actionable steps

            Keep it concise and useful.
            """

            with st.spinner("💬 Generating advice..."):
                result = generate_response(prompt)

                st.subheader("💡 Expert Advice")
                st.markdown(result)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("⚡ Powered by Google Gemini AI | Built with Streamlit")
