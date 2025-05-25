#include <windows.h>
#include <cmath>
#include <cstdlib>

int main() {
    int i = 0;
    while (true) {
        double result = std::sin(i) * std::cos(i);
        malloc(1024 * 1024);
    }
    return 0;
}