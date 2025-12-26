from hello_world import print_input

print_input("Calling from another file")

"""
    python code > byte code > python vm[virtual machine]
    
    compile to byte code 
        > low level and platform independent
    
    __pycache__
        > works only ffor imported files
        > not for top-level files
        
    Python virtual machine
        > code loop to iterate byte code
        > run time engine
        > also knows as python interpreter
        
    byte code is not machine code
        > python specific interpretation
        > cpython,jpython,IronPyton
        > cpython is standard implemenatations
"""