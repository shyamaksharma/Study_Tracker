# Study_Tracker

# 1. Problem Statement

Students often study multiple subjects daily but struggle to keep track of how much time they actually spend on each subject. Without proper tracking, it becomes difficult to identify study patterns, evaluate productivity, or understand which subjects need more attention.

The Study_Tracker system solves this problem by recording daily study sessions, calculating useful statistics, and presenting them clearly to the user.

⸻

# 2. Scope of the Project

	The scope of this project includes:
		•	Recording study activity for a user-defined number of days
		•	Accepting multiple subjects per day
		•	Storing minutes studied for each subject
		•	Processing the daily study data to compute totals and find patterns
		•	Displaying clean visual/text-based summaries per day
		•	Validating inputs to ensure reliable and accurate data

⸻

# 3. Target Users

	The system is designed for:
		•	Students wanting to track their daily study time
		•	Anyone preparing for exams or competitive tests
		•	Individuals who want a simple way to monitor their learning habits

⸻

# 4. High-Level Features

	The Study_Tracker system provides the following key functionalities:
	
	Input Features
		•	Users can enter the number of days to track
		•	Users can input multiple subjects per day
		•	Each subject has a study duration (in minutes)
		•	Input validation ensures correct entries
	
	Processing Features
		•	Total study minutes calculated for each day
		•	Most-studied and least-studied subjects identified
		•	Single-subject days supported smoothly
	
	Output Features
		•	Daily study summary printed clearly
		•	A mini bar chart (using “#”) to visualize minutes studied
		•	Highlights of maximum and minimum study subjects
	
	Structural Features
		•	Fully modular architecture:
		•	Input.py
		•	processing.py
		•	output.py
		•	main.py
		•	Clean folder structure compatible with GitHub submissions
		•	Readable, maintainable code
