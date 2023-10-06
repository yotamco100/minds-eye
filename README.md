# Mind's Eye

## What is this?
This is a simplified version of the original Mind's Eye - a tool to create Control Flow Graphs of high-level code in XMind.

This version works on path lists, ones you would find as outputs to the `find` command, or a list of paths on a website. The tool will create a `.xmind` file with a mindmap version of your list!

## Why would I need this?
Reading lists and code is hard. Looking at graphs is easier. Also, creating comments and remarks is easier in XMind than in code.

## How do I use this?
Simple! Here's an example:
```bash
python main.py path_list.txt --output ~/Desktop/path_list.xmind
```
That's it! On your Desktop you'll have a `path_list.xmind` file, which is the graph version of your `path_list.txt`.

## How do I extend this?
The code is designed to be slim, but relatively extensible.
 - The `parser` folder stores parsers, which open files, read their contents, and store the result of the parsing process.
 - The `grapher` folder stores graphers, which take that parsed data and graph it.
 
 You can extend `parser/parser.py` to create your own parser, and `grapher/grapher.py` to graph new parsing formats (replacing nested dicts with whatever you want) and/or new graph platforms (replacing XMind with GraphViz, for example!)

 ## What's next?
 Currently this is written in Python for XMind 8, which is obsolete.
 A logical next step would be to transcribe it into JS, which has a new XMind SDK.
 Good luck :)
