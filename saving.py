# saving.py
import csv
import os
import uuid
import asyncio # Import asyncio

# Har bir suhbat ID'si uchun yaratilgan fayl nomini saqlash uchun global lug'at.
_session_file_map = {}

async def save_conversation_data_to_csv(session_id: str, question_key: str, user_answer: str, label: str):
    """
    Suhbat ma'lumotlarini CSV faylga saqlash uchun yordamchi funksiya.
    Har bir suhbat uchun noyob fayl yaratadi va foydalanuvchi javoblarini
    bosqichma-bosqich CSVga qo'shadi, endi label bilan birga.
    """
    if session_id not in _session_file_map:
        _session_file_map[session_id] = f"context_{uuid.uuid4().hex}.csv"

    file_name = _session_file_map[session_id]
    file_exists = os.path.exists(file_name)

    try:
       
        with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                # Yangi CSV sarlavhalari
                writer.writerow(["Savol", "Javob", "Label"])

            # Joriy savol, javob va labelni qo'shish
            writer.writerow([question_key, user_answer, label])
        return f"Ma'lumot '{file_name}' fayliga muvaffaqiyatli saqlandi, label: '{label}'."
    except Exception as e:
        return f"Xatolik: Ma'lumotni CSV fayliga saqlashda muammo yuz berdi: {e}"