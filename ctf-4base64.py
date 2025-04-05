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
    target = '46004746409548141804243297904243125193404843946697460795444349'

    known = ''
    charset = string.ascii_lowercase + string.digits
    best_match = (0, '')


    for i in range(10):
        for a in charset:
            for b in charset:
                test = known + a + b
                print(f'Testing: {test}')

                with codecs.open("message.txt", 'wb') as data_file:
                    data_file.write(test.encode())

                try:
                    result = subprocess.check_output(["./rev_secret_secret.o"])
                    result = result.decode()
                except subprocess.CalledProcessError:
                    continue

                encoded_messages = re.findall(r"\d+", result)
                if not encoded_messages:
                    continue

                encoded = encoded_messages[0]
                print(f'Encoded: {encoded}')


                score = matched(target, encoded)
                print(f'Score: {score}')


                if score > best_match[0]:
                    best_match = (score, test)
                    print(f'New best match: {best_match}')


        known = best_match[1]
        print(f'Known prefix after iteration {i + 1}: {known}')


        best_match = (0, '')


    print(f'Final decoded message: {known}')


if __name__ == "__main__":
    main()