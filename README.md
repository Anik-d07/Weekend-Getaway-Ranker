# Weekend Getaway Ranker 🧳

A simple Python-based recommendation engine that ranks Indian cities
for weekend travel using ratings, popularity, and visit duration.

This project is built as part of the **Aeka Advisors – Python Developer** assignment.

---

## 📌 Problem Statement

Build a recommendation engine for local travel based on the
**India's Must-See Places** dataset.

**Input:** Source City  
**Output:** Ranked list of top weekend destinations

---

## 🧠 Approach & Logic

The dataset does not contain geographical distance between cities.
Therefore, **Time Needed to Visit in hrs** is used as a proxy for weekend feasibility.

The ranking is based on:
- **Google Review Rating** → Visitor satisfaction  
- **Number of Google Reviews (in lakhs)** → Popularity  
- **Time Needed to Visit in hrs** → Lower time suits weekend trips  

### Ranking Formula
score = average_rating + popularity − average_time_needed

Cities with higher scores are better suited for weekend travel.

---

## 🛠 Tech Stack

- Python
- Pandas

---

## 📂 Project Structure

WEEKEND_GETAWAY_RANKER/
├── ranker.py
├── Top_Indian_Places_to_Visit.csv
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Execution

Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Anik-d07/Weekend-Getaway-Ranker
cd WEEKEND_GETAWAY_RANKER
2️⃣ Install Dependencies
Ensure Python 3.9+ is installed, then run:

bash
pip install -r requirements.txt

3️⃣ Run the Script

bash
python ranker.py

4️⃣ Provide Input
When prompted, enter the source city:

bash
Enter source city: Delhi
The program will display the top recommended weekend destinations.

📊 Sample Output (Three Cities)

▶️ Source City: Delhi

Top weekend destinations from Delhi:
              City          State  avg_rating  popularity  avg_time      score
82       Hyderabad      Telangana    4.390909        8.77  1.772727  11.388182
137         Mumbai     Maharastra    4.480000        8.25  2.300000  10.430000
70   Greater Noida  Uttar Pradesh    4.400000        7.85  2.000000  10.250000
24       Bangalore      Karnataka    4.440000        5.66  1.200000   8.900000
112        Kolkata    West Bengal    4.480000        5.64  1.650000   8.470000

▶️ Source City: Mumbai

Top weekend destinations from Mumbai:
              City          State  avg_rating  popularity  avg_time      score
57           Delhi          Delhi    4.381250        9.69  2.218750  11.852500
83       Hyderabad      Telangana    4.390909        8.77  1.772727  11.388182
71   Greater Noida  Uttar Pradesh    4.400000        7.85  2.000000  10.250000
24       Bangalore      Karnataka    4.440000        5.66  1.200000   8.900000
113        Kolkata    West Bengal    4.480000        5.64  1.650000   8.470000

▶️ Source City: Bangalore

Top weekend destinations from Bangalore:
              City          State  avg_rating  popularity  avg_time      score
56           Delhi          Delhi    4.381250        9.69  2.218750  11.852500
82       Hyderabad      Telangana    4.390909        8.77  1.772727  11.388182
137         Mumbai     Maharastra    4.480000        8.25  2.300000  10.430000
70   Greater Noida  Uttar Pradesh    4.400000        7.85  2.000000  10.250000
112        Kolkata    West Bengal    4.480000        5.64  1.650000   8.470000

