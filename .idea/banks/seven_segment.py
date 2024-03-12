class sevenSegmentDisplay:
    import time

    segment = [[0] * 4 for _ in range(5)]

    def fill_a():
        segment[0][0] = 1
        segment[0][1] = 1
        segment[0][2] = 1
        segment[0][3] = 1

    def fill_b():
        segment[0][3] = 1
        segment[1][3] = 1
        segment[2][3] = 1

    def fill_c():
        segment[2][3] = 1
        segment[3][3] = 1
        segment[4][3] = 1

    def fill_d():
        segment[4][0] = 1
        segment[4][1] = 1
        segment[4][2] = 1
        segment[4][3] = 1

    def fill_e():
        segment[2][0] = 1
        segment[3][0] = 1
        segment[4][0] = 1

    def fill_f():
        segment[0][0] = 1
        segment[1][0] = 1
        segment[2][0] = 1

    def fill_g():
        segment[2][0] = 1
        segment[2][1] = 1
        segment[2][2] = 1
        segment[2][3] = 1

    def display():
        for i in segment:
            for j in i:
                if j == 1:
                    print("# ", end="")
                else:
                    print("  ", end="")
                time.sleep(0.3)
            print()

    def input_value(value):
        if len(value) > 9:
            value = value[:9]

        for i in value:
            if i != '1' and i != '0':
                raise ValueError("Input Must be 1 or 0")

        for i in range(len(value)):
            if value[i] == '1':
                if i == 0:
                    fill_a()
                elif i == 1:
                    fill_b()
                elif i == 2:
                    fill_c()
                elif i == 3:
                    fill_d()
                elif i == 4:
                    fill_e()
                elif i == 5:
                    fill_f()
                elif i == 6:
                    fill_g()

    if __name__ == "__main__":
        try:
            value = int(input("Enter binary Number: "))
            val_to_string = str(value)
            input_value(val_to_string)
            display()
        except ValueError as e:
            print(e)







