import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (under 8 characters)")

    # Character variety checks
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Missing lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Missing uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Missing numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Missing symbols")

    # Repeated characters check
    if len(set(password)) < len(password) * 0.7:
        score -= 1
        feedback.append("Too many repeated characters")

    # Score
    max_score = 6
    normalized_score = max(0, min(score, max_score))

    if normalized_score >= 5:
        strength = "Strong"
    elif normalized_score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": normalized_score,
        "out_of": max_score,
        "strength": strength,
        "feedback": feedback
    }

pw = input("Enter a password to check: ")
result = check_password_strength(pw)

print(f"\nStrength: {result['strength']} ({result['score']} / {result['out_of']})")
if result['feedback']:
    print("Suggestions:")
    for tip in result['feedback']:
        print(f"- {tip}")
