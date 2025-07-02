# TailorTalk – Conversational Appointment Scheduler

This is a **resubmission** of the TailorTalk assignment with improvements and full deployment on both frontend and backend.

---

## 🔗 Live Links

* **Frontend (Streamlit App):**
  [https://tailortalk-6gtvxuhi7olnu59sfdzk8v.streamlit.app](https://tailortalk-6gtvxuhi7olnu59sfdzk8v.streamlit.app)

* **Backend (FastAPI on Render):**
  [https://tailortalk-backend-wkym.onrender.com](https://tailortalk-backend-wkym.onrender.com)

* **GitHub Repository:**
  [https://github.com/Saishivanichittipolu/TailorTalk-Backend](https://github.com/Saishivanichittipolu/TailorTalk-Backend)

---

## 🛠 Tech Stack

* **Frontend:** Streamlit (Python)
* **Backend:** FastAPI (Python)
* **Hosting:** Render (for backend), Streamlit Cloud (for frontend)
* **Calendar Integration:** Google Calendar API
* **Security:** Service account credentials stored as environment variables

---

## ✅ Features

* Conversational chatbot interface for appointment scheduling
* View upcoming Google Calendar slots
* Book new appointments using natural language
* Chat history retained per session
* Fully deployed backend and frontend

---

## 📦 How to Run Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Saishivanichittipolu/TailorTalk-Backend.git
   cd TailorTalk-Backend
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variable**
   Add your service account JSON content as an environment variable:

   ```bash
   export GOOGLE_SERVICE_ACCOUNT='PASTE_JSON_HERE'
   ```

4. **Start the Backend**

   ```bash
   uvicorn main:app --reload
   ```

5. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

---

## 📌 Notes

* Make sure your Google Calendar has a few test events saved under the **primary calendar**.
* The deployed frontend communicates with the backend hosted on Render.

---

## 🙋‍♀️ Author

**Sai Shivani**
[GitHub](https://github.com/Saishivanichittipolu)
