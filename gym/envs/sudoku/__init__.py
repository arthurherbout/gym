from gym.envs.sudoku.sudoku_env import SudokuEnv
from gym.envs.registration import register

register(
    id='Sudoku',
    entry_point='sudoku.sudoku_env:SudokuEnv',
    )
