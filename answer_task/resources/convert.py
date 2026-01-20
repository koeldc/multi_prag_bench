import json

def jsonl_to_json(input_file, output_file):
    """Convert JSONL file to JSON array"""
    data = []
    
    # Read JSONL file
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                data.append(json.loads(line))
    
    # Write as JSON array
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Converted {len(data)} records from {input_file} to {output_file}")

# Usage
jsonl_to_json('annotation_samples.jsonl', 'annotation_samples.json')
