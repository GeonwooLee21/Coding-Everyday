#include <string>
#include <vector>
using namespace std;

int solution(string s) {
    int answer = 0;

    string compress_string;
    vector<int> compress_string_size;

    if (s.size() == 1) {
        compress_string_size.push_back(1);
    }
    else {
        for (int size = 1; size < s.size()/2 + 1; size++) {
            // initial substring
            string substring = s.substr(0, size);
            int count = 1;

            int i;
            for (i = size; i < s.size(); i += size) {
                if (substring == s.substr(i, size)) {
                    count++;
                }
                else {
                    // compress s
                    if (count == 1) {
                        compress_string += substring;
                    }
                    else {
                        compress_string += to_string(count);
                        compress_string += substring;
                    }
                    // substring update
                    substring = s.substr(i, size);
                    count = 1;
                }
            }
            
            // compress s
            if (count == 1) {
                compress_string += substring;
            }
            else {
                compress_string += to_string(count);
                compress_string += substring;
            }

            compress_string_size.push_back(compress_string.size());
            compress_string.clear();
        }
    }

    // find shortest compressed string length
    int min = 1001;
    for (int i = 0; i < compress_string_size.size(); i++) {
        if (compress_string_size[i] < min) {
            min = compress_string_size[i];
        }
    }
    answer = min;

    return answer;
}