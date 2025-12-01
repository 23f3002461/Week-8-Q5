"""
MRR Quarterly Analysis (2024)
Author/Verifier: 23f3002461@ds.study.iitm.ac.in
"""

import matplotlib.pyplot as plt
import numpy as np
import json

# Data (quarterly MRR growth, 2024)
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [8.11, 3.15, 6.31, 9.42]

# Compute stats
average = sum(mrr_growth) / len(mrr_growth)
average_rounded = round(average, 2)  # should be 6.75
industry_target = 15.0

print("Quarterly MRR growth:", mrr_growth)
print("Average MRR growth (2024):", average_rounded)
print("Industry target:", industry_target)

# Create trend plot vs benchmark
x = np.arange(len(quarters))
plt.figure(figsize=(8,5))
plt.plot(x, mrr_growth, marker='o', label='Company MRR growth')
plt.hlines(industry_target, x[0], x[-1], linestyles='--', label=f'Industry target ({industry_target}%)')
plt.xticks(x, quarters)
plt.ylim(0, max(max(mrr_growth) + 5, industry_target + 5))
plt.xlabel('Quarter (2024)')
plt.ylabel('MRR Growth (%)')
plt.title('Monthly Recurring Revenue (MRR) Growth — 2024 Quarters')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("mrr_trend.png", dpi=150)
plt.close()

# Write analysis summary
with open("analysis_output.txt", "w") as f:
    f.write("MRR Quarterly Analysis (2024)\n")
    f.write(f"Company quarterly MRR growth: {mrr_growth}\n")
    f.write(f"Average MRR growth: {average_rounded}\n")
    f.write(f"Industry target: {industry_target}\n")
    f.write("Recommendation: Expand into new market segments\n")

# Write JSON summary
summary = {
    "quarters": quarters,
    "mrr_growth": mrr_growth,
    "average": average_rounded,
    "industry_target": industry_target,
    "recommendation": "Expand into new market segments"
}
with open("analysis_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Saved mrr_trend.png, analysis_output.txt, analysis_summary.json")
