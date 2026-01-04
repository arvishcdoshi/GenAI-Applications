#include <iostream>
#include <vector>

// Function implementing binary search
int binarySearch(const std::vector<int>& arr, int left, int right, int x) {
    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Check if x is present at mid
        if (arr[mid] == x) {
            return mid;
        }

        // If x is greater, ignore left half
        if (arr[mid] < x) {
            left = mid + 1;
        } else {
            // If x is smaller, ignore right half
            right = mid - 1;
        }
    }
    // Element is not present in the array
    return -1;
}

int main() {
    std::vector<int> arr = {2, 3, 4, 10, 40};
    int x = 10;
    int result = binarySearch(arr, 0, arr.size() - 1, x);
    if (result != -1) {
        std::cout << "Element is present at index " << result << std::endl;
    } else {
        std::cout << "Element is not present in the array" << std::endl;
    }
    return 0;
}