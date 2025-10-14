import subprocess
import os

def run_nslookup(input_file, output_file):
    try:
        # Open input file and read domains
        with open(input_file, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
        
        # Open output file
        with open(output_file, 'w') as f:
            for domain in domains:
                try:
                    # Run nslookup command
                    result = subprocess.run(['nslookup', domain], 
                                         capture_output=True, 
                                         text=True, 
                                         timeout=10)
                    
                    # Write results to output file
                    f.write(f"--- NSLOOKUP Results for {domain} ---\n")
                    f.write(result.stdout)
                    f.write(result.stderr)
                    f.write("\n" + "="*50 + "\n\n")
                    
                    # Print progress to console
                    print(f"Processed: {domain}")
                    
                except subprocess.TimeoutExpired:
                    f.write(f"--- NSLOOKUP Results for {domain} ---\n")
                    f.write("Error: Lookup timed out\n")
                    f.write("\n" + "="*50 + "\n\n")
                    print(f"Timeout: {domain}")
                except Exception as e:
                    f.write(f"--- NSLOOKUP Results for {domain} ---\n")
                    f.write(f"Error: {str(e)}\n")
                    f.write("\n" + "="*50 + "\n\n")
                    print(f"Error processing {domain}: {str(e)}")
                    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    # Define input and output file paths
    input_file = "domains.txt"  # File containing list of domains
    output_file = "nslookup_results.txt"  # Output file for results
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist")
        print("Please create a file named 'domains.txt' with one domain per line")
        return
    
    print(f"Starting nslookup for domains in {input_file}")
    run_nslookup(input_file, output_file)
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
