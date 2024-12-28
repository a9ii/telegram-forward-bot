import telebot

API_TOKEN = 'YOUR_BOT_API_TOKEN'  # استبدلها برمز API الخاص بالبوت
bot = telebot.TeleBot(API_TOKEN)

group_chat_id = -100<Group_id>  # معرف المجموعة
channel_id = -100<channel_id>   # معرف القناة

# دالة لتحويل الرسائل
@bot.message_handler(content_types=['text', 'photo', 'document', 'audio', 'video', 'sticker', 'video_note', 'voice'])
def forward_to_channel(message):
    try:
        # إذا كانت الرسالة تحتوي على صورة
        if message.content_type == 'photo':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة صورة: {message.message_id}")
        
        # إذا كانت الرسالة تحتوي على مستند
        elif message.content_type == 'document':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة مستند: {message.message_id}")

        # إذا كانت الرسالة تحتوي على نص
        elif message.content_type == 'text':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة نصية: {message.message_id}")
        
        # إذا كانت الرسالة تحتوي على صوت
        elif message.content_type == 'audio':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة صوتية: {message.message_id}")

        # إذا كانت الرسالة تحتوي على فيديو
        elif message.content_type == 'video':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة فيديو: {message.message_id}")

        # إذا كانت الرسالة تحتوي على ملصق
        elif message.content_type == 'sticker':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة ملصق: {message.message_id}")

        # إذا كانت الرسالة تحتوي على ملاحظة فيديو
        elif message.content_type == 'video_note':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة ملاحظة فيديو: {message.message_id}")
        
        # إذا كانت الرسالة تحتوي على رسالة صوتية
        elif message.content_type == 'voice':
            bot.forward_message(channel_id, group_chat_id, message.message_id)
            print(f"تم تحويل رسالة صوتية: {message.message_id}")
        
    except Exception as e:
        print(f"Error: {e}")

# تشغيل البوت
bot.polling(none_stop=True)
