choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
    print('\n')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print('----------')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print('----------')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    # above code is to print board layouts

    try:
        choice = int(input("> ").strip())
    except ValueError:
        print("Please enter only valid fields from board (0-8)")
        continue
