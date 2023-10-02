"""
<div class="html">
  <p>
    In the game of Blackjack, the dealer must draw cards until the sum of the
    values of their cards is greater than or equal to a
    <span>target</span> value minus 4. For example, traditional Blackjack uses a
    <span>target</span> value of 21, so the dealer must draw cards until their
    total is greater than or equal to 17, at which point they stop drawing cards
    (they "stand"). If the dealer draws a card that brings their total above the
    <span>target</span> (above 21 in traditional Blackjack), they lose (they
    "bust").
  </p>
  <p>
    Naturally, when a dealer is drawing cards, they can either end up standing
    or busting, and this is entirely up to the luck of their draw.
  </p>

  <p>
    Write a function that takes in a <span>target</span> value as well as a
    dealer's <span>startingHand</span> value and returns the probability that
    the dealer will bust (go over the <span>target</span> value before
    standing). The <span>target</span> value will always be a positive integer,
    and the <span>startingHand</span> value will always be a positive integer
    that's smaller than or equal to the <span>target</span> value.
  </p>

  <p>
    For simplicity, you can assume that the dealer has an infinite deck of cards
    and that each card has a value between 1 and 10 inclusive. The likelihood of
    drawing a card of any value is always the same, regardless of previous
    draws.
  </p>

  <p>
    Your solution should be rounded to 3 decimal places and to the nearest
    value. For example, a probability of <span>0.314159</span> would be rounded
    to <span>0.314</span>, while a probability of <span>0.1337</span> would be
    rounded to <span>0.134</span>.
  </p>
  <h3>Sample Input</h3>
  <pre><span class="CodeEditor-promptParameter">target</span> = 21
<span class="CodeEditor-promptParameter">startingHand</span> = 15
</pre>
  <h3>Sample Output</h3>
  <pre>0.45 <span class="CodeEditor-promptComment">// Drawing a 2-6 would result in the dealer standing.</span>
<span class="CodeEditor-promptComment">// Drawing a 7-10 would result in the dealer busting.</span>
<span class="CodeEditor-promptComment">// Drawing a 1 would result in a 16, meaning the dealer keeps drawing.</span>
<span class="CodeEditor-promptComment">// Drawing with a 16 results in a 0.5 probability of busting (6-10 all result in busts).</span>
<span class="CodeEditor-promptComment">// The overall probability of busting is 0.4 + (0.1 * 0.5)</span>
<span class="CodeEditor-promptComment">// (the probability of busting on the first draw + the probability of busting on the second).</span>
</pre>
</div>
"""

def blackjackProbability(target, startingHand):
    memo = {}
    return round(calculate_prob(startingHand, target, memo), 3)


def calculate_prob(current_hand, target, memo):
    if current_hand in memo:
        return memo[current_hand]
    if current_hand > target:
        return 1
    if current_hand + 4 >= target:
        return 0
    total_prob = 0
    for dc in range(1, 11):
        total_prob += 0.1 * calculate_prob(current_hand + dc, target, memo)
    memo[current_hand] = total_prob
    return total_prob