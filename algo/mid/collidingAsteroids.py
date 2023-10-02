"""
<div class="html">
  <p>
    You're given an array of integers <span>asteroids</span>,
    where each integer represents the size of an asteroid.
    The sign of the integer represents the direction the asteroid
    is moving (positive = right, negative = left). All asteroids
    move at the same speed, meaning that two asteroids moving in the same direction can never collide.
  </p>
  <p>
    For example, the integer <span>4</span> represents an asteroid
    of size 4 moving to the right. Similarly, <span>-7</span> represents
    an asteroid of size 7 moving to the left.
  </p>
  <p>
    If two asteroids collide, the smaller asteroid (based on absolute value) explodes.
    If two colliding asteroids are the same size, they both explode.
  </p>
  <p>
    Write a function that takes in this array of asteroids and returns
    an array of integers representing the asteroids after all collisions occur.
  </p>

<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">asteroids</span> = [-3, 5, -8, 6, 7, -4, -7]
</pre>
<h3>Sample Output</h3>
<pre>[-3, -8, 6] <span class="CodeEditor-promptComment">// The -3 moves left, having no collisions.
// The 5 moves right, colliding with the -8 and being destroyed by it.
// The 6 never collides with another asteroid.
// The 7 first collides with the -4, destroying it.
// The 7 and the -7 then collide, both being destroyed.
</span>
</pre></div>
"""

def collidingAsteroids(asteroids):
    q = []
    for asteroid in asteroids:
        if len(q) == 0 or (q[-1] < 0 and asteroid > 0) or (q[-1] * asteroid > 0):
            q.append(asteroid)
        else:
            while True:
                if len(q) == 0 or (q[-1] < 0 and asteroid > 0) or (q[-1] * asteroid > 0):
                    q.append(asteroid)
                    break
                if q:
                    if abs(q[-1]) < abs(asteroid):
                        q.pop()
                    elif abs(q[-1]) == abs(asteroid):
                        q.pop()
                        break
                    else:
                        break
                else:
                    q.append(asteroid)
                    break
    return q


if __name__ == '__main__':
    print(collidingAsteroids([-3,5,-8,6,7,-4,-7]))