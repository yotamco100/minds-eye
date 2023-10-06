from lang_parser.dir_parser import DirParser
from grapher.xmind_grapher import XMindGrapher
import argparse
import os

BANNER = r"""
██                                    
████                                  
  ████                                
  ██████████████                      
    ████████████████                  
    ██████▓▓▒▒▓▓████████              
      ████▓▓▒▒▓▓██████████            
      ████▓▓▒▒▓▓████████████          
        ██▓▓▒▒▓▓██████    ████        
        ██▓▓▒▒▓▓██████    ██████      
          ██▒▒▓▓██████    ██████      
          ██▒▒▒▒▓▓████████████▓▓██    
          ██▓▓▒▒▓▓████████████▓▓██    
          ████▒▒▒▒▓▓████████▓▓▒▒▓▓██  
          ████▓▓▒▒▒▒▓▓████▓▓▒▒▒▒▒▒██  
            ████▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒██  
              ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██        __  ____           ___          ______         
                ████████████▓▓▒▒▒▒▓▓██       /  |/  (_)___  ____/ ( )_____   / ____/_  _____ 
                          ████████████      / /|_/ / / __ \/ __  /|// ___/  / __/ / / / / _ \
                              ████████     / /  / / / / / / /_/ /  (__  )  / /___/ /_/ /  __/
                                  ████    /_/  /_/_/_/ /_/\__,_/  /____/  /_____/\__, /\___/ 
                                    ██                                          /____/       
"""

def parse_arguments():
    """
    Helper function to parse arguments for the program.
    """
    parser = argparse.ArgumentParser(
        prog="Mind's Eye",
        description="An XMind graph generator.")
    parser.add_argument("filename", help="The file to parse.")
    parser.add_argument("--output", help="The path of the output.", default="output.xmind")
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(BANNER)
    print("[+] Starting MindsEye...")
    filename = args.filename
    if not os.path.exists(filename):
        print("[!] The file path you've given was not found.")
        return
    print("[+] Parsing File...")
    my_parser = DirParser(filename)
    parsed_content = my_parser.parse()
    my_grapher = XMindGrapher(args.output, parsed_content)
    print("[+] Generating XMind 8 trees...")
    my_grapher.generate_graph()
    print("[+] Saving graph...")
    my_grapher.save_graph()
    print("[+] Done!")

if __name__ == "__main__":
    main()