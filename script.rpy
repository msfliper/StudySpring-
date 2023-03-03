﻿
init:
    image oleg = "oleg/oleg.png"
    $ left2 = Position(xalign=0.2, yalign=1.1)
    $ right2 = Position(xalign=0.8, yalign=1.1)
    image gg = "gg/gg.png"
define s = Character('Саша', color = "#FF4500")
define gg = Character(" ", image = "gg")
define a = Character("Алена", color = "#FF4500" )
define tch = Character("Преподаватель")
define stranger = Character("Незнакомец", color = "#D2691E"  )
define oleg = Character("Олег", image = "oleg")
define prepod = Character("Преподаватель")
define bileter = Character("Билетёр")
define ivan = Character("Ваня")
define neznakom = Character("Незнакомец")
define neznakom_2  = Character("Второй незнакомец")
define policeman  = Character("Полицейский")
define test_points = 0
define test2_points = 0
define test3_points = 0
define test4_points = 0
define test5_points = 0
define flag = False
define flag_day_4 = False


    
label start:
    play music "audio/mainthem.mp3" volume 0.3 fadein 4
    #scene bg black

    #show gg
    scene bg room
    "Прошло много времени с моего переезда в Санкт-Петербург."

    "Что было до того, как я поступила в ГУМРФ?"
    "Да ничего интересного:"
    " обычный провинциальный город"
    "Небольшой детский сад и ничем не примечательная школа."
    "У меня были друзья "
    "И те, с кем общение не сложилось."
    "В общем говоря"
    "Cамый обыкновенный подросток. "
    "Мне всегда нравился Питер"
    "По сравнению с моим родным городом, он казался сказкой. "
    "Поэтому, когда на ЕГЭ я набрал хорошее количество баллов, я без раздумий решил подавать документы в университет им. Адмирала Макарова."
    "Почему сюда?"
    "Все просто! "
    "Я люблю море и этот вуз лучший для того, чтобы исполнить мои мечты, связанные с морской гладью"
    jump sc1

label sc1:
    scene bg alarmclock
    play sound "sound/alarm.mp3"
    "Резкий звук и сон пропадает вместе с воспоминаниями о нем. "
    "Будильник, к счастью или к сожалению, сегодня работает великолепно"
    "Мне удалось поспать всего лишь 3 часа "
    "Неудивительно, что мои мешки под глазами с каждым днем становятся все больше и больше. "
    "Необходимо нормализовать режим со следующей недели… "
    "Но это на следующей неделе, на этой я очень и очень сильно…"

    menu:
        #"Устала":
            #jump Alena_w
        "Устал":
            jump Alena
    return
label Alena:
    scene bg door
    with Dissolve(2)
    show gg norm
    scene bg knock
    with fade
    play sound "sound/knock.mp3"

    "Кому я нужен таким ранним утром ?"

    menu:
        "Нужно открыть дверь."

        "Открыть дверь.":
            play sound "sound/door.mp3"
            hide gg
            jump sc2

    return
#ввод имени
label sc2:
    hide gg
    scene bg hallway
    with fade

    #show gg norm at left2
    show alena png

    a "Привет! Я из соседней комнаты. Хотела с тобой познакомиться, меня зовут Алена. А тебя как ?"
    gg "Привет! Я "
    $ gg = renpy.input("...")
    $ gg = gg.strip()
    if gg == "":
        $ gg = "@#$%@#$!"
    a "Рада с тобой познакомиться, [gg]!"
    menu:
        "И я с тобой рад познакомиться, ..."

        "Алена":
            a "Удачи в первый день!"
            jump sc3
        "Настя":
            jump what1
        "Кирилл":
            jump what1
    return

label what1:
    hide gg
    hide alena
    show alena angry
    with fade
    a "Я Алёна!!!"
    hide alena
    show gg qu with fade  # Тут по-хорошему добавить более грустную эмоцию
    gg "Извини, пожалуйста! У меня плохая память на имена."
    jump sc3
    return
label sc3:
    hide gg
    scene bg room
    with fade
    show gg norm

    gg "Идея прогуливать универ в первый день не выглядит хорошей, да и делать мне сегодня в общем то нечего. Эх ладно какие у меня сегодня пары."
    hide gg
    scene bg schedule
    with fade
    "Расписание: '9:30-11:05 Менеджмент, 11:15-12:50 Физика, 13:35-15:10 Дискретная математика'"

    gg "Что-то расписание не внушает оптимизма, надеюсь сегодня все пройдет спокойно. Хватит заниматься философией пора собираться, а то такими темпами точно опоздаю. "

label sc4:
    scene bg hall
    play sound "sound/vuz.mp3"
    "Спустя некоторое время в институте"
    show gg q
    gg "Ну и толпа у гардероба! Зная свою невнимательность, главное не потерять номерок."
    scene bg nomer
    hide gg
    "Гардеробщица" "Вот ваш номерок"
    gg "Спасибо!"

    scene bg hall 
    play sound "sound/vuz.mp3"
    show gg classi
    gg "Cкоро начало занятий надо торопиться… ЭЭЭЭХ какая там была первая пара"

    
    menu:

        "Пойти на менеджмент":
            jump menegment
        "Пойти на Физику":
            jump physics

    return

label menegment:
    #все еще холл ВУЗа
    gg "Ну и когда память меня подводила?! На самом деле практически всегда… Но я уверен, что сейчас другой случай"
    gg "Кабинет точно находится на 4 этаже, но где именно… А ладно главное найти знакомые лица, там и нужная аудитория."
    stop sound fadeout 1
    scene bg audi
    play sound "sound/classi.mp3"
    show gg classi
    gg "Спустя недолгое скитание по этажу я всё-таки нахожу нужную аудиторию"
    show gg classi at right
    with fade
    hide gg
    show s norm at left
    s "Эй давай сюда я уже занял нам место."
    gg "Да вижу я не ори так, а то тебя слышно даже на первом этаже"
    s "Ну а что мне делать если без очков ты людей не видишь! Вчера даже не поздоровался со мной! "
    gg "Отстань… Я просто немного невнимательный и не замечаю тебя"
    s "Да-да, одно и тоже оправдание каждый раз…"
    hide s norm
    hide gg
    #фон доски с преподавателем
    show tch norm
    tch "Здравствуйте студенты, садимся и записываем сегодняшнюю тему «Разделение компаний по их целям и размерам"
    hide tch
    show gg classi
    gg "Пссс Саш, дай листочек я тетрадь дома забыл"
    # не забываем вставлять героев и изменять их эмоции в диалоге
    hide gg
    show s norm
    s "И почему я не удивлен…"
    hide s
    show gg angry
    gg "Не душни и поторапливайся"
    hide gg
    show s norm
    s "Мне кажется я должен брать с тебя деньги каждый раз, когда ты что-то забываешь"
    hide s
    show gg norm
    gg  "Знаешь есть такая поговорка: помогаю кому-то не…"
    show gg classi
   #появление преподавателя с фоном доски
    hide gg
    show tch ang
    tch "[gg], хватит болтать! Если вы так хорошо разбираетесь в моем предмете, то скажите нам что значит аббревиатура ОАО."
   #появление гг у доски
    hide tch
    show gg q
    gg "ЭЭЭ… Объединённые Арабские… Острова?"
    hide gg
    show tch norm
    tch "Открытое акционерное общество. Сиди и записывай, иначе с такими познаниями ты никогда не сдашь мой предмет."

    #убираем всех героев, звуки письма, картинка лекции
    hide tch
    play sound "sound/перелистывание.mp3"
    scene bg audi
    "     "
    jump kirill


label physics:
    gg "Ну и когда память меня подводила?! На самом деле практически всегда… Но я уверен, что сейчас другой случай"
    gg "Может я и не знаю номер кабинета, но зато отлично помню, где он находится, надо подняться на 5 этаж повернуть налево, а потом еще раз налево и до конца. Какая же у меня всё-таки феноменальная память, надо будет сходить на шоу талантов."
    "Спустя некоторое время у кабинета физики"
    stranger "В кабинете ни души, неужели я пришел самый первый… Или же я все-таки оши…"
    stranger "A вот и ты наконец. Оставляй свои вещи подходи и бери билет."
    gg "Извините, но тут…"
    stranger "Хватит болтать ты и так опоздал на пересдачу, так что поторапливайся и начинай"
    gg "Но…"
    stranger "БЫСТРЕЕ!!!"
    gg "“Я так и не смог сказать ему что он меня с кем-то перепутал и просидел так половину пары”"
    "Студент" "Извините за опоздание, пробки я еле доехал"
    stranger "Так стоп! Мартынов, тогда кто это?"
    gg "Я [gg]. Я случайно перепутал занятия."
    stranger "Так чего ты молчал и ничего не сказал"
    gg "Но я же…"
    stranger "Все хватит! Бери свои вещи и уходи я и так потратил на тебя кучу времени"
    gg "не повезло же этому студенту."
    gg "“Придя на вторую полупару менеджмента и получив нагоняй от преподавателя за опоздание я сел со своим другом Сашей и начал записывать лекцию”"
    jump kirill