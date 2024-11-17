SELECT
    first_name || ' ' || last_name AS name,
    weight,
    height,
    reach,
    stance,
    {{ generate_win_percentage('wins', 'losses', 'draws') }}, 
    {{ generate_total_fights('wins', 'losses', 'draws') }},
    wins,
    losses,
    draws
FROM
    {{ ref('fighters') }} 