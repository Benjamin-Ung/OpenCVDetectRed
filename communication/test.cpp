#include <iostream>
#include<windows.h>  

using namespace std;

int main(){
    int x = 0;
    while(x < 1000){
        //sleep(2);
        cout << to_string(x) + "\n";
        x += 1;
    }
    
    
    return 0;
}