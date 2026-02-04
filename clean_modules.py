# This script removes specific modules from sys.modules to force reloading them.

# Import sys to access the modules currently loaded
import sys

# Define variables
modules_to_remove = []

# Create a list of modules to remove (e.g., everything inside your project package)
def get_modules_to_remove():
     return [
         name for name in sys.modules.keys() 
         if name.startswith("agent-framework") or name.startswith("azure-ai") # Replace with your package name
     ]

# Function to remove specified modules from sys.modules
def clean_modules():
    modules_to_remove = get_modules_to_remove()

    # Is there anything to remove?
    if not modules_to_remove:
        print("No modules to remove.")
        return

    for module in modules_to_remove:
        print(f"- {module}")
    
    for module_name in modules_to_remove:
        del sys.modules[module_name]

def print_modules():
    for module_name in sys.modules.keys():
        print(f"-- {module_name}")

# Main execution
def main():
    
    print_modules()
    clean_modules()

if __name__ == "__main__":
    main()
