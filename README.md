🤖 AI Hiring Assistant
======================

Project Overview
----------------

AI Hiring Assistant is a smart chatbot designed to streamline technical interviews. It collects candidate details, generates relevant interview questions based on their tech stack, and facilitates an interactive interview session using AI-powered responses. The chatbot is built using **Streamlit** for the frontend and **FastAPI** for the backend, leveraging **Hugging Face API** for AI-driven question generation.

* * * * *

🚀 Installation Instructions
----------------------------

Follow these steps to set up and run the application locally:

### **1️⃣ Clone the Repository**

```
git clone https://github.com/AnirudhGupta007/AI_Hiring_Assistant.git
cd AI_Hiring_Assistant

```

### **2️⃣ Create a Virtual Environment & Activate it**

```
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

```

### **3️⃣ Install Dependencies**

```
pip install -r requirements.txt

```

### **4️⃣ Run the Backend**

```
uvicorn backend:app --reload

```

### **5️⃣ Run the Frontend**

```
streamlit run app.py

```

* * * * *

📖 Usage Guide
--------------

1.  Open the Streamlit UI.
2.  Enter candidate details such as **name, email, experience, tech stack, etc.**
3.  Click **"Start Interview"** to generate questions.
4.  Answer the AI-generated interview questions interactively.
5.  The chatbot will provide real-time responses based on your answers.

* * * * *

🔧 Technical Details
--------------------

-   **Frontend:** Streamlit
-   **Backend:** FastAPI
-   **AI Model:** Hugging Face API (GPT-based model)
-   **Database:** N/A (currently using in-memory data processing)
-   **Deployment:** GitHub, Cloud (TBD)

* * * * *

🎨 Prompt Design
----------------

The chatbot uses carefully crafted prompts to:

-   Extract **candidate details** (structured questions for easy data collection)
-   Generate **relevant technical questions** based on the candidate's tech stack (e.g., Python, FastAPI, ML, React, etc.)
-   Simulate **an interactive interview experience** with AI-driven question-response logic

* * * * *

🛠️ Challenges & Solutions
--------------------------

**1\. Challenge:** Finding an optimal way to generate relevant questions for candidates' tech stacks.

-   **Solution:** Created a structured question bank and used AI-powered selection based on keywords.

**2\. Challenge:** API authentication errors while using Hugging Face.

-   **Solution:** Ensured that the correct API key format and permissions were used.

**3\. Challenge:** Deploying both frontend and backend on a free cloud platform.

-   **Solution:** Researching optimal free-tier cloud services like Render or Hugging Face Spaces.

* * * * *

🎯 Future Enhancements
----------------------

-   Improve **AI question generation** for better relevance.
-   Add **user authentication** to save candidate responses.
-   Integrate **resume parsing** for automated candidate assessment.
-   Deploy on **cloud services** for seamless accessibility.

* * * * *

🤝 Contributing
---------------

Feel free to contribute! Fork the repo, make changes, and submit a pull request.

* * * * *

📞 Contact
----------

For any queries, reach out at **<anirudhgupta@gmail.com>**.
