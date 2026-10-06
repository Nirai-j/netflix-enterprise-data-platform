from dotenv import load_dotenv
import os

load_dotenv()

print("HOST =", os.getenv("AURORA_HOST"))
print("PORT =", os.getenv("AURORA_PORT"))
print("DB   =", os.getenv("AURORA_DB"))
print("USER =", os.getenv("AURORA_USER"))
print("PASS =", os.getenv("AURORA_PASSWORD"))