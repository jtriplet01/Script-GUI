import customtkinter

app = customtkinter.CTk()
app.mainloop()
app.title("Script Portal")
app.geometry("500x300")

button = customtkinter.CTkButton(app, text="My Button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()