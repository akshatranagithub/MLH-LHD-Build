from win10toast import ToastNotifier
notification = ToastNotifier()

quotes = [
    ["Wake up early everyday"],
    ["Exercise Daily"],
    ["Do Meditation"],
    ["Take a Bath"],
    ["Try Learning something new"],
    ["Study Daily"]
]

for quote in quotes:
    notification.show_toast(quote[0], quote[1], duration = 10)
