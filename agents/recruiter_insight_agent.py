class RecruiterInsightAgent:

    def generate_insight(
        self,
        candidate_name,
        score
    ):

        if score > 85:
            return f"""
            {candidate_name} is a strong match.
            Recommended for interview shortlist.
            """

        return f"""
        {candidate_name} requires further evaluation.
        """