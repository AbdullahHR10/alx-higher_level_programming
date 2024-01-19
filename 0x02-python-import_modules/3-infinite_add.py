#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    args = sys.argv[1:]
    number_of_args = len(sys.argv) - 1
    if number_of_args <= 0:
        result = 0
        print(result)
    else:
        result = sum(map(int, args))
        print(result)
        
