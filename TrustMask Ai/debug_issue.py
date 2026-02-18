
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anonymizer import KVKKAnonymizer

def debug_issue():
    print("Initializing Anonymizer...")
    anonymizer = KVKKAnonymizer()
    
    text = "Eylül, üniversite sınav sonuçlarını büyük bir merakla bekliyor."
    print(f"\nAnalyzing Text: '{text}'")
    
    # Run full pipeline
    result = anonymizer.anonymize(text)
    
    with open("debug_output.txt", "w", encoding="utf-8") as f:
        f.write(f"Sanitized Text: {result.sanitized_text}\n")

if __name__ == "__main__":
    debug_issue()
