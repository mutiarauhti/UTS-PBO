import tkinter as tk

def konversi_suhu():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    reamur = celsius * 4/5
    kelvin = celsius + 273.15

    label_fahrenheit.config(text=f"Fahrenheit: {fahrenheit:.2f} °F")
    label_reamur.config(text=f"Reamur: {reamur:.2f} °Re")
    label_kelvin.config(text=f"Kelvin: {kelvin:.2f} K")

app = tk.Tk()
app.title("Konversi Suhu")

label_input = tk.Label(app, text="Masukkan suhu dalam Celsius:")
label_input.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Konversi", command=konversi_suhu)
button.pack()

label_fahrenheit = tk.Label(app, text="Fahrenheit: ")
label_fahrenheit.pack()

label_reamur = tk.Label(app, text="Reamur: ")
label_reamur.pack()

label_kelvin = tk.Label(app, text="Kelvin: ")
label_kelvin.pack()

app.mainloop()