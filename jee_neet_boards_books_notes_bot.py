from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8756798363:AAF5Q_gduy-yaEOgbcNUoyCG2k_-EcJ8-xA"
CHANNEL = "@jeementor"


# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("✅ Check Subscription", callback_data="check_sub")]
    ]

    await update.message.reply_text(
        "👋 Welcome!\n\nFirst join our channel to continue:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ---------------- CHECK SUB ----------------
async def check_subscription(user_id, context):
    try:
        member = await context.bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False


# ---------------- HANDLER ----------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    # ================= CHECK SUB =================
    if query.data == "check_sub":
        if await check_subscription(user_id, context):

            keyboard = [
                [InlineKeyboardButton("📘 JEE", callback_data="jee")],
                [InlineKeyboardButton("📗 NEET", callback_data="neet")],
                [InlineKeyboardButton("📙 BOARDS", callback_data="boards")],
                [InlineKeyboardButton("🏠 Home", callback_data="home")]
            ]

            await query.message.edit_text(
                "✅ Subscription verified!\n\nChoose category:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            keyboard = [
                [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL.replace('@','')}")],
                [InlineKeyboardButton("🔁 Check Again", callback_data="check_sub")]
            ]

            await query.message.edit_text(
                "❌ You have not joined the channel yet.",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    # ================= HOME =================
    elif query.data in ["home", "back_home"]:
        keyboard = [
            [InlineKeyboardButton("📘 JEE", callback_data="jee")],
            [InlineKeyboardButton("📗 NEET", callback_data="neet")],
            [InlineKeyboardButton("📙 BOARDS", callback_data="boards")]
        ]

        await query.message.edit_text(
            "🏠 Main Menu:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= MAIN CATEGORIES =================
    elif query.data == "jee":
        keyboard = [
            [InlineKeyboardButton("📘 Physics", callback_data="jee_phy")],
            [InlineKeyboardButton("📗 Chemistry", callback_data="jee_chem")],
            [InlineKeyboardButton("📙 Maths", callback_data="jee_math")],
            [InlineKeyboardButton("⬅️ Back", callback_data="home")]
        ]

        await query.message.edit_text("📘 JEE Section:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "neet":
        keyboard = [
            [InlineKeyboardButton("⬅️ Back", callback_data="home")]
        ]

        await query.message.edit_text("🚧 NEET coming soon...", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "boards":
        keyboard = [
            [InlineKeyboardButton("⬅️ Back", callback_data="home")]
        ]

        await query.message.edit_text("🚧 BOARDS coming soon...", reply_markup=InlineKeyboardMarkup(keyboard))

    # ================= JEE SUBJECT BACK =================
    elif query.data in ["jee_phy", "jee_chem", "jee_math"]:
        keyboard = [
            [InlineKeyboardButton("📘 PW MODULES", callback_data=f"{query.data}_pw")],
            [InlineKeyboardButton("⬅️ Back", callback_data="jee")]
        ]

        title = {
            "jee_phy": "📘 JEE Physics:",
            "jee_chem": "🧪 JEE Chemistry:",
            "jee_math": "📙 JEE Maths:"
        }

        await query.message.edit_text(
            title[query.data],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ================= PW MODULE MENUS =================
    elif query.data == "jee_phy_pw":
        keyboard = [
            [InlineKeyboardButton("Module 1", callback_data="phy_m1")],
            [InlineKeyboardButton("Module 2", callback_data="phy_m2")],
            [InlineKeyboardButton("Module 3", callback_data="phy_m3")],
            [InlineKeyboardButton("⬅️ Back", callback_data="jee_phy")]
        ]

        await query.message.edit_text("📘 Physics Modules:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "jee_chem_pw":
        keyboard = [
            [InlineKeyboardButton("Module 1", callback_data="chem_m1")],
            [InlineKeyboardButton("Module 2", callback_data="chem_m2")],
            [InlineKeyboardButton("Module 3", callback_data="chem_m3")],
            [InlineKeyboardButton("⬅️ Back", callback_data="jee_chem")]
        ]

        await query.message.edit_text("🧪 Chemistry Modules:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "jee_math_pw":
        keyboard = [
            [InlineKeyboardButton("Module 1", callback_data="math_m1")],
            [InlineKeyboardButton("Module 2", callback_data="math_m2")],
            [InlineKeyboardButton("Module 3", callback_data="math_m3")],
            [InlineKeyboardButton("⬅️ Back", callback_data="jee_math")]
        ]

        await query.message.edit_text("📙 Maths Modules:", reply_markup=InlineKeyboardMarkup(keyboard))

    # ================= MODULE CONTENT + BACK =================
    elif query.data == "phy_m1":
        await query.message.edit_text(
            "📘 Physics Module 1\n\nhttps://study-notes-hub.blogspot.com/2026/05/the-importance-of-study-in-life-of.html?m=1",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_phy_pw")]])
        )

    elif query.data == "phy_m2":
        await query.message.edit_text(
            "📘 Physics Module 2\n\nhttps://study-notes-hub.blogspot.com/2026/05/unlock-your-future-true-importance-of.html?m=1",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_phy_pw")]])
        )

    elif query.data == "phy_m3":
        await query.message.edit_text(
            "📘 Physics Module 3\n\nhttps://study-notes-hub.blogspot.com/2026/05/how-to-build-effective-study-habits.html?m=1",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_phy_pw")]])
        )

    elif query.data == "chem_m1":
        await query.message.edit_text(
            "🧪 Chemistry Module 1\n\nhttps://study-notes-hub.blogspot.com/2026/05/the-importance-of-study-in-life-of_5.html?m=1",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_chem_pw")]])
        )

    elif query.data == "chem_m2":
        await query.message.edit_text(
            "🧪 Chemistry Module 2\n\nhttps://study-notes-hub.blogspot.com/2026/05/unlock-your-future-true-importance-of_5.html",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_chem_pw")]])
        )

    elif query.data == "chem_m3":
        await query.message.edit_text(
            "🧪 Chemistry Module 3\n\nhttps://study-notes-hub.blogspot.com/2026/05/how-to-build-effective-study-habits_5.html?m=1",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_chem_pw")]])
        )

    elif query.data == "math_m1":
        await query.message.edit_text(
            "📙 Maths Module 1\n\nhttps://study-notes-hub.blogspot.com/2026/05/the-importance-of-study-in-life-of_92.html",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_math_pw")]])
        )

    elif query.data == "math_m2":
        await query.message.edit_text(
            "📙 Maths Module 2\n\nhttps://study-notes-hub.blogspot.com/2026/05/unlock-your-future-true-importance-of_66.html?m=1",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_math_pw")]])
        )

    elif query.data == "math_m3":
        await query.message.edit_text(
            "📙 Maths Module 3\n\nhttps://study-notes-hub.blogspot.com/2026/05/how-to-build-effective-study-habits_92.html",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="jee_math_pw")]])
        )

    # ================= SOON =================
    elif query.data == "soon":
        await query.message.reply_text("🚧 This feature is coming soon...")


# ---------------- MAIN ----------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()