def get_behavior_score(candidate):

    signals = []

    redrob = candidate.get(
        "redrob_signals",
        {}
    ) or {}

    possible_fields = [

        "profile_completeness_score",

        "recruiter_response_rate",

        "interview_completion_rate",

        "github_activity_score",

        "offer_acceptance_rate"
    ]

    for field in possible_fields:

        value = redrob.get(
            field,
            None
        )

        if isinstance(
            value,
            (int, float)
        ):

            signals.append(value)

    if redrob.get("open_to_work_flag") is True:

        signals.append(90)

    if not signals:

        return 50

    score = sum(signals) / len(signals)

    return round(
        min(100, score),
        2
    )
