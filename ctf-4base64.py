import codecs
import re
import string
import subprocess


def matched(target, encoded):
    """
    Compare two strings character by character and return the number of matching characters.
    """
    res = 0
    for i in range(min(len(encoded), len(target))):
        if target[i] == encoded[i]:
            res += 1
        else:
            break
    return res


def main():
    # Target encoded message
    target = '46004746409548141804243297904243125193404843946697460795444349'

    # Initialize variables
    known = ''  # Known prefix of the original message
    charset = string.ascii_lowercase + string.digits  # Possible characters to test
    best_match = (0, '')  # Best match score and corresponding test string

    # Brute-force loop
    for i in range(10):  # Limit to 10 iterations for demonstration purposes
        for a in charset:
            for b in charset:
                test = known + a + b  # Build a test string by appending two characters
                print(f'Testing: {test}')

                # Write the test string to "message.txt"
                with codecs.open("message.txt", 'wb') as data_file:
                    data_file.write(test.encode())

                try:
                    # Run the external binary to encode the test string
                    result = subprocess.check_output(["./rev_secret_secret.o"])
                    result = result.decode()  # Decode the binary's output
                except subprocess.CalledProcessError:
                    continue  # Skip if the binary fails

                # Extract the encoded message from the binary's output
                encoded_messages = re.findall(r"\d+", result)
                if not encoded_messages:
                    continue  # Skip if no encoded message is found

                encoded = encoded_messages[0]  # Use the first encoded message
                print(f'Encoded: {encoded}')

                # Compare the encoded message with the target
                score = matched(target, encoded)
                print(f'Score: {score}')

                # Update the best match if this test string produces a better score
                if score > best_match[0]:
                    best_match = (score, test)
                    print(f'New best match: {best_match}')

        # Update the known prefix with the best match
        known = best_match[1]
        print(f'Known prefix after iteration {i + 1}: {known}')

        # Reset the best match for the next iteration
        best_match = (0, '')

    # Final result
    print(f'Final decoded message: {known}')


if __name__ == "__main__":
    main()