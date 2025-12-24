# Wordle (Flask)

Prosta webowa implementacja gry **Wordle** napisana w Pythonie z użyciem **Flask**.  
Projekt edukacyjny zrealizowany w celu nauki backendu, pracy z sesją oraz integracji Pythona z HTML/CSS.

---

## 🎯 Funkcjonalności

- losowe 5-literowe hasło z pliku tekstowego
- maksymalnie 6 prób (jak w oryginalnym Wordle)
- kolorowy feedback:
  - 🟩 litera na właściwym miejscu
  - 🟨 litera występuje w słowie, ale w innym miejscu
  - ⬜ litera nie występuje w słowie
- walidacja wpisu (5 liter + słowo musi istnieć w słowniku)
- stan gry przechowywany w `session` (Flask)
- blokada wpisywania po wygranej lub po 6 próbach
- przycisk **Reset** rozpoczynający nową grę
- plansza 6×5 zbudowana przy użyciu **CSS Grid**

> Uwaga: logika feedbacku jest w wersji uproszczonej i nie obsługuje jeszcze w 100% wszystkich edge-case’ów związanych z powtórzeniami liter.

---

## 🧠 Technologie

- Python 3
- Flask
- Jinja2
- HTML / CSS (CSS Grid)

---

## 📂 Struktura projektu
.
├── app.py
├── wordlist_fives.txt
└── templates/
└── index.html

---

## ▶️ Uruchomienie lokalnie

1. (Opcjonalnie) utwórz wirtualne środowisko:
   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

2. Zainstaluj Flask:
    ```
    pip install Flask
    
3. Uruchom aplikację:
   ```
   python app.py
   
4. Otwórz w przeglądarce:
   ```
   http://127.0.0.1:5000

---

## 🚀 Pomysły na dalszy rozwój

- pełna obsługa powtórzeń liter (dokładne zasady Wordle)
- klawiatura ekranowa
- animacje kafelków (flip / fade)
- statystyki gier (wygrane, przegrane, streak)
- tryb dark mode
- deployment aplikacji (np. Render, Railway)

---

## 👤 Autor

Projekt wykonany samodzielnie w ramach nauki Pythona i frameworka Flask,
z pomocą mentora AI
