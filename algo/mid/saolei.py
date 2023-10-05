"""
<div class="html">
  <p>
    <a class="Link Link--ae" href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)" target="_blank">
      Minesweeper
    </a>
    is a popular video game. From Wikipedia, "The game features a grid of
    clickable squares, with hidden "mines" scattered throughout the board. The
    objective is to clear the board without detonating any mines, with help from
    clues about the number of neighboring mines in each field." Specifically,
    when a player clicks on a square (also called a cell) that doesn't contain a
    mine, the square reveals a number representing the number of immediately
    adjacent mines (including diagonally adjacent mines).
  </p>

  <p>
    You're given a two-dimensional array of strings that represents a
    Minesweeper board for a game in progress. You're also given a row and a
    column representing the indices of the next square that the player clicks on
    the board. Write a function that returns an updated board after the click
    (your function can mutate the input board).
  </p>

  <p>
    The board will always contain only strings, and each string will be one of
    the following:
  </p>
  <ul>
    <li><span>"M"</span>: A mine that has not been clicked on.</li>
    <li>
      <span>"X"</span>: A mine that has been clicked on, indicating a lost game.
    </li>
    <li>
      <span>"H"</span>: A cell with no mine, but whose content is still hidden
      to the player.
    </li>
    <li>
      <span>"0-8"</span>: A cell with no mine, with an integer from 0 to 8
      representing the number of adjacent mines. Note that this is a
      single-digit integer represented as a string. For example
      <span>"2"</span> would mean there are 2 adjacent cells with mines.
      Numbered cells are not clickable as they have already been revealed.
    </li>
  </ul>

  <p>
    If the player clicks on a mine, replace the <span>"M"</span> with
    <span>"X"</span>, indicating the game was lost.
  </p>
  <p>
    If the player clicks on a cell adjacent to a mine, replace the
    <span>"H"</span> with a string representing the number of adjacent mines.
  </p>
  <p>
    If the player clicks on a cell with no adjacent mines, replace the
    <span>"H"</span> with <span>"0"</span>. Additionally, reveal all of the
    adjacent hidden cells as if the player had clicked on those cells as well.
  </p>

  <p>
    You can assume the given row and column will always represent a legal move.
    The board can be of any size and have any number of mines in it.
  </p>

  <h3>Sample Input #1</h3>
  <pre><span class="CodeEditor-promptParameter">board</span> = [
  ["M", "M"],
  ["H", "H"],
  ["H", "H"]
]
<span class="CodeEditor-promptParameter">row</span> = 2
<span class="CodeEditor-promptParameter">column</span> = 0
  </pre>
  <h3>Sample Output #1</h3>
  <pre>[
  ["M", "M"],
  ["2", "2"],
  ["0", "0"]
]
  </pre>

  <h3>Sample Input #2</h3>
  <pre><span class="CodeEditor-promptParameter">board</span> = [
  ["H", "H", "H", "H", "M"],
  ["H", "1", "M", "H", "1"],
  ["H", "H", "H", "H", "H"],
  ["H", "H", "H", "H", "H"]
]
<span class="CodeEditor-promptParameter">row</span> = 3
<span class="CodeEditor-promptParameter">column</span> = 4

</pre>
  <h3>Sample Output #2</h3>
  <pre>[
  ["0", "1", "H", "H", "M"],
  ["0", "1", "M", "2", "1"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"]
]
</pre>
</div>
"""


def is_valid(r, c, n_row, n_col):
    return 0 <= r < n_row and 0 <= c < n_col


def get_neighbors(board, r, c):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    neighbors = []
    for direction in directions:
        new_r = r + direction[0]
        new_c = c + direction[1]
        if is_valid(new_r, new_c, len(board), len(board[0])):
            neighbors.append((new_r, new_c))
    return neighbors

def revealMinesweeper(board, row, column):
    # Write your code here.
    if board[row][column] == 'M':
        board[row][column] = 'X'
    else:
        neighbors = get_neighbors(board, row, column)
        adjacent_mine_count = 0
        for neighbor in neighbors:
            if board[neighbor[0]][neighbor[1]] == 'M':
                adjacent_mine_count += 1
        if adjacent_mine_count > 0:
            board[row][column] = str(adjacent_mine_count)
        else:
            board[row][column] = '0'
            for neighbor in neighbors:
                if board[neighbor[0]][neighbor[1]] == 'H':
                    revealMinesweeper(board,neighbor[0], neighbor[1])
    return board


if __name__ == '__main__':
    b = [
        ["H", "H", "H", "H", "M"],
        ["H", "1", "M", "H", "1"],
        ["H", "H", "H", "H", "H"],
        ["H", "H", "H", "H", "H"]
    ]
    print(revealMinesweeper(b, 3, 4))