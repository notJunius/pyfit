import sys
import time

def main():
    print("Welcome to traked!")
    time.sleep(2)
    print("[1] rerun script")
    print("[2] log weight")
    print("[3] exit")
    choice = input("what would you like to do? ")
    match choice:
        case '1': 
            main()
        case '2': 
            print('alrighttttt')
            main()
        case '3': 
            sys.exit()








if __name__ == "__main__":
    main()
