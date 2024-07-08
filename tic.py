import streamlit as st
import numpy as np

# Constants for the players
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Initialize the board
def initialize_board():
    return np.full((3, 3), EMPTY)

# Check if a player has won the game
def checkWinner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the game is a draw
def checkDraw(board):
    return all(all(cell != EMPTY for cell in row) for row in board)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if checkWinner(board, AI):
        return 1
    if checkWinner(board, HUMAN):
        return -1
    if checkDraw(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Find the best move for the AI
def findBestMove(board):
    best_score = -np.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main game function
def main():
    st.title("Tic-Tac-Toe")
    if 'board' not in st.session_state:
        st.session_state.board = initialize_board()
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'winner' not in st.session_state:
        st.session_state.winner = None

    board = st.session_state.board

    if st.session_state.game_over:
        st.write(f"Game Over! {st.session_state.winner}")
        if st.button("Restart Game"):
            st.session_state.board = initialize_board()
            st.session_state.game_over = False
            st.session_state.winner = None
    else:
        cols = st.columns(3)
        for i in range(3):
            for j in range(3):
                with cols[j]:
                    if board[i][j] == EMPTY:
                        if st.button(f"{EMPTY}", key=f"{i}{j}"):
                            board[i][j] = HUMAN
                            if checkWinner(board, HUMAN):
                                st.session_state.game_over = True
                                st.session_state.winner = "You win!"
                            elif checkDraw(board):
                                st.session_state.game_over = True
                                st.session_state.winner = "It's a draw!"
                            else:
                                move = findBestMove(board)
                                board[move[0]][move[1]] = AI
                                if checkWinner(board, AI):
                                    st.session_state.game_over = True
                                    st.session_state.winner = "AI wins!"
                                elif checkDraw(board):
                                    st.session_state.game_over = True
                                    st.session_state.winner = "It's a draw!"
                    else:
                        st.write(board[i][j])

if __name__ == "__main__":
    main()
