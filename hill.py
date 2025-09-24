from board import Board
import time

N_QUEENS = 5 # queens constant

def queen_row(n, col):
  row = [0] * n
  row[col] = 1
  return row

def main():
  board = Board(N_QUEENS)
  board_map = board.get_map()
  best_fitness_value = board.get_fitness()
  best_fitness_map = [r[:] for r in board_map]
  row = 0

  while True:
    
    # end if solution is found
    if board.get_fitness() == 0:
      board.print_map()
      break

    # represents if the move that was made improved the fitness score
    fitness_improved = False

    for col in range(N_QUEENS):
      board_map[row] = queen_row(N_QUEENS, col)
      new_fitness_value = board.get_fitness()
      if new_fitness_value < best_fitness_value:
        best_fitness_value = new_fitness_value
        best_fitness_map = [r[:] for r in board_map] # deep copy since .copy() copies only outer list
        fitness_improved = True
    board_map[:] = [r[:] for r in best_fitness_map]

    if fitness_improved == False:
      board = Board(N_QUEENS)
      board_map = board.get_map()
      best_fitness_value = board.get_fitness()
      best_fitness_map = [r[:] for r in board_map]
      row = 0
    else:
      row = 0 if row == N_QUEENS - 1 else row + 1

if __name__ == "__main__":
  start_time = time.time()
  main()
  print("Running time:", (time.time() - start_time), "seconds")



  # =========== Test functions ===================== #
  # test = Board(5)
  # print(f"fitness: {test.get_fitness()}")
  # print(f"map array: {test.get_map()}")
  # test.print_map()
  # print(f"Encoded: {test.encode()}\n")

  # test.decode('20314')
  # print("fitness: ", end="")
  # print(test.get_fitness())
  # test.print_map()
  # print(f"Encoded {test.encode()}")
  # print("========================")
  # ================================================= #