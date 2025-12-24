import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "dev"


def load_words(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f]
    words = [w for w in words if len(w) == 5 and w.isalpha()]
    return words


words = load_words("wordlist_fives.txt")
words_set = set(words)


def is_valid(guess, words_set):
    return len(guess) == 5 and guess.isalpha() and guess in words_set


def score(guess, secret):
    word_guessed = list(guess)
    word_secret = list(secret)
    result = []

    for idx in range(5):
        if word_guessed[idx] == word_secret[idx]:
            result.append("G")
        elif word_guessed[idx] in word_secret:
            result.append("Y")
        else:
            result.append("B")

    return "".join(result)


@app.route("/", methods=["GET", "POST"])
def index():
    if "secret" not in session:
        session["secret"] = random.choice(words)
        session["attempts"] = []

    error_msg = None
    game_over = False  # <-- DODAJ

    # jeśli już koniec (np. odświeżenie strony)
    if len(session.get("attempts", [])) >= 6:  # <-- DODAJ
        game_over = True  # <-- DODAJ

    if request.method == "POST" and not game_over:  # <-- ZMIANA
        guess = request.form.get("guess", "").strip().lower()

        if not is_valid(guess, words_set):
            error_msg = "Błędne słowo (5 liter, musi być w słowniku)"
        else:
            feedback = score(guess, session["secret"])

            attempts = session.get("attempts", [])
            attempts.append((guess, feedback))
            session["attempts"] = attempts
            session.modified = True

            if feedback == "GGGGG":
                error_msg = "Wygrana! 🎉"
                game_over = True  # <-- DODAJ
            elif len(session["attempts"]) >= 6:
                error_msg = f"Koniec prób! Hasło to: {session['secret']}"
                game_over = True  # <-- DODAJ

    board = [[{"letter": "", "state": ""} for _ in range(5)] for _ in range(6)]

    for row_i, (g, fb) in enumerate(session["attempts"][:6]):
        for col_i in range(5):
            board[row_i][col_i]["letter"] = g[col_i].upper()
            board[row_i][col_i]["state"] = fb[col_i]

    return render_template(
        "index.html",
        board=board,
        attempts=session["attempts"],
        error_msg=error_msg,
        game_over=game_over,  # <-- DODAJ
    )


@app.post("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
