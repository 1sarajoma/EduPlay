# Import all necessary modules
import pygame
import sys
import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Create the eductional screen window
root = Tk()
root.title("Educational Quiz Game")
root.geometry("1200x680")
	
# Define all popups and use pillow to load each of their images
def popup1():
    top = Toplevel(root)
    top.title("Fact 1")
    Label(top, text= "Karl Benz made the first car", font = ('Times New Roman', 15, 'bold')).pack()
    path = "car_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup2():
    top = Toplevel(root)
    top.title("Fact 2")
    Label(top, text= "Alexander Graham Bell made the first telephone", font = ('Times New Roman', 15, 'bold')).pack()
    path = "phone_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup3():
    top = Toplevel(root)
    top.title("Fact 3")
    Label(top, text= "The TV was invented in 1927", font = ('Times New Roman', 15, 'bold')).pack()
    path = "tv_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup4():
    top = Toplevel(root)
    top.title("Fact 4")
    Label(top, text= "The radio was invented in 1901", font = ('Times New Roman', 15, 'bold')).pack()
    path = "radio_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup5():
    top = Toplevel(root)
    top.title("Fact 5")
    Label(top, text= "The basis for data transmission on the internet was TCP/IP", font = ('Times New Roman', 15, 'bold')).pack()
    path = "tcp_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup6():
    top = Toplevel(root)
    top.title("Fact 6")
    Label(top, text= "Charles Babbage was involved with the first computer", font = ('Times New Roman', 15, 'bold')).pack()
    path = "computer_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup7():
    top = Toplevel(root)
    top.title("Fact 7")
    Label(top, text= "Apple released the Iphone in 2007", font = ('Times New Roman', 15, 'bold')).pack()
    path = "iphone_popup_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup8():
    top = Toplevel(root)
    top.title("Fact 8")
    Label(top, text= "The Magnavox Odyssey was the first ever game console", font = ('Times New Roman', 15, 'bold')).pack()
    path = "console_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup9():
    top = Toplevel(root)
    top.title("Fact 9")
    Label(top, text= "Roger L. Easton was involved in making the GPS", font = ('Times New Roman', 15, 'bold')).pack()
    path = "gps_popup_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup10():
    top = Toplevel(root)
    top.title("Fact 10")
    Label(top, text= "The CEO of Tesla is Elon Musk", font = ('Times New Roman', 15, 'bold')).pack()
    path = "tesla_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup11():
    top = Toplevel(root)
    top.title("Fact 11")
    Label(top, text= "Windows 10 was released in 2015", font = ('Times New Roman', 15, 'bold')).pack()
    path = "windows_img.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup12():
    top = Toplevel(root)
    top.title("Fact 12")
    Label(top, text= "Akio Morita developed the Sony Walkman", font = ('Times New Roman', 15, 'bold')).pack()
    path = "walkman_popup_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup13():
    top = Toplevel(root)
    top.title("Fact 13")
    Label(top, text= "The worldwide web was invented in 1989", font = ('Times New Roman', 15, 'bold')).pack()
    path = "www_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup14():
    top = Toplevel(root)
    top.title("Fact 14")
    Label(top, text= "Masahiro Hara invented the QR code", font = ('Times New Roman', 15, 'bold')).pack()
    path = "qr_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()
def popup15():
    top = Toplevel(root)
    top.title("Fact 15")
    Label(top, text= "The airplane flew 120 feet on it's very first flight", font = ('Times New Roman', 15, 'bold')).pack()
    path = "plane_popup_img.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image=img)
    panel.photo = img
    panel.pack()

# Place all of the quiz game code inside of the start quiz function
def start_quiz():
    # Initialize all of the needed custom variables
    pygame.init()
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("TechQuiz Game")
    font = pygame.font.Font(None, 48)
    bg_image = pygame.image.load("background.jpg")
    game_over_bg = pygame.image.load("gameoverbg.jpg")
    custom_font = pygame.font.Font("game_font.ttf", 40)

    # Define the background and game over screen
    pygame.mixer.init()
    def bg_music():
        pygame.mixer.music.load("bg_music.mp3")
        pygame.mixer.music.play(loops=-1)
    def game_over_theme():
        pygame.mixer.music.load("game_over.mp3")
        pygame.mixer.music.play(loops=-1)

    # Play the background music
    bg_music()  


    # Define all of the questions
    questions = [
        {
            "question": "Who made the first car?",
            "options": ["Karl Benz", "Albert Einstein", "Steve Jobs"],
            "correct_option": "Karl Benz"
        },
        {
            "question": "Who was associated with the first telephone?",
            "options": ["Nikola Tesla", "Alexander Graham Bell", "Tim Berners-Lee"],
            "correct_option": "Alexander Graham Bell"
        },
        {
            "question": "What was a significant invention in 1927?",
            "options": ["Television", "Iphone", "PC"],
            "correct_option": "Television"
        },
        {
            "question": "When was the radio invented?",
            "options": ["1921", "1851", "1901"],
            "correct_option": "1901"
        },
        {
            "question": "What was the basis for data transmission?",
            "options": ["TCP/IP", "Bluetooth", "Ethernet"],
            "correct_option": "TCP/IP"
        },
        {
            "question": "Who was involved with the first computer?",
            "options": ["Steve Jobs", "Samuel Morse", "Charles Babbage"],
            "correct_option": "Charles Babbage"
        },
        {
            "question": "When did Apple release the Iphone?",
            "options": ["2004", "2007", "2008"],
            "correct_option": "2007"
        },
        {
            "question": "What was the first-ever game console?",
            "options": ["Magnavox Odyssey", "Nintendo 64", "Playstation"],
            "correct_option": "Magnavox Odyssey"
        },
        {
            "question": "What was Roger L. Easton involved in making?",
            "options": ["Laptop", "GPS", "Hard drive"],
            "correct_option": "GPS"
        },
        {
            "question": "Who is the CEO of Tesla?",
            "options": ["Elon Musk", "Steve Jobs", "Mark Zuckerberg"],
            "correct_option": "Elon Musk"
        },
        {
            "question": "Who developed the Sony Walkman?",
            "options": ["Akio Morita", "Jeff Bezos", "Jack Ma"],
            "correct_option": "Akio Morita"
        },
        {
            "question": "When was the World Wide Web Invented?",
            "options": ["1991", "1989", "1988"],
            "correct_option": "1989"
        },
        {
            "question": "What did Masahiro Hara invent?",
            "options": ["QR Codes", "Credit cards", "Barcode scanner"],
            "correct_option": "QR Codes"
        },
        {
            "question": "How many feet was the first airplane flight",
            "options": ["110", "140", "120"],
            "correct_option": "120"
        },
        {
            "question": "What was significant that was created in 1991?",
            "options": ["Windows", "Mac OS", "Linux"],
            "correct_option": "Linux"
        }
    ]

    # Create class for the user
    class User(pygame.sprite.Sprite):
        def __init__(self):
            # Draw the square onto the screen
            super().__init__()
            self.image = pygame.image.load("sprite_resized.png")
            self.rect = self.image.get_rect()
            self.rect.center = (800, 0)

        # Create update function
        def update(self):
            # Set up each movement key
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                
            # Set boundaries for movement 
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > 545:
                self.rect.y = 545
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 745:   
                self.rect.x = 745

    # Create class for enemies                  
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            # Draw the opponents and set their speed and position
            super().__init__()
            self.image = pygame.image.load("enemy_sprite.png")
            self.rect = self.image.get_rect()
            self.vel_x = random.randint(3, 6)
            self.vel_y = random.randint(3, 6)
            self.rect.x = random.randint(0, 768)
            self.rect.y = random.randint(0, 568)

        # Create update function    
        def update(self):
            # Make bouncing off walls effect
            if self.rect.left < 0:
                self.vel_x = -self.vel_x
            if self.rect.right > 800:
                self.vel_x = -self.vel_x
            if self.rect.top < 0:
                self.vel_y = -self.vel_y
            if self.rect.bottom > 600:
                self.vel_y = -self.vel_y
                
            # Move the opponent based off of the random speed chosen
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

    # Create game over function            
    def game_over_screen(time_secs, score):
        while True:
            for event in pygame.event.get():
                # If the user wants to exit out of the game over screen make it so they are able to
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Define custom variables and place them
            time_txt = custom_font.render(f"Time: {time_secs} seconds", True, WHITE)
            score_txt = custom_font.render(f"Score: {score}", True, WHITE)
            screen.blit(game_over_bg, (0, 0))
            screen.blit(time_txt, (200, 100))
            screen.blit(score_txt, (250, 500))
            pygame.display.flip()

    # Create function for choosing the question
    def question():
        global current_question
        global selected_answer
        global game_ongoing
        # Choose a random question and place them in a random position
        current_question = random.choice(questions)
        current_question["x"] = random.randint(350, 550)
        current_question["y"] = random.randint(300, 400)

        # Set boolean variables
        selected_answer = None
        game_ongoing = True

    # Create function for showing the question and making it clickable
    def show_question():
        # Create the surface and rect for the question, and place it above the options
        text_surface = font.render(current_question["question"], True, WHITE)
        text_rect = text_surface.get_rect(center=(current_question["x"], current_question["y"] - 65))
        screen.blit(text_surface, text_rect)
        
        global score
        global option
        keys = pygame.key.get_pressed()
        options = current_question["options"]
        correct_option = current_question["correct_option"]

        # For each option in the list of options
        for i in range(len(options)):
            # Go through the list of options and place them each
            option = options[i]
            option_surface = font.render(option, True, WHITE)
            option_rect = option_surface.get_rect(center=(current_question["x"], current_question["y"] + i * 60))
            screen.blit(option_surface, option_rect)

            # If user clicks space
            if keys[pygame.K_SPACE]:
                # If the space bar is clicked between the middle of the sprite and the option
                if option_rect.collidepoint(user.rect.centerx, user.rect.centery):
                    if option == correct_option:
                        # Add one to the score and load the next question
                        score += 1
                        question()
                    # If it is the wrong option    
                    else:
                        # Place the game over screen, play the theme, and change the state of the variable
                        game_over_theme()
                        game_over = True
                        game_over_screen(timer//60, score)


    all_sprites = pygame.sprite.Group()

    # Add initial 2 enemies
    enemy_group = pygame.sprite.Group()
    for i in range(2):
        enemy = Enemy()
        enemy_group.add(enemy)
        all_sprites.add(enemy)

    # Place user on the screen    
    user = User()
    all_sprites.add(user)

    # Initialize different variables and select the first question
    game_over = False
    running = True
    timer = 0
    global score
    score = 0
    question()

        
        
    while running:
        # Place the background and show the first question
        screen.blit(bg_image, (0, 0))
        show_question()

        # Draw all sprites onto screen
        all_sprites.draw(screen)

        # Every 30 seconds (will also place another one at the start)
        if timer % (60 * 30) == 0:
        # Spawn in another enemy
            enemy = Enemy()
            enemy_group.add(enemy)
            all_sprites.add(enemy)

        for event in pygame.event.get():
            # If user wants to exit out of the game, allow them to do that
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            # Update the sprites
            all_sprites.update()

            # Initialize what would happen if the user and enemy collide
            hits = pygame.sprite.spritecollide(user, enemy_group, False)
            
            if hits:
                # Place the game over screen, play the theme, and change the state of the boolean
                game_over_theme()
                game_over = True
                time_secs = timer // 60
                game_over_screen(time_secs, score)

            # Constantly update the timer
            timer += 1

            # Initialize the font and draw the timer and the score on the screen
            font = pygame.font.Font(None, 36)
            timer_text = font.render(f"Time: {timer // 60}", True, WHITE)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(timer_text, (10, 10))
            screen.blit(score_text, (10, 40))

        # Set the display and clock
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Place all of the images on the educational screen
car_img = ImageTk.PhotoImage(Image.open("car_img.png"))
Label(root, image = car_img).place(x = 300, y = 300)

radio_img = ImageTk.PhotoImage(Image.open("radio_img.png"))
Label(root, image = radio_img).place(x = 10, y = 320)

phone_img = ImageTk.PhotoImage(Image.open("phone_img.png"))
Label(root, image = phone_img).place(x = 120, y = 120)

walkman_img = ImageTk.PhotoImage(Image.open("walkman_img.png"))
Label(root, image = walkman_img).place(x = 900, y = 0)

gps_img = ImageTk.PhotoImage(Image.open("gps_img.png"))
Label(root, image = gps_img).place(x = 750, y = 400)

console_img = ImageTk.PhotoImage(Image.open("console_img.png"))
Label(root, image = console_img).place(x = 450, y = 475)

plane_img = ImageTk.PhotoImage(Image.open("plane_img.png"))
Label(root, image = plane_img).place(x = 370, y = 0)

# Place all of the buttons with their commands on the screen
ttk.Button(root, text= "Car", command= popup1).place(x=130, y=30, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Telephone", command= popup2).place(x=30, y=100, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Television", command= popup3).place(x=600, y=400, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Radio", command= popup4).place(x=100, y=500, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Internet", command= popup5).place(x=250, y=310, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Computer", command= popup6).place(x=400, y=260, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Apple", command= popup7).place(x=300, y=550, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Gaming", command= popup8).place(x=700, y=600, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "GPS", command= popup9).place(x=830, y=620, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Tesla", command= popup10).place(x=760, y=140, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Windows 10", command= popup11).place(x=930, y=260, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Walkman", command= popup12).place(x=1050, y=340, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "WWW", command= popup13).place(x=1000, y=590, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "QR Code", command= popup14).place(x=300, y=90, relheight = 0.08, relwidth = 0.08)
ttk.Button(root, text= "Airplane", command= popup15).place(x=850, y=350, relheight = 0.08, relwidth = 0.08)

Button(root, bg='blue', fg = 'white', text= "Start quiz", command=start_quiz).place(x=600, y=250, relheight = 0.1, relwidth = 0.1)



root.mainloop()

