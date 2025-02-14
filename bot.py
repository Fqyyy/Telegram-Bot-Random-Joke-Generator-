import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

subjects = [
    "Программист", "Кот", "Студент", "Физик", "Банана", "Собака", "Чайник", "Геймер", "Пингвин", "Робот",
    "Алгоритм", "Пират", "Инопланетянин", "Дракон", "Бутерброд", "Космонавт", "Вампир", "Зомби", "Единорог", "Хакер",
    "Бобер", "Панда", "Ковбой", "Фея", "Рыцарь", "Сфинкс", "Клоун", "Повар", "Сантехник", "Библиотекарь"
]

verbs = [
    "ел", "писал", "читал", "спал", "танцевал", "играл", "сломал", "потерял", "нашел", "запустил",
    "программировал", "рисовал", "пел", "строил", "разрушал", "изучал", "прятал", "ловил", "варил", "жарил",
    "летал", "плавал", "бегал", "кричал", "шептал", "смеялся", "плакал", "мечтал", "взрывал", "чинил"
]

objects = [
    "код", "книгу", "баг", "диплом", "гитару", "кофе", "клавиатуру", "мышь", "монитор", "сервер",
    "торт", "ракету", "телефон", "корабль", "зонтик", "магию", "пакет", "лампу", "кресло", "стол",
    "окно", "дверь", "галактику", "планету", "комету", "бутерброд", "пиццу", "суп", "чай", "кота"
]

adverbs = [
    "усердно", "весело", "грустно", "странно", "быстро", "медленно", "тихо", "громко", "осторожно", "небрежно",
    "элегантно", "смешно", "серьезно", "неуклюже", "аккуратно", "голодно", "сонно", "зло", "добро", "тайно"
]

places = [
    "в офисе", "на кухне", "в космосе", "в подвале", "на крыше", "в метро", "в зоопарке", "в библиотеке", "в лесу", "в пустыне",
    "на пляже", "в горах", "в замке", "в пещере", "в самолете", "в поезде", "в магазине", "в кафе", "в школе", "в больнице"
]

def generate_joke():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object_ = random.choice(objects)
    adverb = random.choice(adverbs)
    place = random.choice(places)
    
    joke = f"{subject} {adverb} {verb} {object_} {place}."
    return joke

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /joke, чтобы получить случайную шутку.")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke_text = generate_joke()
    await update.message.reply_text(joke_text)

def main():

    token = ""
    

    application = Application.builder().token(token).build()
    

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("joke", joke))
    

    application.run_polling()

if __name__ == "__main__":
    main()