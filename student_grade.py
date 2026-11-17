
def grade_for(avg):
    if avg >= 70:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 50:
        return "C"
    if avg >= 45:
        return "D"
    if avg >= 40:
        return "E"
    return "F"


def average(scores):
    return sum(scores) / len(scores) if scores else 0.0


students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]},]

# (name, average, grade) for each student
summaries = []
for student in students:
    avg = average(student["scores"])
    summaries.append((student["name"], avg, grade_for(avg)))

passed = [s for s in summaries if s[2] in ("A", "B", "C")]
highest = max(summaries, key=lambda s: s[1])
lowest = min(summaries, key=lambda s: s[1])


passed_names = ", ".join(s[0] for s in passed)
top_name, top_avg = highest[0], highest[1]
low_name, low_avg = lowest[0], lowest[1]

for name, avg, grade in summaries:
    print(f"{name} → Average: {avg:.2f} → Grade: {grade}")

print(f"Passed: {passed_names}")
print(f"Highest: {top_name} ({top_avg:.1f})")
print(f"Lowest: {low_name} ({low_avg:.1f})")