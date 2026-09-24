import tkinter as tk


def main():
	window = tk.Tk()
	window.title("Welcome")
	window.geometry("520x320")
	window.configure(bg="#f4f7fb")

	tk.Label(
		window,
		text="Welcome!",
		font=("Arial", 30, "bold"),
		fg="#1f2937",
		bg="#f4f7fb",
	).pack(pady=(65, 12))

	tk.Label(
		window,
		text="We're glad you're here.",
		font=("Arial", 14),
		fg="#4b5563",
		bg="#f4f7fb",
	).pack(pady=5)

	tk.Button(
		window,
		text="Get Started",
		command=window.destroy,
		font=("Arial", 12, "bold"),
		fg="white",
		bg="#2563eb",
		activebackground="#1d4ed8",
		activeforeground="white",
		relief="flat",
		padx=24,
		pady=10,
		cursor="hand2",
	).pack(pady=30)

	window.mainloop()


if __name__ == "__main__":
	main()
