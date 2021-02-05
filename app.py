import tkinter as tk
from downloader import downloadFile

imgList = [
    "https://anime-girls-holding-programming-books.netlify.app/static/Yaoyorozu_Momo_Holding_Go_Programming_Language-b5f73b96a822664c23fe22e11f23bdfc.png",
    "https://anime-girls-holding-programming-books.netlify.app/static/Tkmiz_Art_With_Python_Programming_Book-0357d34d4da5d7eb34a548c5cb90aeee.png",
    "https://anime-girls-holding-programming-books.netlify.app/static/Megumin_Reading_Programming_Gengo_Ruby-aba8f284555a669a5e07959bda852141.jpg",
    "https://anime-girls-holding-programming-books.netlify.app/static/Senko-san_Scala-5e145303f6209173ccccac47b4524433.png",
    "https://anime-girls-holding-programming-books.netlify.app/static/Zero_Two_Holding_Nodejs_8_the_Right_Way-6b2719eb6b765a3b947addd2eca9f723.png"]

root = tk.Tk()
root.title("Code downloader")

def startDownloader():
    for img in imgList:
        downloadFile(img)
        textBox.insert(tk.INSERT, "1 file downloaded \n")

canvas = tk.Canvas(root, height=700, width=700, bg="#fffaeb")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

download = tk.Button(frame, text="Download Files", padx=10, pady=5, fg="black",
                     command=startDownloader, bg="#fffaeb")
download.pack()

textBox = tk.Text(frame)
textBox.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

root.mainloop()
