# transfer.py
import tkinter


def packWidgets(widgets):
    for widget in widgets:
        """Would like to throw in error checking here just in-case I write a bad widget"""
        widget.pack()


def declare_frames(tk):
    frames = {
        "Frame1": tkinter.Frame(master=tk, width=100, height=100),
    }

    for frame in frames.values():
        frame.pack()
    return frames


def declare_widgets(tk, frames):
    testLabel = tkinter.Label(
        master=frames.get("Frame1"),
        text="Hello, Tkinter",
    ).place(x=50, y=50)


def main():
    tk = tkinter.Tk()
    tk.title("File Transfer")
    frames = declare_frames(tk)
    declare_widgets(tk, frames)
    tk.mainloop()


if __name__ == "__main__":
    main()
    input()
