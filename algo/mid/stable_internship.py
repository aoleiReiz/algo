"""
<div class="html">
<p>
  A company has hired N interns to each join one of N different teams. Each
  intern has ranked their preferences for which teams they wish to join, and
  each team has ranked their preferences for which interns they prefer.
</p>
<p>
  Given these preferences, assign 1 intern to each team. These assignments
  should be "stable," meaning that there is no unmatched pair of an intern and a
  team such that both that intern and that team would prefer they be matched
  with each other.
</p>
<p>
  In the case there are multiple valid stable matchings, the solution that is
  most optimal for the interns should be chosen (i.e. every intern should be
  matched with the best team possible for them).
</p>
<p>
  Your function should take in 2 2-dimensional lists, one for interns and
  one for teams. Each inner list represents a single intern or team's preferences,
  ranked from most preferable to least preferable. These lists will always be
  of length N, with integers as elements. Each of these integers corresponds
  to the index of the team/intern being ranked. Your function should return a
  2-dimensional list of matchings in no particular order. Each matching should
  be in the format [internIndex, teamIndex].
</p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">interns</span> = [
  [0, 1, 2],
  [1, 0, 2],
  [1, 2, 0]
]
</pre>
<pre><span class="CodeEditor-promptParameter">teams</span> = [
  [2, 1, 0],
  [1, 2, 0],
  [0, 2, 1]
]
</pre>
<h3>Sample Output</h3>
<pre><span class="CodeEditor-promptComment">// This is the most optimal solution for interns</span>
[
  [0, 0],
  [1, 1],
  [2, 2]
]
</pre>

<pre><span class="CodeEditor-promptComment">// This is also a stable matching, but it is suboptimal for the interns
// because interns 0 and 2 could have been given better team matchings</span>
[
  [2, 0],
  [1, 1],
  [0, 2]
]
</pre>
</div>
"""


def stableInternships(interns, teams):
    choosen_interns = {}
    freeze_interns = list(range(len(interns)))
    current_intern_choice = [0] * len(interns)

    team_map = []
    for team in teams:
        rank = {}
        for i, intern_num in enumerate(team):
            rank[intern_num] = i
        team_map.append(rank)

    while len(freeze_interns) > 0:
        intern_num = freeze_interns.pop()

        intern = interns[intern_num]
        team_preference = intern[current_intern_choice[intern_num]]
        current_intern_choice[intern_num] += 1

        if team_preference not in choosen_interns:
            choosen_interns[team_preference] = intern_num
            continue

        prev_team_rank = team_map[team_preference][choosen_interns[team_preference]]
        current_rank = team_map[team_preference][intern_num]
        if current_rank < prev_team_rank:
            freeze_interns.append(choosen_interns[team_preference])
            choosen_interns[team_preference] = intern_num
        else:
            freeze_interns.append(intern_num)

    return [[intern_num, team_num] for team_num, intern_num in choosen_interns.items()]


if __name__ == '__main__':
    print(stableInternships([
        [0, 1, 2],
        [1, 0, 2],
        [1, 2, 0]
    ], [
        [2, 1, 0],
        [1, 2, 0],
        [0, 2, 1]
    ]))
