"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # if it is not an end game situation the heuristic function equals number of AI player legal moves
    # Otherwise use the game utility (if AI wins +Inf if AI loses -Inf)
    if game.utility(player) == 0:
        player_moves = game.get_legal_moves(player)
        opponent_moves = game.get_legal_moves(game.get_opponent(player))
        return len(player_moves)/(1 + len(opponent_moves))
    else:
        return game.utility(player)


def custom_score02(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # if it is not an end game situation the heuristic function equals number of AI player legal moves
    # Otherwise use the game utility (if AI wins +Inf if AI loses -Inf)
    if game.utility(player) == 0:
        player_moves = game.get_legal_moves(player)
        opponent_moves = game.get_legal_moves(game.get_opponent(player))
        # In the beginning try to  eliminate the opponent mobility aggressively
        # later try to survive yet ...
        if game.move_count > 0.8 * game.width*game.height:
            return len(player_moves)
        else:
            return len(player_moves)/(1 + len(opponent_moves))
    else:
        return game.utility(player)


def custom_score03(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # if it is not an end game situation the heuristic function equals number of AI player legal moves
    # Otherwise use the game utility (if AI wins +Inf if AI loses -Inf)
    if game.utility(player) == 0:
        player_moves = game.get_legal_moves(player)
        # In the beginning try to  eliminate the opponent mobility aggressively
        # later try to survive yet ...
        if game.move_count > 0.7 * game.width*game.height:
            opponent_moves = game.get_legal_moves(game.get_opponent(player))
            # If the opponent has only one move that leads to opponent loss, force it
            # (as long as the player has further moves after forcing it)
            if len(opponent_moves) == 1:
                next_game = game.forecast_move(opponent_moves[0])
                if len(next_game.get_legal_moves(game.get_opponent(player))) == 0 and \
                                len(next_game.get_legal_moves(player)) > 0:
                    return float("inf")
            return len(player_moves) / (1 + len(opponent_moves))
        else:
            return len(player_moves)
    else:
        return game.utility(player)


def custom_score04(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # if it is not an end game situation the heuristic function equals number of AI player legal moves
    # Otherwise use the game utility (if AI wins +Inf if AI loses -Inf)
    if game.utility(player) == 0:
        if len(game.get_blank_spaces()) < 10:
            return float(len(game.get_legal_moves(player)) *
                         (1+1/(1+len(game.get_legal_moves(game.get_opponent(player))))))
        else:
            # avoid moving to a dead zone (where AI player does not have any further move
            return float(len(game.get_legal_moves(player)) *
                         (1+8/(1+len(game.get_legal_moves(game.get_opponent(player))))))
    else:
        return game.utility(player)


def custom_score05(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # if it is not an end game situation the heuristic function equals number of AI player legal moves
    # Otherwise use the game utility (if AI wins +Inf if AI loses -Inf)
    if game.utility(player) == 0:
        player_moves = game.get_legal_moves(player)

        if len(game.get_blank_spaces()) > 40:
            # Maximize open moves while keeping an eye for aggression in early-game
            opponent_moves = game.get_legal_moves(game.get_opponent(player))
            return float(len(player_moves))
        elif len(game.get_blank_spaces()) > 10:
            # Get more aggressive in mid-game
            opponent_moves = game.get_legal_moves(game.get_opponent(player))
            return float(len(player_moves) - 4*len(opponent_moves))
        else:
            # Get survivalist in the late-game
            opponent_moves = game.get_legal_moves(game.get_opponent(player))
            return float(len(player_moves))

    else:
        return game.utility(player)


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        if len(legal_moves) <= 0:
            return -1, -1

        # Choose the center as the best initial move till finding a better move (if it is available)
        if (3, 3) not in legal_moves and game.move_count <= 1:
            move = (3, 3)
        else:
            move = legal_moves[0]  # To initiate move variable

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring

            if self.method == 'minimax':
                if self.iterative:
                    depth = 0
                    while self.time_left() > self.TIMER_THRESHOLD:
                        _, move = self.minimax(game, depth)
                        depth += 1
                else:
                    _, move = self.minimax(game, self.search_depth)

            if self.method == 'alphabeta':
                if self.iterative:
                    depth = 0
                    while self.time_left() > self.TIMER_THRESHOLD:
                        _, move = self.alphabeta(game, depth)
                        depth += 1
                else:
                    move = self.alphabeta(game, self.search_depth)

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return move

        # Return the best move from the last completed search iteration
        return move

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # Reaching the terminal nodes (the node is not necessarily an end game node but a node considered a sudo-end
        # based on the depth dictated by the iterative deepening code
        if depth == 0:
            return self.score(game, self), None

        # maximizing layer
        if maximizing_player:
            score = float("-inf")
            move = (-1, -1)
            for next_move in game.get_legal_moves():
                new_game = game.forecast_move(next_move)
                move_score, _ = self.minimax(new_game, depth-1, False)
                if move_score > score:
                    score = move_score
                    move = next_move
        # minimizing layer
        else:
            score = float("inf")
            move = (-1, -1)
            for next_move in game.get_legal_moves():
                new_game = game.forecast_move(next_move)
                move_score, _ = self.minimax(new_game, depth - 1, True)
                if move_score < score:
                    score = move_score
                    move = next_move

        return score, move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # Reaching the terminal nodes (the node is not necessarily an end game node but a node considered a sudo-end
        # based on the depth dictated by the iterative deepening code
        if depth == 0:
            return self.score(game, self), None

        # maximizing layer
        if maximizing_player:
            score = float("-inf")
            move = (-1, -1)
            for next_move in game.get_legal_moves():
                new_game = game.forecast_move(next_move)
                move_score, _ = self.alphabeta(new_game, depth-1, alpha, beta, False)
                if move_score > score:
                    score = move_score
                    move = next_move

                # maximize alpha
                alpha = max(alpha, score)
                if alpha >= beta:
                    break

        # minimizing layer
        else:
            score = float("inf")
            move = (-1, -1)
            for next_move in game.get_legal_moves():
                new_game = game.forecast_move(next_move)
                move_score, _ = self.alphabeta(new_game, depth-1, alpha, beta, True)
                if move_score < score:
                    score = move_score
                    move = next_move

                # minimize beta
                beta = min(beta, score)
                if alpha >= beta:
                    break

        return score, move
