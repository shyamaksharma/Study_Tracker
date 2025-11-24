# Functional Requirements

# 1. Input Module Requirements
	1.	The system shall prompt the user to enter the number of days for which they want to record study activity.
	2.	The system shall allow the user to enter multiple subjects for each day.
	3.	The system shall allow the user to enter the number of minutes spent on each subject.
	4.	The system shall validate that:
	•	subject names are non-empty strings
	•	study time is a positive integer
	5.	The system shall allow the user to stop adding subjects for a day by typing the exit keyword (done).
	6.	The system shall repeat this input collection process for all days requested by the user.

⸻

# 2. Processing Module Requirements
	1.	The system shall store each day’s study records in a structured format.
	2.	The system shall compute the total minutes studied for each day.
	3.	The system shall identify:
	•	the subject with the maximum study time for the day
	•	the subject with the minimum study time for the day
	4.	The system shall correctly handle:
	•	days where only one subject was studied (max = min = same subject)
	5.	The system shall prepare a structured data summary for the output module.

⸻

# 3. Output Module Requirements
	1.	The system shall display all subjects studied during each day along with minutes spent.
	2.	The system shall display the total study time per day.
	3.	The system shall output the most studied and least studied subjects clearly.
	4.	The system shall display results in a clean, readable format with headings.
	5.	The system shall handle special situations such as:
	•	days with only one subject
	•	invalid inputs (with user-friendly error messages)
