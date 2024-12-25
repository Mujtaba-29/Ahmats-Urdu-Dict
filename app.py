import streamlit as st
import random
from transformers import pipeline

# Set up the Streamlit app
st.set_page_config(page_title="احمت صاحب کی اردو ڈکشنری", page_icon="📚")

# Add a beautiful header with emojis
st.markdown("<h1 style='text-align: center; color: purple;'>📖 احمت صاحب کی اردو ڈکشنری 📖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>🌟 ہر لفظ ایک پراسرار کہانی 🌟</h3>", unsafe_allow_html=True)

# Add a sense of mystery in the introduction
st.write("🔍 **یہ ایک پراسرار اردو ڈکشنری ہے۔**")
st.write("**کیا آپ جاننا چاہتے ہیں کہ اس لفظ کا مطلب کیا ہے؟** صرف ایک بٹن پر کلک کریں اور احمت صاحب کی تخلیقی دنیا میں قدم رکھیں! 💡")
st.markdown("---")

# Generate a list of 300 words ending with 'نما' without explicit numbering
words = [
    "ٹکمل نما", "چنگچی نما", "کتاب نما", "پنکھا نما", "گھڑی نما", "پتھر نما",
    "موم بتی نما", "چراغ نما", "آئینہ نما", "شیشہ نما", "پانی نما", "ہوا نما",
    "روشنی نما", "چاند نما", "سورج نما", "گاڑی نما", "سائیکل نما", "مشین نما",
    "کھلونا نما", "دوائی نما", "کرسی نما", "میز نما", "صوفہ نما", "بیگ نما",
    "کمپیوٹر نما", "موبائل نما", "پرندہ نما", "درخت نما", "پھول نما", "پتہ نما",
    "کھڑکی نما", "دروازہ نما", "قالین نما", "چائے نما", "کافی نما", "پلیٹ نما",
    "چمچ نما", "چاقو نما", "سوراخ نما", "شمع نما", "گلاب نما", "جھیل نما",
    "سمندر نما", "دریا نما", "تالاب نما", "پتنگ نما", "ہاتھی نما", "شیر نما",
    "چیتا نما", "بلی نما", "کتا نما", "شہد نما", "پھل نما", "میوہ نما",
    "مٹھائی نما", "برف نما", "بندوق نما", "گھوڑا نما", "سانپ نما", "خرگوش نما",
    "لومڑی نما", "چھتری نما", "بارش نما", "طوفان نما", "میدان نما", "پہاڑ نما",
    "گھاٹی نما", "جنگل نما", "چاندی نما", "سونا نما", "ہیرا نما", "موتی نما",
    "کانچ نما", "مٹی نما", "پلاسٹک نما", "کاغذ نما", "قلم نما", "کتابچہ نما",
    "رنگ نما", "بکس نما", "سکہ نما", "ڈالر نما", "روپیہ نما", "کھانے نما",
    "پینے نما", "خوشبو نما", "بدبو نما", "دھوپ نما", "سایہ نما", "جھوٹ نما",
    "سچ نما", "دوست نما", "دشمن نما", "دکان نما", "گھر نما", "محل نما",
    "مسجد نما", "مندر نما", "چرچ نما", "بازار نما", "ہوٹل نما", "جیل نما",
    "اسکول نما", "کالج نما", "یونیورسٹی نما", "کتب خانہ نما", "دفتر نما", "فائل نما",
    "سفری نما", "جوتا نما", "کپڑا نما", "چادر نما", "چٹائی نما", "کشن نما",
    "بستر نما", "تکیہ نما", "کمبل نما", "لحاف نما", "ہاتھ نما", "پیر نما",
    "چہرہ نما", "آنکھ نما", "ناک نما", "کان نما", "منہ نما", "داڑھی نما",
    "مونچھ نما", "زبان نما", "دل نما", "دماغ نما", "پیٹ نما", "گھڑیال نما",
    "درختچہ نما", "پھولچہ نما", "پتہچہ نما", "پانیچہ نما", "چاکلیٹ نما", "بسکٹ نما",
    "پکوڑا نما", "سموسہ نما", "چائے کپ نما", "روٹی نما", "برتن نما", "صراحی نما",
    "ٹوکری نما", "گملہ نما", "بیج نما", "جھاڑو نما", "جالی نما", "لکڑی نما",
    "چاکلیٹ نما", "بسکٹ نما", "پکوڑا نما", "سموسہ نما", "چائے نما", "آئسکریم نما",
    "قلفی نما", "کیک نما", "پیالہ نما", "چکن نما", "گوشت نما", "سبزی نما"
]

# Predefined sentence templates without explicit numbers
templates = [
    "یہ ایک خیالی شے ہے جو {word} کی طرح لگتی ہو، مگر {feature}۔",
    "ایک ایسی چیز جو {word} کی طرح دکھائی دیتی ہو اور {feature}۔",
    "{word} ایک فرضی شے ہے جو {feature}۔",
    "یہ ایک عجیب و غریب شے ہے جو {word} کی طرح ہے اور {feature}۔",
    "یہ ایک منفرد شے ہے جو {word} کی طرح منفرد لگتی ہو۔"
] * 10  # Repeat for variety

# Random features for the fictional meanings
features = [
    "رنگ بدل سکتی ہو", "ہوا میں تیر سکتی ہو", "روشنی پیدا کرتی ہو", "خوشبو دیتی ہو",
    "خود بخود غائب ہو سکتی ہو", "کھانے کے قابل ہو", "آواز نکال سکتی ہو", "وقت بتا سکتی ہو",
    "موسیقی بجاتی ہو", "خواب دکھاتی ہو"
]

# Load the Hugging Face pipeline for text generation
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")  # Replace with Urdu-compatible LLM if available

model = load_model()

# Generate random word and fictional meaning when user clicks the button
if st.button("🔮 لفظ دریافت کریں"):
    selected_word = random.choice(words)
    selected_template = random.choice(templates)
    selected_feature = random.choice(features)
    
    # Generate the meaning using the template
    fictional_meaning = selected_template.format(word=selected_word, feature=selected_feature)
    
    # Display the word and its fictional meaning
    st.markdown("<h3 style='text-align: center; color: darkblue;'>✨ آپ کا لفظ ہے ✨</h3>", unsafe_allow_html=True)
    st.write(f"**لفظ:** {selected_word} 🌀")
    st.write(f"**مفہوم:** {fictional_meaning}")
    st.markdown("<p style='text-align: center; color: green;'>یہ لفظ احمت صاحب کی کاوش ہے۔ 🙌</p>", unsafe_allow_html=True)

# Footer with emojis
st.markdown("---")
st.markdown("<p style='text-align: center;'>🌟 شکریہ کہ آپ نے احمت صاحب کی اردو ڈکشنری استعمال کی! 🌟</p>", unsafe_allow_html=True)
