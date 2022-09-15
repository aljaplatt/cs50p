import sys

def main():
    # check the command line args 
    # check_cl_args()
    print(sys.argv) # ['lines_0.py']



def check_cl_args():
    #Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if it is a Python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()