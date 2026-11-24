import streamlit as st
import datetime

st.set_page_config(page_title="Cafe Chatbot", page_icon="☕", layout="centered")

st.markdown("""
<style>
    .main { background-color: #FFFFFF; }
    .stChatMessage { border-radius: 12px; }
    .footer { text-align: center; color: #888; font-size: 13px; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

st.title("☕ Cafe & Restaurant")
st.write("Welcome! Ask about Menu, Prices, Timing, Reservation or Delivery.")

CAFE_NAME = "Cafe Islamabad"
WHATSAPP_DISPLAY = "+92 3****"

MENU = {
    "coffee": "Hot Coffee - Rs. 450\nIced Coffee - Rs. 550\nCappuccino - Rs. 500",
    "pizza": "Chicken Pizza (Small) - Rs. 900\nChicken Pizza (Large) - Rs. 1,600\nCheese Pizza - Rs. 1,200",
    "burger": "Zinger Burger - Rs. 650\nBeef Burger - Rs. 750\nChicken Burger - Rs. 550",
    "pasta": "Alfredo Pasta - Rs. 850\nChicken Pasta - Rs. 950",
    "dessert": "Brownie - Rs. 400\nMolten Lava - Rs. 600\nIce Cream - Rs. 350",
    "tea": "Green Tea - Rs. 250\nSpecial Chai - Rs. 300\nKashmiri Chai - Rs. 450",
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hello! Welcome to {CAFE_NAME}. How can I help you today? You can ask for Menu, Prices, Timing or Book a Table."}
    ]

def get_reply(msg):
    msg = msg.lower()
    words = msg.split()
    if any(w in words for w in ["hi", "hello", "hey", "salam", "assalam"]):
        return "Hello! Welcome to our Cafe. Would you like to see the Menu or Book a Table?"
    if "menu" in msg or "food" in msg or "eat" in msg:
        return "Our Menu:\n\n☕ Coffee & Tea\n🍕 Pizza\n🍔 Burgers\n🍝 Pasta\n🍰 Desserts\n\nWhich one do you want to see? Just type Pizza, Burger, Coffee etc."
    if "coffee" in msg or "cappuccino" in msg or "latte" in msg:
        return MENU["coffee"]
    if "pizza" in msg:
        return MENU["pizza"]
    if "burger" in msg:
        return MENU["burger"]
    if "pasta" in msg:
        return MENU["pasta"]
    if "dessert" in msg or "sweet" in msg or "brownie" in msg or "cake" in msg:
        return MENU["dessert"]
    if "tea" in msg or "chai" in msg:
        return MENU["tea"]
    if "price" in msg or "rate" in msg or "cost" in msg:
        return "Prices start from Rs. 250. Coffee Rs. 450, Burger Rs. 550, Pizza Rs. 900. Which item price do you want?"
    if "timing" in msg or "open" in msg or "close" in msg or "time" in msg:
        return "We are open daily: 11:00 AM to 12:00 AM.\nFriday: 3:00 PM to 12:00 AM."
    if "location" in msg or "address" in msg or "where" in msg:
        return "We are located in Islamabad, Pakistan."
    if "delivery" in msg or "home" in msg:
        return "Yes! Home Delivery available in Islamabad. Delivery charges Rs. 200. Delivery time 30-45 minutes."
    if "book" in msg or "table" in msg or "reserve" in msg or "reservation" in msg:
        return "Sure! To book a table, please fill the Reservation Form on the right side. Or WhatsApp us on " + WHATSAPP_DISPLAY
    if "order" in msg or "buy" in msg:
        return f"You can order on WhatsApp: {WHATSAPP_DISPLAY} or fill the form on the right."
    if "contact" in msg or "number" in msg or "whatsapp" in msg or "phone" in msg:
        return f"You can contact us on WhatsApp: {WHATSAPP_DISPLAY}"
    if "thank" in msg or "thanks" in msg:
        return "Thank you for visiting us! Hope to see you soon. 😊"
    if "bye" in msg:
        return "Good Bye! Have a great day. ☕"
    return "I can help with Menu, Prices, Timing, Delivery or Table Booking. What would you like? Try typing 'Menu' or 'Pizza'."

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    reply = get_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

st.sidebar.header("📅 Book a Table")
with st.sidebar.form("reserve"):
    name = st.text_input("Your Name")
    persons = st.selectbox("Persons", ["1", "2", "3", "4", "5+"])
    date = st.date_input("Date")
    time = st.selectbox("Time", ["12:00 PM", "2:00 PM", "4:00 PM", "6:00 PM", "8:00 PM", "10:00 PM"])
    submitted = st.form_submit_button("Confirm Booking")
    if submitted:
        st.sidebar.success(f"Thank you {name}! Table booked for {persons} persons on {date} at {time}.")
        with open("reservations.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | {name} | {persons} | {date} | {time}\n")

st.sidebar.write(f"💬 WhatsApp: {WHATSAPP_DISPLAY}")
st.markdown("<div class='footer'>Islamabad, Pakistan</div>", unsafe_allow_html=True)
