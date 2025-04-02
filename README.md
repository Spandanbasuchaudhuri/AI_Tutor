# Unnati - AI-Powered Educational Platform

## Overview
Unnati is a personalized, interactive educational platform powered by AI, specifically designed for students ranging from elementary to high school. The platform dynamically generates courses, assessments, and quizzes tailored to the user's education level and performance, providing an adaptive learning experience to maximize educational outcomes. The intuitive design ensures an engaging user experience, motivating students to achieve their educational goals effectively.

## Features

### User Management
- **User Registration:** Users can register by providing their full name, username, password, age, and school level (`Elementary School`, `Middle School`, or `High School`)【30†source】.
- **User Login:** Users securely log in using their credentials verified against stored data【29†source】.
- **User Profiles:** User-specific data, including educational level and course progress, is stored and retrieved from CSV files【31†source】.
- **Secure Data Handling:** Robust data security measures ensure user privacy and confidentiality of sensitive information.

### Preassessment Module
- Students take a preassessment test based on their educational level (`Elementary`, `Middle`, `High School`)【20†source】.
- The system selects a randomized subset of MCQs for each user.
- Scores determine the recommended course difficulty (`Beginner`, `Intermediate`, `Advanced`) and are stored in the user's profile【20†source】.
- Immediate feedback on performance to guide users effectively.

### Course Generation
- Courses are dynamically generated using AI models (Llama3:8b and Gemma 2B via Ollama)【26†source】【28†source】.
- Users input a course topic, after which the system generates a structured course outline with modules and submodules【25†source】.
- Detailed module content is created automatically with extensive explanations, real-world examples, and practical insights【28†source】.
- Continuous AI improvement ensures the generation of relevant, up-to-date educational content.

### Content UI
- Users can generate and interact with module content, marking completion progress【24†source】.
- Visual progress tracking through graphical interfaces (donut charts) indicating completed modules【24†source】.
- Completion statuses are logged and stored for progress tracking.
- User-friendly layout with easy navigation for enhanced learning engagement.

### MCQ Assessment
- MCQs are generated automatically based on module content using a Retrieval-Augmented Generation (RAG) approach【27†source】.
- Questions and answers are stored temporarily in CSV format for quick access and state persistence【23†source】.
- Users can retake quizzes if a passing score is not achieved, ensuring mastery before proceeding【23†source】.
- Automatic scoring and detailed feedback help students identify areas needing improvement.

### Sidebar Navigation
- Easy-to-navigate UI using a streamlined sidebar for switching between key pages (`Login`, `Preassessment`, `Course Selection`, `Content UI`, `MCQ`)【22†source】.
- Real-time updates reflecting user progress and status.

## Performance Considerations
The Unnati platform was developed and optimized on an NVIDIA RTX 3050 GPU with 20GB RAM. Performance and responsiveness of AI-driven components may vary based on your system's hardware specifications and architecture. For optimal performance, it is recommended to use similar or higher hardware configurations.

## Technologies Used
- **Frontend:** Streamlit for user-friendly web interfaces.
- **Backend & AI Models:** Python, Ollama for AI model interactions (Llama3:8b, Gemma 2B).
- **Data Management:** CSV and JSON files for user data storage and MCQ management.
- **Visualization:** Matplotlib for creating interactive and informative graphics.

## Project Structure
```
Unnati/
├── auth/
│   ├── login.py
│   ├── register.py
│   └── profiles.py
├── pages/
│   ├── preassessment_ui.py
│   ├── content_ui.py
│   ├── mcq_ui.py
│   ├── sidebar.py
│   └── login_ui.py
├── main.py
├── course_gen.py
├── mcq_gen.py
├── course_content_gen.py
├── users/
│   └── [username]/
│       ├── courses/
│       └── scores/
├── preassessment/
│   ├── Elementary_MCQ_Full_Set.csv
│   ├── Middle_School_MCQ_Test_Full.csv
│   └── High_School_MCQ_Test_Full.csv
└── README.md
```

## Getting Started
1. **Installation:** Clone this repository and install required dependencies.
   ```bash
   git clone [repository_url]
   cd Unnati
   pip install -r requirements.txt
   ```
2. **Running the App:**
   ```bash
   streamlit run main.py
   ```
3. **Access the application:** Visit `http://localhost:8501` in your web browser.

## System Requirements
- **GPU:** NVIDIA RTX 3050 or higher recommended
- **Memory:** 12GB RAM or more
- **Storage:** Adequate storage space for datasets, user information, and generated content

## Contribution
Feel free to contribute to the development of Unnati by submitting pull requests, suggesting features, or reporting issues. We welcome educational specialists, developers, and UX/UI designers to collaborate and enhance the platform's capabilities.
