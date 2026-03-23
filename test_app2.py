import traceback
import sys

try:
    import app.main
    print("App imported successfully")
except Exception as e:
    traceback.print_exc()
