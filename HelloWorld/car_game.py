command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car already running.")
        else:
            print("car is start")
            started = True
    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            print("car is stopped")
            started = False

    elif command == "quit":
        break
    elif command == "help":
        print("""
>start
>stop
>help
>quit
        """)
    else:
        print("i don't understand")