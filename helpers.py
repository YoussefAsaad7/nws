import re
import random
import threading


def format_msg(message):
    # Remove Links
    msg = re.sub(r'https?://\S+', '', message)
    msg = msg.replace('@QUICKECONEWS', '@Stock_market_earnings1™️')
    msg = msg.replace('cnbc', '').replace('🥇قناة اخبار العالم والاقتصاد', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('https://t.me/businessma7room', '@Stock_market_earnings1™️').replace('محروم', ''). \
        replace('قناة أَخبار الفوركس العاجلة', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('⬤ قناة أَخبار الفوركس العاجلة 📚', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('Telegram.me/ForexBreakingNews ✅', ''). \
        replace('Telegram.me/ForexBreakingNews', ''). \
        replace('🔴 قناة أَخبار الفوركس العاجلة : 🥇', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('قناة اخبار الفوركس العاجلة', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('https://t.me/QUICKECONEWS', '@Stock_market_earnings1™️'). \
        replace('قناة اخبار الفوركس والاقتصاد', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('اخبار الفوركس و الآقتصاد', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('https://t.me/fx_news_34', ''). \
        replace('اخبار الفوركس والاقتصاد ', 'قناة المفكرة الإقتصادية📚📩'). \
        replace('اخبار الفوركس والاقتصاد', 'قناة المفكرة الإقتصادية📚📩') . \
        replace('أَخبار الفوركس العاجلة', 'قناة المفكرة الإقتصادية📚📩') . \
        replace('أخبار الفوركس و الآقتصاد', 'قناة المفكرة الإقتصادية📚📩')

    # remove unneeded tags
    tags_to_remove = ['cnbc']

    for tag in tags_to_remove:
        pattern = re.compile(fr'#{tag}\b', re.IGNORECASE)
        message = pattern.sub('', message)

    msg += '\n\n @Stock_market_earnings1™️'
    msg = random_emoji() + ' ' + msg
    return msg


def random_emoji():
    emojis = ["🟢", "🔻", "🔺", "🚨", "📌", "🔵", "🔴", "🔹", "♦️"]
    return random.choice(emojis)


def get_random_list_item(list):
    return random.choice(list)

def filter_msg(message):
    with open('keywords.txt', 'r', encoding='utf-8') as f:
        keywords = {line.strip() for line in f}
        for keyword in keywords:
            if keyword in message:
                print(f"Filtered Keyword {keyword} Found in {message}")
                f.close()
                return False  # send
        f.close()
        return True  # Don't Send the msg


# Helpers for Dow Analyzer
def dow_analyzer_format_msg(r_c, e_c, f_c, t_r, t_f, d_price, d_pips, sectors):
    msg = 'الداونجونز :'
    msg += '\n'

    msg += '🟢'
    msg += ' '
    msg += f'{r_c}'
    msg += ' '
    msg += 'شركة صعود'
    msg += ' '
    msg += f'( {t_r["symbol"]} '
    msg += 'الأكثر صعوداّ بتأثير +'
    msg += f'{t_r["pips"]}'
    msg += ' نقطة'
    msg += ')\n'

    msg += '◼️'
    msg += ' '
    msg += f'{e_c} '
    msg += 'شركة تعادل'
    msg += '\n'

    msg += '🔻'
    msg += ' '
    msg += f'{f_c} '
    msg += 'شركة هبوط'
    msg += ' '
    msg += f'( {t_f["symbol"]}'
    msg += ' '
    msg += 'الأكثر هبوطاّ بتأثير '
    msg += f'{t_f["pips"]}'
    msg += ' '
    msg += 'نقطة'
    msg += ')'
    msg += '\n\n'

    msg += 'سعر الداونجونز'
    msg += '👁‍🗨'
    msg += ' '
    msg += f'{d_price}'
    msg += ' '
    msg += '('
    if d_pips > 0:
        msg += f'+{d_pips}'
    else:
        msg += f'{d_pips}'
    msg += ' نقطة '
    msg += ')'
    msg += ' مقسمة كالاتي: '
    msg += '\n\n'

    for sector in sectors:
        msg += sector.name
        msg += ' '
        if sector.pips_impact > 0:
            msg += f'(+{sector.pips_impact}'
        else:
            msg += f'({sector.pips_impact}'
        msg += ' نقطة '
        msg += ')'
        msg += ' :'
        msg += '\n'
        for ticker in sector.tickers:
            msg += '$'
            msg += ticker.symbol
            msg += f'({ticker.pips_impact}'
            msg += ' نقطة '
            msg += '), '
        msg += '\n\n'

    msg += '🔵'
    msg += '🕒'
    msg += '-- يتم التحديث اّلياّ كل ربع ساعة من افتتاح السوق حتى اغلاقه'
    msg += '\n'
    msg += '@iqtisadNews™️'
    return msg


def format_dow_analyzer_for_main_channel(msg):
    start_marker = "الداونجونز :"
    end_marker = "مقسمة"

    start_index = msg.find(start_marker)
    end_index = msg.find(end_marker)

    if start_index == -1 or end_index == -1:
        return None

    cut_text = msg[start_index:end_index].strip()
    cut_text += '\n'
    cut_text += '🔵 '
    cut_text += 'لتفاصيل أكثر '
    cut_text += '@dow_trends'
    cut_text += '\n\n'
    cut_text += '@iqtisadNews™️'
    return cut_text


def generate_random_integer(min_value, max_value):
    return random.randint(min_value, max_value)


def schedule_task(task, delay):
    # Schedule the task to run after delay
    timer = threading.Timer(delay, task)
    timer.start()


def generate_random_reaction_emoji():
    reaction_emojis = ["❤️", "👏", "👍", "⚡️", "🔥", "⚡️", "🎉", "🔥", "😱", "🤯", "👀", "🍾", "🐳", "🐳"]
    return random.choice(reaction_emojis)


def check_forwarder_keywords(message_text):
    with open('forwarder_keywords.txt', 'r', encoding='utf-8') as f:
        keywords = {line.strip() for line in f}
        for keyword in keywords:
            if keyword in message_text:
                f.close()
                return True  # Do Forward
        f.close()
        return False  # Do Not Forward
