#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int storage, int usage, vector<int> change) {
    int total_usage = 0;
    for(int i=0; i<change.size(); i++){
        usage = usage + usage * change[i] / 100;
        total_usage += usage;
        if(total_usage > storage){
            return i;
        }
    }
    return -1;
}

int main(){
    vector<int> change = {10, -10, 10, -10, 10, -10, 10, -10, 10, -10};
    cout << solution(5141,500,change) << endl;
    return 0;
}