import sys # import standard module sys in order to use its function and variables

def main(args):
    # text like "hello world" is called string
    # strings have to be inside quotes "" or ''
    str = ""
    if len(args):
       str = " ".join(args)
    print("hello from ermis " + str)


if __name__ == "__main__":
  args = sys.argv[1:]    # get the system parameters
  main(args)