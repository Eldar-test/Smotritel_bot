from aiogram import Router, types
router = Router()

@router.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я — Смотритель душ. Готов начать тестирование?")
