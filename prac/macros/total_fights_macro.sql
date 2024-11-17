{% macro generate_total_fights(wins, losses, draws) %}
    ({{ wins }} + {{ losses }} + {{ draws }}) AS total_fights
{% endmacro %}