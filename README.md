
This project is a hybrid **educational app + quiz game** built with **Tkinter** and **Pygame**.
It is designed to teach users about important technological inventions and historical facts while providing an interactive game experience.

---

✨ Features

🖼️ Educational Screen (Tkinter)

* Displays images of important inventions (car, radio, airplane, phone, etc.).
* Each invention has a **button** — clicking it opens a popup window with:

  * A fact about the invention.
  * An image loaded via **Pillow (PIL)**.

🎮 Quiz Game (Pygame)

* Starts when the **"Start Quiz"** button is pressed.
* Player controls a **sprite character** with arrow keys.
* Random **quiz questions** appear on the screen with multiple-choice answers.
* To answer, the player moves their sprite to the correct option and presses **SPACE**.
* Enemies bounce around the screen — colliding with one ends the game.
* Every 30 seconds, a new enemy spawns to increase difficulty.
* Tracks **score** (correct answers) and **time survived**.
* Includes background music and a game-over theme.

---

▶️ How to Run

Run the script in your terminal or IDE:

python main.py

* On launch, you’ll see the **educational screen** with images and buttons.
* Click invention buttons to learn facts.
* Press **"Start Quiz"** to begin the interactive game.

---

🎯 Gameplay Controls

* **Arrow Keys** → Move player.
* **SPACE** → Select an answer when colliding with an option.
* **Close window / Quit** → Exit the game.

---
