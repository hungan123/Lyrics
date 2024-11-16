import time
import sys
import random
from colorama import *
import pygame

init()
pygame.init()
pygame.mixer.init()

colors = [
    Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.CYAN,
    Fore.LIGHTWHITE_EX, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA
]

lyrics = [
    "Rảnh không baby (baby baby)", #1
    "Anh phi qua này (huh ah huh ah)", #2
    "Em thèm đồ Tây", #3
    "Để đưa em qua Hàn (진짜)", #4
    "Có một sự thật là tính hơi lowkey", #5
    "Nhưng khi cạnh em mất luôn lầm lì", #6
    "Suốt bấy lâu nay sống trong lý trí", #7
    "Nhưng bên cạnh em thì luôn easy", #8
    "Anh không nói dối bao giờ đâu (yeah anh không)", #9
    "Mà hào quang phát ra đằng sau (khi em tới)", #10
    "Sao em có thể không biết em lung linh được như nào", #11
    "Bình thường em không có thói quen soi gương hay sao", #12
    "Thề là thấy em giây đầu tiên", #13
    "Anh đã muốn đưa em lên thuyền", #14
    "Baby bấy lâu nay ở đâu", #15
    "Sao giờ mới được nhìn thấy nhau", #16
    "Thật lòng những ngôi sao ngoài kia chẳng có ai lọt vào được mắt anh", #17
    "Xứng tầm được làm một ngôi sao ở tận trên cao nếu anh ngay bên cạnh", #18
    "Baby girl be mine (you)", #19
    "Đó là English", #20
    "Làm người yêu anh nha em đó là tiếng Việt", #21
    "Mà từ xa em y như người nổi tiếng thiệt", #22
    "Nhìn muốn tăng huyết áp cần một hôm đi xông hơi", #23
    "Cần phải bán nhà để nuôi em cũng chơi", #24
    "Em có trốn ra đại dương anh cũng bơi", #25
    "Visa đây baby nếu em thích cứ cà", #26
    "Tiền và xe của anh em cứ đem về nhà giữ nha", #27
    "Anh không nói dối bao giờ đâu (yeah anh không)", #28
    "Mà hào quang phát ra đằng sau (khi em tới)", #29
    "Sao em có thể không biết em lung linh được như nào", #30
    "Bình thường em không có thói quen soi gương hay sao", #31
    "Thề là thấy em giây đầu tiên anh đã muốn đưa em lên thuyền", #32
    "Baby bấy lâu nay ở đâu sao giờ mới được nhìn thấy nhau", #33
    "Thật lòng những ngôi sao ngoài kia chẳng có ai lọt vào được mắt anh", #34
    "Xứng tầm được làm một ngôi sao ở tận trên cao nếu anh ngay bên cạnh", #35
    "Chắc chắn là hạng A A A", #36
    "Phải là hạng A A A", #37
    "Xứng đáng là hạng A A A", #38
    "Phải làm hạng A A A", #39
]


# Thời gian tạm dừng giữa các câu lời bài hát (tạm thời dự kiến)
timings = [
    16, 1, 0.65, 0.65, 0.5, 0.4, 0.3, 0.3, 0.65, 1.25, 1.5, 1.5, 0.5, 0.2, 0.7, 0.7,
    0.5, 0.3, 0.3, 0.1, 0, 0, 0, 0, 0, 0, 0, 1.4, 1.4, 1.5,
    1.2, 0.5, 0.8, 0.4, 1.2, 0.7, 0.7, 0.7
]

music = pygame.mixer.Sound("sao_hang_a.MP3")
music.set_volume(0.5)
def print_line_with_color(line, color):
    for char in line:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

music.play()

for line, delay in zip(lyrics, timings):
    time.sleep(delay)
    color = random.choice(colors)
    print_line_with_color(line, color)
while pygame.mixer.music.get_busy():
    time.sleep(1)

pygame.quit()
#hunga_k12