tries = 2
while True:
    try:
        number = int(input("What is your favorite number?\n"))
        print('Inverse is', 1/number)
        break
    except ValueError:
        print('Number please')
    except ZeroDivisionError:
        print('Number other than zero please')
    except Exception:
        print('Something went wrong')
        break
    finally:
        print('Try number', tries)
        tries += 1