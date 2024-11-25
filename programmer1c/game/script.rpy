# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# Пример define e = Character('Эйлин', color="#c8ffc8")

define Nate = Character('Нэйт', color = "#FFFFFF")
define Sam = Character('Сэм', color = "#000000")
define Bella_II = Character('Белла_ИИ', color = "#FFFFFF")
define Vincent = Character('Винсент', color = "#FFFFFF")
define Agent = Character('Нэйт', color = "#FFFFFF")
define Bella_Human = Character('Белла_человек', color = '#FFF000')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    # Пример вывода фразы: e "Вы создали новую игру Ren'Py."

    # Сцена 1, Фон 1, Участники: Nate
    Nate "Утро доброе… Какой сегодня день?.. А не важно, в любом случае я не хочу вставать."

    Nate "Для меня это нормально, я часто провожу свои дни за компьютером или телефоном, иногда вообще не вставая с кровати."
    
    Nate "Мне 18 и я уже почти год живу один. Родители давно смирились с тем, что я ничем не интересуюсь и не занимаюсь, и просто присылают мне столько денег, сколько мне хватает на проживание."
    
    Nate "Чтож, может быть сегодня это измениться?"
    
    Nate "Мой взгляд падает на компьютер, подаренный мне дедом, несколько лет назад."
    
    Nate "Хмм… Не так давно друг программист советовал мне изучить программирование… Наверное я всë же слишком ленив для этого."
    
    Nate "Я, как обычно беру свой телефон."
    
    Nate "Я смотрю в экран уже минуту, и мне не приходит в голову ничего, чем я бы мог себя занять… Всë надоело."
    
    Nate "Я снова смотрю на компьютер."
    
    Nate "Может всë же попробовать? Всë равно мне нечего делать."
    
    Nate "Надо сходить к другу, пусть скажет с чего мне начинать."
    
    Nate "…"
    
    Nate "Несмотря на то что я сказал, я не встал с кровати."
    
    Nate "Может завтра? Меня всë ещë клонит в сон, но могу ли я позволить себе откладывать это дело?"

    # Прописать Выбор


    return