# Read the original sequence file
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Remove ORIGIN, numbers, //, spaces, and newlines
cleaned_content = content.replace('ORIGIN', '').replace('//', '')
# Remove all digits and whitespace
import re
cleaned_sequence = re.sub(r'[\d\s]', '', cleaned_content)

# Extract insulin parts: aa 25-54 and aa 90-110
# Note: Python uses 0-based indexing, so we need to adjust
insulin_part1 = cleaned_sequence[24:54]  # aa 25-54 (indices 24-53)
insulin_part2 = cleaned_sequence[89:109] # aa 90-110 (indices 89-108)

# Combine to get full insulin sequence
insulin_sequence = insulin_part1 + insulin_part2
# Save to clean file
with open('preproinsulin-seq-clean.txt', 'w') as output_file:
    output_file.write(insulin_sequence)