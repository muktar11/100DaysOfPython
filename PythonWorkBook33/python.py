from tkinter import * 
import requests 

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfgi(quote_text, text=quote)



window = Tk()
window.title("kanye says")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="backgorund.img")
canvas.create_image(150, 207, image= background_img)
get_quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


Kanye_img = PhotoImage(file="Kanye,png")
Kanye_button = Button(image=Kanye_img, highlightthickness=0, command=get_quote)
Kanye_button.grid(row=1,  column=0)

window.mainloop()