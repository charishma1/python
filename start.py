import helper

def main():
    print("Name: ", __name__)
    print("Pckage: ", __package__)
    print("FIle: ", __file__)
    helper.main()

if __name__ == "__main__":
    print("hello form main")
    main()