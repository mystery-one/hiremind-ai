class RecruiterInsightAgent:

    def explain_candidate(
        self,
        candidate_name,
        semantic_score,
        experience_score,
        skill_score
    ):

        final_score = (
            0.5 * semantic_score +
            0.3 * experience_score +
            0.2 * skill_score
        )

        if final_score >= 85:
            verdict = "Strong Match"
        elif final_score >= 70:
            verdict = "Good Match"
        else:
            verdict = "Needs Further Evaluation"

        explanation = f"""
Candidate: {candidate_name}

Overall Evaluation: {verdict}

Reasons:
- Strong semantic similarity with job description
- Relevant technical skill alignment
- Experience matches hiring requirements

Final Score: {final_score:.2f}
"""

        return explanation