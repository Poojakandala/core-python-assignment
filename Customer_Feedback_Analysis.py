def positive_feedback_percentage(ratings):
    if not ratings:  
        return 0.0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return percentage

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
result = positive_feedback_percentage(ratings)

print(f"Positive Feedback: {result}%")
