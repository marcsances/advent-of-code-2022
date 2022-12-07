def main():
    window = []
    with open("input.txt", "r") as f:
        idx = 0
        while True:
            idx = idx + 1
            c = f.read(1)
            if c == "":
                print("not found")
                return
            window = window[0 if len(window) < 14 else 1:14] + [c]
            print(window)
            if len(window) == 14 and len(set(window)) == 14:
                print(idx)
                return


if __name__ == "__main__":
    main()