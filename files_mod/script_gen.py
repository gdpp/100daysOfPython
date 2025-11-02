js_code = """
    console.log("Hi from file generated in python")
    
    function add(a: number, b: number): number{
        return a + b
    }
"""

with open("script.ts", "w") as script:
    script.write(js_code)

