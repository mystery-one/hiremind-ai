class RankingAgent:

    def rank_candidates(
        self,
        semantic_score,
        experience_score,
        behavioral_score
    ):

        final_score = (
            0.5 * semantic_score +
            0.3 * experience_score +
            0.2 * behavioral_score
        )

        return final_score