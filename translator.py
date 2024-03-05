from tkinter import Tk, Label, Text, Button, StringVar, OptionMenu
from googletrans import Translator

class TranslatorApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Aplikasi Translator Mutiara")

        self.label_text = Label(master, text="Masukkan teks:")
        self.label_text.pack()

        self.text_input = Text(master, height=5, width=40)
        self.text_input.pack()

        self.label_lang = Label(master, text="Pilih Bahasa Tujuan:")
        self.label_lang.pack()

        self.languages = ["inggris", "rusia", "swedia"]
        self.selected_lang = StringVar(master)
        self.selected_lang.set(self.languages[0])

        self.lang_menu = OptionMenu(master, self.selected_lang, *self.languages)
        self.lang_menu.pack()

        self.label_result = Label(master, text="Hasil Terjemahan:")
        self.label_result.pack()

        self.text_result = Text(master, height=5, width=40, state="disabled")
        self.text_result.pack()

        self.button_translate = Button(master, text="Terjemahkan", command=self.translate_text)
        self.button_translate.pack()

    def translate_text(self):
        text_to_translate = self.text_input.get("1.0", "end-1c")
        target_lang = self.selected_lang.get()

        translator = Translator()
        translation = translator.translate(text_to_translate, dest=target_lang)

        translated_text = translation.text
        self.text_result.config(state="normal")
        self.text_result.delete("1.0", "end")
        self.text_result.insert("1.0", translated_text)
        self.text_result.config(state="disabled")
if __name__ == "__main__" :
    root = Tk()
    app = TranslatorApp(root)
    root.mainloop()