from TicTacToe import ticTacToe as t

if __name__ == "__main__":
    # play with human
    p1 = t.Player("computer", exp_rate=0)
    p1.loadPolicy("policy_p1")

    p2 = t.HumanPlayer("human")

    st = t.State(p1, p2)
    st.play2()
