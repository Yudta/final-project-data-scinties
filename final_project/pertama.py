# Chatbot Edukasi Pemadam Kebakaran & Penyelamatan

import json
from transformers import pipeline

# Inisialisasi model NLP (gunakan model kecil agar ringan)
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

# Memory sederhana untuk menyimpan riwayat percakapan
chat_history = []

def edukasi_firefighter(user_input):
	"""
	Fungsi untuk memberikan jawaban edukatif tentang pemadam kebakaran & penyelamatan.
	Gaya bahasa santai, mudah dimengerti.
	"""
	# Membaca QnA dari file eksternal (qna.json)
	try:
		with open("qna.json", "r", encoding="utf-8") as f:
			faq = json.load(f)
	except Exception as e:
		return f"Maaf, data QnA tidak bisa diakses: {e}"
	# Cari jawaban di FAQ
	for key, value in faq.items():
		if key in user_input.lower():
			return value
	# Jika tidak ada di FAQ, gunakan model NLP
	response = chatbot(user_input, max_length=100, pad_token_id=50256)
	return response[0]['generated_text']

def main():
	print("\n=== Chatbot Edukasi Pemadam Kebakaran & Penyelamatan ===")
	print("(Tanya apa saja tentang pemadam kebakaran, ketik 'keluar' untuk selesai)")
	while True:
		user_input = input("\nKamu: ")
		if user_input.lower() == 'keluar':
			print("Bot: Makasih udah ngobrol! Tetap waspada ya!")
			break
		chat_history.append({"user": user_input})
		bot_reply = edukasi_firefighter(user_input)
		print(f"Bot: {bot_reply}")
		chat_history.append({"bot": bot_reply})

if __name__ == "__main__":
	main()
