#initialize modules
import pygame
import random
from time import sleep 
import math 
from statistics import mean

# Initialize Pygame
pygame.init()


# define Variables
screen_width = 1087
screen_height = 781
image_height = 62
image_width = 57
x_where_is_it = screen_width / 2 - 321 / 2     # divide screen by 2 and divide width of image by 2 to get x coordinate perfectly in middle 
y_where_is_it = screen_height / 2 - 247 / 2      # divide screen by 2 and divide height of image by 2 to get y coordinate perfectly in middle 
x_image = x_where_is_it + 129
y_image = y_where_is_it + 82
time_wait = 5000   # time the program waits while looking at the images in milliseconds
clock = pygame.time.Clock()
random_image_positions = []
font = pygame.font.Font('freesansbold.ttf', 28)
first_runthrough = False
percent_all = []
number_img_displayed = [1,3,4,6,8]
img_num = 0
loop_iteration = 1
loop_iteration_list = [1]
mainloop_iteration = 5
display_percent_distance = False



# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")


# import images
airport = pygame.image.load("airport.png").convert_alpha()
background = pygame.image.load("Background.png").convert_alpha()
bar = pygame.image.load("bar.png").convert_alpha()
bus_station = pygame.image.load("bus station.png").convert_alpha()
cafe = pygame.image.load("cafe.png").convert_alpha()
camping_site = pygame.image.load("camping site.png").convert_alpha()
church = pygame.image.load("church.png").convert_alpha()
gas_station = pygame.image.load("gas station.png").convert_alpha()
hospital = pygame.image.load("hospital.png").convert_alpha()
information = pygame.image.load("information.png").convert_alpha()
library = pygame.image.load("library.png").convert_alpha()
post_office = pygame.image.load("post office.png").convert_alpha()
restroom = pygame.image.load("restroom.png").convert_alpha()
taxi_stand = pygame.image.load("taxi stand.png").convert_alpha()
telephone = pygame.image.load("telephone.png").convert_alpha()
train = pygame.image.load("Train.png").convert_alpha()
where_was_it = pygame.image.load("where was it.png").convert_alpha()
all_symbols = pygame.image.load("all symbols.png").convert_alpha()
exclamation = pygame.image.load("exclamation.png").convert_alpha()

images = [airport, bar, bus_station, cafe, camping_site, church,
             gas_station, hospital, information, library, post_office, restroom,
             taxi_stand, telephone, train]

images_names = ["the airport", "the bar", "the bus station", "the cafe", "the camping site", "the church",
"the gas station", "the hospital", "the information center", "the library", "the post office", "the restroom",
"the taxi stand", "the telephone", "the train station"]

images_number_equivalent = [i for i in range(15)]
# end of importing images 



# function written by ai to do find random variables that dont collide, has same output as mine but is slightly more efficient, (0.001 compared to 0.008)


def aifunc(number_of_images_displayed):
    empty_spaces = {(x, y) for x in range(50, screen_width - 50 - image_width, 100) for y in range(50, screen_height - 50 - image_height, 100)}
    random_image_positions = []
    center_x, center_y = screen_width // 2, screen_height // 2  # get center of screen
    radius = min(screen_width, screen_height) * 0.5  # set radius of circle

    for i in range(number_of_images_displayed):
        while True:
            if not empty_spaces:
                break
            angle = random.uniform(0, 2 * math.pi)  # select random angle within circle
            distance = random.uniform(0, radius)  # select random distance from center
            x = int(center_x + distance * math.cos(angle))  # calculate x position
            y = int(center_y + distance * math.sin(angle))  # calculate y position

            # Check if the new position is at least 50 pixels away from the edge and other pictures
            if (
                x >= 50 and y >= 50 and
                x + image_width + 50 <= screen_width and y + image_height + 50 <= screen_height and
                not any(
                    abs(x - pos[0]) < 100 and abs(y - pos[1]) < 100 for pos in random_image_positions
                )
            ):
                random_image_positions.append((x, y))
                break


    return random_image_positions


#waits a given amount of time without lagging pygame out
def wait_time(milliseconds):
    clock.tick(30)     
    elapsed_time = 0  # starter to count the time that passes in order not to have to stop the program
    #wait for x amount of seconds seconds 
    while elapsed_time < milliseconds: # Display the image for x amount of seconds seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        elapsed_time += clock.tick(30)

def wait_till_keypress():
    keypress = False
    while keypress == False: # Display the image on screen until spacebar pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                keypress = True

        pygame.display.update()



# draws the where was this image screen
def draw_where_was_it(j):
    screen.fill((255,255,255))   #fill white background
    screen.blit(where_was_it, (x_where_is_it, y_where_is_it)) #draw the where was it picture 
    screen.blit(images[random_image_coordinates[j][0]], (x_image, y_image)) #get a random number from the random images list and let that appear
   
    #draw text
    text = font.render(images_names[random_image_coordinates[j][0]], True, (0, 0, 0))
    text_x, text_y = text.get_size()
    screen.blit(text, (screen_width / 2 - text_x/2, screen_height / 2 + 50))



# function that lets the user guess where the image was and drag the image to that point
def drag_to_where_image_was(j):
    pygame.mouse.set_visible(True)
    mouse_click = pygame.mouse.get_pressed()
    screen.blit(background, (0,0))
    

    while not mouse_click[0]: # Display the image for x amount of seconds seconds
        screen.blit(background, (0,0))
        mouse_pos = pygame.mouse.get_pos()

        # default pygame if statement to break off programm while in while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(images[random_image_coordinates[j][0]], (mouse_pos[0]-30, mouse_pos[1]-30))   #constantly display image at current mouse coordinates -30 on each to have it in the middle of the mouse
        mouse_click = pygame.mouse.get_pressed()
        pygame.display.flip()   # update display 


    screen.blit(exclamation, (random_image_coordinates[j][1])) # draw the exclamation point at the pos where the wanted image was displayed

    pygame.draw.circle(screen, (255,0,0), (random_image_coordinates[j][1][0]+30, random_image_coordinates[j][1][1]+30), 120, 3) # draws a red thin circle, at the coordianates of the 
    #exclamation point plus 30 to have it centered and the center isnt the top left corner
    return score(mouse_pos, j)



# small loop to draw all the images
def display_images(number_of_images_displayed):
    random_image_numbers = random.sample(images_number_equivalent,number_of_images_displayed)    #gets a a certain amount of random numbers and cross references them the list of images to get random images
    images_positions = aifunc(number_of_images_displayed)  #gets a certain amount of random images positions that dont overlap to display

    # loop to display the images on screen 
    for i in range(number_of_images_displayed):
        # create random numbers within the picture, meaning not all the way out to the edge,so minus width and height of image and minus borders of background
        screen.blit(images[random_image_numbers[i]], (images_positions[i][0], images_positions[i][1]))
        # Create a new list for each iteration and append it to the 2D array
        new_entry = []
        new_entry.append(random_image_numbers[i])
        new_entry.append((images_positions[i][0], images_positions[i][1]))
        random_image_coordinates.append(new_entry)

        

# score game
def score(mouse_pos, j):
    
    distance = math.sqrt((random_image_coordinates[j][1][0] + 30 - mouse_pos[0])**2 + (random_image_coordinates[j][1][1] + 30 - mouse_pos[1])**2) # calculate distance between the points


# if statements to check if the distance is in the circle, if its within 40 pixels then 100% score, if within the red circle(120 px) then score 
# between 100 and 50%, if its outside of circle but within 320pxl its between 50 and 0% but exponentially dropping instead of linear like in the circle 
    if 1 <= number_img_displayed[img_num]<= 3:
    
        if distance <= 40:
            percentage_score = 100

        elif distance <= 120:
            percentage_score = (((1 - (distance - 40) / 80)))
            percentage_score = percentage_score * 40 + 60

        elif distance <= 320:
            percentage_score = ((math.exp(-4.5 * (distance - 120) / 200)))
            percentage_score = percentage_score * 40
        else: 
            percentage_score = 0

    if 4 <= number_img_displayed[img_num]<= 6:
    
        if distance <= 40:
            percentage_score = 100

        elif distance <= 120:
            percentage_score = (((1 - (distance - 40) / 80)))
            percentage_score = percentage_score * 30 + 70

        elif distance <= 320:
            percentage_score = ((math.exp(-4.5 * (distance - 120) / 200)))
            percentage_score = percentage_score * 70
        else: 
            percentage_score = 0

    if number_img_displayed[img_num]== 8:
    
        if distance <= 40:
            percentage_score = 100

        elif distance <= 120:
            percentage_score = (((1 - (distance - 40) / 80)))
            percentage_score = percentage_score * 20 + 80

        elif distance <= 320:
            percentage_score = ((math.exp(-4.5 * (distance - 120) / 200)))
            percentage_score = percentage_score * 80
        else: 
            percentage_score = 0

     

    score_list.append(percentage_score)
    
    # toggle variable on or off to display the line and text that shows how far off you were
    if display_percent_distance == True:
        pygame.draw.line(screen, (0,0,0), (mouse_pos[0], mouse_pos[1]), (random_image_coordinates[j][1][0] + 30, random_image_coordinates[j][1][1] + 30), 3)  # draw line between images to see distance
        text = font.render(str(int(distance)), True, (0, 0, 0))
        text2 = font.render(str(int(percentage_score)), True, (0, 0, 0))
        screen.blit(text, (300,300))
        screen.blit(text2, (300, 330))


    return percentage_score


def weighted_average(distribution, weights):
    return round(sum([distribution[i]*weights[i] for i in range(len(distribution))])/sum(weights),2)



def find_img_num_displayed(percent_each_exercise, img_num):

    if 35 < mean(percent_each_exercise) < 50:
        img_num = max(img_num - 1, 0)

    if mean(percent_each_exercise) < 35:
        img_num = max(img_num - 2, 0)

    elif 75 < mean(percent_each_exercise) < 100:
        img_num = min(img_num + 1, 4)

    else:
        img_num = min(img_num + 2, 4)

    if img_num == 0:
        loop_iteration = 1

    else:
        loop_iteration = 3

    return img_num, loop_iteration

        

# Game loop
for i in range(mainloop_iteration):
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Update the screen and track elapsed time


# variables to be reset every iteration of loop 
    percent_each_exercise = []
    mouse_pos = ()
    score_list = []
    random_image_coordinates = []
    amount_of_questions = 3
    pygame.mouse.set_visible(False)
# END OF VARIABLE DECLARATION


# display image of all pictures to find only on first iteration 
    if i == 0:
        screen.fill((255,255,255))
        screen.blit(all_symbols, (90,90))
        text_wait_space = font.render("press spacebar to continue", True, (0, 0, 0))
        screen.blit(text_wait_space, (400, 90))
        wait_till_keypress()


#draw x amount of images images once and let them stay on screen for 6 seconds seconds
    screen.blit(background, (0,0))
    display_images(number_img_displayed[img_num])
    wait_time(6000)


# loop through main game loo
    for j in range(loop_iteration):
        draw_where_was_it(j)
        wait_time(2000)
        percent_each_exercise.append(drag_to_where_image_was(j))
        wait_time(2000)

    img_num, loop_iteration = find_img_num_displayed(percent_each_exercise, img_num)
    loop_iteration_list.append(loop_iteration)
    percent_all.append(mean(percent_each_exercise))

    
    # Flip the display
    clock.tick(30)
    pygame.display.flip()

    if i == mainloop_iteration - 1:
        screen.fill((255,255,255))
        text_end_percent = font.render(f"your total percent is {int(weighted_average(percent_all, loop_iteration_list))}", True, (0, 0, 0))
        text_x, text_y = text_end_percent.get_size()
        screen.blit(text_end_percent, (screen_width / 2 - text_x/2, screen_height / 2 + 50))
        text_wait_space = font.render("press spacebar to end", True, (0, 0, 0))
        screen.blit(text_wait_space, (400, 90))
        wait_till_keypress()


# Quit Pygame
pygame.quit()

