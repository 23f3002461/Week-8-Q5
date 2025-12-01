"""
Employee Performance Analysis
Email: 23f3002461@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---- Load Data ----
data = pd.read_csv("employees.csv")

# ---- Calculate Frequency of R&D ----
rd_count = (data["department"] == "R&D").sum()
print("Frequency count for R&D department:", rd_count)

# ---- Create Histogram of Departments ----
plt.figure(figsize=(10, 6))
data["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")

# ---- Save Visualization as HTML ----
html_template = f"""
<html>
<head>
<title>Employee Performance Visualization</title>
</head>
<body>
<h2>Employee Performance Analysis</h2>
<p><b>Email:</b> 23f3002461@ds.study.iitm.ac.in</p>
<p><b>R&D Department Count:</b> {rd_count}</p>
<img src="department_hist.png" alt="Histogram">
</body>
</html>
"""

plt.savefig("department_hist.png")

# Save HTML file
with open("report.html", "w") as f:
    f.write(html_template)

print("HTML report saved as report.html")
