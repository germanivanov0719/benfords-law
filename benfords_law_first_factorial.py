from Benfords_Law import Benfords_Law


def main(init_val=1):
    output = ""
    i = init_val
    min_safe_value = None
    pr_failed = False
    while True:
        if output == "" and min_safe_value == "NONE":
            print(
                f"Test with i == {i} was successful. Safe value as of now: {min_safe_value}\r",
                end="",
            )
            pr_failed = False
        elif output == "" and min_safe_value != "NONE":
            print(
                f"Test with i == {i} was successful. Safe value as of now: {min_safe_value}\r",
                end="",
            )
            pr_failed = False
        elif pr_failed:
            print(f"Test with i == {i} failed")
        else:
            print(f"\nTest with i == {i} failed")
            pr_failed = True
        i += 1
        output = Benfords_Law(1, i, silent=True)


def main_alt(i=1):
    min_safe = None
    while True:
        if Benfords_Law(1, i, silent=True):
            if min_safe is None:
                min_safe = i
            print(f"Test with {i} successful. Min value: {min_safe}.")
        else:
            min_safe = None
            print(f"Test with {i} failed.")
        i += 1


if __name__ == "__main__":
    # main(1800)
    main_alt(1700)
