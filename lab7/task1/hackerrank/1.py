def swap_case(s):
    swap_string =""
    for i in s:
        asci = ord(i)
        if asci < 91 and asci >64:
            asci +=32
        elif asci <122 and asci > 96:
            asci -=32
        swap_string+=chr(asci)
    return swap_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)