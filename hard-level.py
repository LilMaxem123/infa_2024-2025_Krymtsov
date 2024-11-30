import pygame
import sys

# Initialization Pygame
pygame.init()

# Window
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Умная Викторина")
clock = pygame.time.Clock()

# Colors
WHITE = (240, 128, 128)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
SALMON = (250, 128, 114)

# Шрифт
font = pygame.font.Font(None, 60)

# Вопросы и ответы
questions = [
    {"question": "Какой запасной полисахарид у грибов?", "answer": "гликоген"},
    {"question": "Что является ДНК-вирусом?", "answer": "грипп"},
    {"question": "Какой орган выделяет инсулин?", "answer": "поджелудочная железа"},
    {"question": "Как называется кислородное дыхание?", "answer": "аэробное"},
    {"question": "Сколько у здорового человека хромосом?", "answer": "47"},
]

# Текущие состояния
current_question = 0
user_input = ""  # Поле ввода пользователя
show_congratulation = False  # Отображать ли окно с поздравлением
answer_complete = False  # Завершен ли ввод полного ответа
game_over = False  # Флаг завершения игры
incorrect_steps = 0  # Количество шагов для неправильного ввода в пятом вопросе

def draw_question(question, user_input):
    """Отрисовка текущего вопроса и введенного текста."""
    screen.fill(WHITE)

    # Вопрос
    question_surface = font.render(question, True, BLACK)
    question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(question_surface, question_rect)

    # Поле ввода
    input_surface = font.render(user_input, True, BLACK)
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, GRAY, input_rect.inflate(20, 20))
    screen.blit(input_surface, input_rect)

def draw_congratulation():
    """Отрисовка окна с поздравлением."""
    screen.fill(SALMON)
    congrats_surface = font.render("Правильно!", True, BLACK)
    congrats_rect = congrats_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(congrats_surface, congrats_rect)
    subtext_surface = font.render("Нажмите любую клавишу для продолжения...", True, BLACK)
    subtext_rect = subtext_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(subtext_surface, subtext_rect)

def draw_game_over():
    """Отрисовка окна с окончанием игры."""
    screen.fill(SALMON)
    end_text = font.render("Вы проебали!", True, BLACK)
    end_text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(end_text, end_text_rect)

def main():
    global current_question, user_input, show_congratulation, answer_complete, game_over, incorrect_steps

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Обработка ввода
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    # Если игра завершена, ничего не делаем
                    continue
                if show_congratulation:
                    # После поздравления переходим к следующему вопросу
                    show_congratulation = False
                    user_input = ""
                    answer_complete = False
                    current_question += 1
                    if current_question >= len(questions):
                        running = False
                else:
                    # Логика ввода ответа
                    correct_answer = questions[current_question]["answer"]

                    # Для первых 4 вопросов
                    if current_question < 4:
                        if not answer_complete:
                            if len(user_input) < len(correct_answer):
                                user_input += correct_answer[len(user_input)]
                            if user_input == correct_answer:
                                answer_complete = True
                        else:
                            show_congratulation = True
                    # Логика для пятого вопроса (Сколько у здорового человека хромосом?)
                    elif current_question == 4:
                        if incorrect_steps == 0:
                            user_input = "4"  # Первое неправильное нажатие
                            incorrect_steps += 1
                        elif incorrect_steps == 1:
                            user_input = "47"  # Второе неправильное нажатие
                            incorrect_steps += 1
                        elif incorrect_steps == 2:
                            game_over = True  # После третьего нажатия заканчиваем игру

        # Рендер экрана
        if game_over:
            # Если игра завершена, показываем экран с окончанием игры
            draw_game_over()
        elif current_question < len(questions):
            if show_congratulation:
                draw_congratulation()
            else:
                draw_question(questions[current_question]["question"], user_input)
        else:
            screen.fill(SALMON)
            end_text = font.render("Вы проебали! И вы называете себя бмом????", True, BLACK)
            end_text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(end_text, end_text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
